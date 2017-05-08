from django.db import models
import json

# Create your models here.

class Mineral(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    image_filename = models.CharField(max_length=500, blank=True, null=True)
    image_caption = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=500, blank=True, null=True)
    formula = models.CharField(max_length=500, blank=True, null=True)
    strunz_classification = models.CharField(max_length=500, blank=True,
                                             null=True)
    crystal_system = models.CharField(max_length=500, blank=True, null=True)
    unit_cell = models.CharField(max_length=500, blank=True, null=True)
    color = models.CharField(max_length=500, blank=True, null=True) 
    crystal_symmetry = models.CharField(max_length=500, blank=True, null=True)
    cleavage = models.CharField(max_length=500, blank=True, null=True)
    mohs_scale_hardness = models.CharField(max_length=500, blank=True,
                                          null=True)
    luster = models.CharField(max_length=500, blank=True, null=True)
    streak = models.CharField(max_length=500, blank=True, null=True)
    diaphaneity = models.CharField(max_length=500, blank=True, null=True)
    optical_properties = models.CharField(max_length=500, blank=True,
                                         null=True)
    refractive_index = models.CharField(max_length=500, blank=True, null=True)
    crystal_habit = models.CharField(max_length=500, blank=True, null=True)
    specific_gravity = models.CharField(max_length=500, blank=True, null=True)

    @classmethod
    def add_minerals_to_db(cls):
        with open ('assets/data/minerals.json', encoding='utf8') as file:
            minerals = json.load(file)
            for mineral in minerals:
                Mineral(
                    name = mineral.get('name', ''),
                    image_filename = mineral.get('image filename', ''),
                    image_caption = mineral.get('image caption', ''),
                    category = mineral.get('category', ''),
                    formula = mineral.get('formula', ''),
                    strunz_classification = mineral.get('strunz classification', ''),
                    crystal_system = mineral.get('crystal system', ''),
                    unit_cell = mineral.get('unit cell', ''),
                    color = mineral.get('color', ''),
                    crystal_symmetry = mineral.get('crystal symmetry', ''),
                    cleavage = mineral.get('cleavage', ''),
                    mohs_scale_hardness = mineral.get('mohs scale hardness', ''),
                    luster = mineral.get('luster', ''),
                    streak = mineral.get('streak', ''),
                    diaphaneity = mineral.get('diaphaneity', ''),
                    optical_properties = mineral.get('optical properties', ''),
                    refractive_index = mineral.get('refractive index', ''),
                    crystal_habit = mineral.get('crystal habit', ''),
                    specific_gravity = mineral.get('specific gravity', '')
                ).save()
    

