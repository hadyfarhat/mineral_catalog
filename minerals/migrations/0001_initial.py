# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=500, blank=True, null=True)),
                ('image_filename', models.CharField(max_length=500, blank=True, null=True)),
                ('image_caption', models.CharField(max_length=500, blank=True, null=True)),
                ('category', models.CharField(max_length=500, blank=True, null=True)),
                ('formula', models.CharField(max_length=500, blank=True, null=True)),
                ('strunz_classification', models.CharField(max_length=500, blank=True, null=True)),
                ('crystal_system', models.CharField(max_length=500, blank=True, null=True)),
                ('unit_cell', models.CharField(max_length=500, blank=True, null=True)),
                ('color', models.CharField(max_length=500, blank=True, null=True)),
                ('crystal_symmetry', models.CharField(max_length=500, blank=True, null=True)),
                ('cleavage', models.CharField(max_length=500, blank=True, null=True)),
                ('mohs_scale_hardness', models.CharField(max_length=500, blank=True, null=True)),
                ('luster', models.CharField(max_length=500, blank=True, null=True)),
                ('streak', models.CharField(max_length=500, blank=True, null=True)),
                ('diaphaneity', models.CharField(max_length=500, blank=True, null=True)),
                ('optical_properties', models.CharField(max_length=500, blank=True, null=True)),
                ('refractive_index', models.CharField(max_length=500, blank=True, null=True)),
                ('crystal_habit', models.CharField(max_length=500, blank=True, null=True)),
                ('specific_gravity', models.CharField(max_length=500, blank=True, null=True)),
            ],
        ),
    ]
