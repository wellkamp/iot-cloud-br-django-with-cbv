import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from .models import Sensor, SensorValue
# Create your views here.


class SensorListView(LoginRequiredMixin, ListView):
    model = Sensor
    template_name = 'sensor/sensors.html'
    context_object_name = 'sensors'

    def get_queryset(self):
        return Sensor.objects.filter(user_id=self.request.user.id)


class SensorDetailView(LoginRequiredMixin, DetailView):
    model = Sensor
    template_name = 'sensor/sensor_table.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        sensor = get_object_or_404(Sensor, slug=self.kwargs['slug'])
        sensors = SensorValue.objects.all().filter(user_sensor_id=sensor.id).order_by('-last_date')[:10]
        temperature = [obj.temperature for obj in sensors]
        humidity = [obj.humidity for obj in sensors]
        last_hour = [obj.last_hour.strftime("%H:%M:%S") for obj in sensors]
        context = {
            'sensors': sensors,
            'temperature': json.dumps(temperature),
            'humidity': json.dumps(humidity),
            'last_hour': json.dumps(last_hour),
        }
        return context


class SensorDeleteView(LoginRequiredMixin, DeleteView):
    model = Sensor
    success_url = reverse_lazy('sensors')


class SensorRecordView(LoginRequiredMixin, DeleteView):
    model = SensorValue
    success_url = reverse_lazy('sensors')


'''
class SensorDetailView(DetailView):
    model = Sensor
    template_name = 'sensor/sensor_table.html'

    def get_context_data(self, **kwargs):
        sensor = get_object_or_404(Sensor, slug=self.kwargs['slug'])
        result = SensorValue.objects.all().filter(user_sensor_id=sensor.id)
        context = {
            'sensors': result
        }
        return context
'''

'''
class SensorValueDetailView(DetailView):
    model = SensorValue
    template_name = 'sensor/sensor_table.html'
    context_object_name = 'sensors'

    def get_context_data(self, **kwargs):
        result = SensorValue.objects.filter(user_sensor_id=self.kwargs['pk'])
        context = {
            'sensors': result
        }
        return context
'''

