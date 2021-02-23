from operator import attrgetter

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.conf import settings
from autoslug import AutoSlugField
User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    AUTOSLUG_FIELDS = ("first_name", "last_name")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    slug = AutoSlugField(populate_from='user', unique=True, always_update=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def get_absolute_url(self):
        return reverse('profile', kwargs={"slug": self.slug})

    def __str__(self):
        return self.first_name


