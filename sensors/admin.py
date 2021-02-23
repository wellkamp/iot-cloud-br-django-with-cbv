from django.contrib import admin

from .models import Sensor, SensorValue


@admin.register(Sensor)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'sensor_name',)


@admin.register(SensorValue)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'humidity')
