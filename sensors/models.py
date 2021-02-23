from django.db import models
from autoslug import AutoSlugField
from django.conf import settings
from django.urls import reverse
User = settings.AUTH_USER_MODEL


class Sensor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sensor_name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='sensor_name', unique=True, always_update=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sensor_name

    class Meta:
        verbose_name = 'sensor'
        verbose_name_plural = 'sensors'

    def get_absolute_url(self):
        return reverse('sensor', kwargs={"slug": self.slug})


class SensorValue(models.Model):
    user_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    last_date = models.DateField()
    last_hour = models.TimeField()

    def __str__(self):
        return str(self.user_sensor)

    class Meta:
        verbose_name = 'sensor_value'
        verbose_name_plural = 'sensor_values'