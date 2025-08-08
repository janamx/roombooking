from django.contrib import admin
from .models import Room, Booking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'room')
    list_filter = ('id', 'room')