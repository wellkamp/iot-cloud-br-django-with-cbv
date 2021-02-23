from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from .models import Profile
from django.conf import settings

User = settings.AUTH_USER_MODEL


class IndexView(TemplateView):
    template_name = 'index.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile/profile.html'


class CreateProfileView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/profile_create.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(CreateProfileView, self).form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/profile_update.html'

    def form_valid(self, form):
        profile = form.save()
        return redirect('profile', slug=profile.slug)

    def get_queryset(self):
        qs = super(ProfileUpdateView, self).get_queryset()
        return qs.filter(user=self.request.user)