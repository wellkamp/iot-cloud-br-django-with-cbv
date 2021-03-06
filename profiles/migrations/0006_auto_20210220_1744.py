# Generated by Django 3.1.7 on 2021-02-20 20:44

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20210220_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='first_name', unique=True),
        ),
    ]
