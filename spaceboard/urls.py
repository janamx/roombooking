from django.urls import path

from . import views

app_name = "spaceboard"
urlpatterns = [
    path("", views.RoomView.as_view(), name="overview"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("<int:pk>/booking/", views.BookingView.as_view(), name="booking"),
    path("<int:pk>/booking/book-room/", views.booking_view, name="book-room"),
    path("<int:pk>/booking-success/", views.booking_success, name="booking-success"),
    path("api/bookings/", views.bookings_api, name="bookings-api"),
    path("dashboard/delete/<int:pk>/", views.delete, name="delete"),
    path("dashboard/delete/deletion-success/", views.deletion_success, name="deletion-success"),
    path("dashboard/edit/<int:pk>/", views.EditView.as_view(), name="edit"),
]