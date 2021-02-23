from django.urls import path

from . import views

urlpatterns = [
    path('', views.SensorListView.as_view(), name='sensors'),
    # path('<int:pk>/', views.SensorValueDetailView.as_view(), name='sensors-table'),
    path('remove/<slug:slug>/<int:pk>', views.SensorDeleteView.as_view(), name='delete-sensor'),
    path('<slug:slug>/', views.SensorDetailView.as_view(), name='sensors-table'),
    path('remove/<int:pk>', views.SensorRecordView.as_view(), name='delete-record'),
]