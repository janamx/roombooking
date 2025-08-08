from django.apps import AppConfig
from django.urls import reverse


class SpaceboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spaceboard'

    #def ready(self):
     #   from django.contrib import admin
      #  admin.site.site_url = reverse('spaceboard:dashboard')