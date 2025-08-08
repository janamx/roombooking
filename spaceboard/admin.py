from django.contrib import admin
from .models import Room, Booking

#admin.site.register(Room)
#admin.site.register(Booking)
admin.site.site_url = "http://127.0.0.1:8000/spaceboard/dashboard/"


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'room')
    list_filter = ('id', 'room')