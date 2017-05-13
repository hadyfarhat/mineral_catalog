import random

from django.shortcuts import render, get_object_or_404

from .models import Mineral


def minerals_list(request):
    minerals = Mineral.objects.all()
    return render(request, "minerals/mineral_list.html",
                  {'minerals': minerals})


def mineral_details(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    mineral_image_path = 'minerals/images/{}.jpg'.format(mineral.name)
    return render(request, "minerals/mineral_details.html",
                  {'mineral': mineral,
                   'mineral_image_path': mineral_image_path})


def random_mineral(request):
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    mineral_image_path = 'minerals/images/{}.jpg'.format(
                                                random_mineral.name)
    return render(request, 'minerals/mineral_details.html', {
                                    'mineral': random_mineral,
                                    'mineral_image_path': mineral_image_path})
