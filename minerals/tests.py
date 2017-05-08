from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Mineral

class MineralModelTest(TestCase):
    def setUp(self):
        self.m = Mineral.objects.create(
            name="mineral 1"
        )

    def test_mineral_creation(self):
        self.assertEqual("mineral 1", self.m.name)

class MineralViewTest(TestCase):
    def setUp(self):
        self.m = Mineral.objects.create(
            name="mineral 1",
            image_filename="mineral1.jpeg"
        )
        self.m2 = Mineral.objects.create(
            name="mineral 2",
            image_filename="mineral2.jpeg"
        )
        self.m3 = Mineral.objects.create(
            name="mineral 3",
            color="red"
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.m, resp.context['minerals'])
        self.assertIn(self.m2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.m.name)
        self.assertContains(resp, self.m3.name)
        # self.assertContains(resp, self.m3.color)

    def test_mineral_details_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.m.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.m, resp.context['mineral'])
