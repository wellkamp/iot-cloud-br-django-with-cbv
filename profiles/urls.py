from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/<slug:slug>', views.ProfileDetailView.as_view(), name='profile'),
    path('profile/create/<int:pk>', views.CreateProfileView.as_view(), name='create_profile'),
    path('profile/update/<slug:slug>', views.ProfileUpdateView.as_view(), name='profile_update')
]