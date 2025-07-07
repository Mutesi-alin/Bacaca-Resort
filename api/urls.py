from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.get_rooms),
    path('rooms/<int:id>/', views.get_room_detail),
    path('rooms/create/', views.create_room),
    path('availability/', views.check_availability),
    path('bookings/', views.create_booking),  # POST for creating bookings
    path('bookings/<int:id>/', views.get_booking_by_id),  # GET for getting booking
    path('bookings/<int:id>/cancel/', views.cancel_booking),  # DELETE for canceling
]