# Generated by Django 3.1.7 on 2021-02-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0006_auto_20210222_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
