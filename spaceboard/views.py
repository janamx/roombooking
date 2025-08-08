from datetime import date, time, datetime

from django import forms
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Room, Booking
from .forms import EditingForm


class RoomView(generic.ListView):
    template_name = "spaceboard/overview.html"
    context_object_name = "room_overview"

    def get_queryset(self):
        return Room.objects.order_by("capacity")



class DetailView(generic.DetailView):
    model = Room
    template_name = "spaceboard/detail.html"



class DashboardView(generic.ListView):
    model = Room
    template_name = "spaceboard/dashboard.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(user_id=self.request.user.id)



class BookingView(generic.DetailView):
    model = Room
    template_name = "spaceboard/booking.html"



class EditView(generic.UpdateView):
    model = Booking
    form_class = EditingForm
    template_name = "spaceboard/edit.html"

    def get_success_url(self):
        return reverse_lazy('dashboard')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start'].input_formats = ['%Y-%m-%dT%H:%M']
        form.fields['end'].input_formats = ['%Y-%m-%dT%H:%M']
        return form



def booking_view(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        Booking.book(
            room=room,
            user_id=request.user.id,
            start=request.POST['start'],
            end=request.POST['end']
        )
        return redirect('../../booking-success')

    

def booking_success(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'spaceboard/booking_success.html', {'room': room})



def bookings_api(request):
    room_id = request.GET.get('room')
    user_id = request.GET.get('user')

    bookings = Booking.objects.all()
    if room_id:
        bookings = bookings.filter(room=room_id)
        color = '#111111'
    else:
        if user_id:
            bookings = bookings.filter(user_id=user_id)
            color = '#13711e'

    events = []
    for booking in bookings:
        events.append({
            'id': booking.id,
            'room': f'{booking.room.name}',
            'start': booking.start.isoformat(),
            'end': booking.end.isoformat(),
            'color': color,
            'extendedProps': {
                'room': booking.room.name,
            }
        })
    return JsonResponse(events, safe=False)



def deletion_success(request):
    return render(request, 'spaceboard/deletion_success.html')


def delete(request, pk):
    booking = Booking.objects.get(id=pk)
    booking.delete()
    return redirect('../deletion-success/')



