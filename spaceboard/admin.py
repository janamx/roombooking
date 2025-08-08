from django.contrib import admin
from django.urls import reverse
from .models import Room, Booking

admin.site.site_url = reverse('spaceboard:dashboard')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'room')
    list_filter = ('id', 'room')