from django.urls import path
from . import views

def api_root(request):
    from django.http import JsonResponse
    return JsonResponse({
        "message": "Bacaca Resort API v1.0",
        "available_endpoints": {
            "rooms": "/api/rooms/",
            "room_detail": "/api/rooms/{id}/",
            "create_room": "/api/rooms/create/",
            "availability": "/api/availability/",
            "bookings": "/api/bookings/",
            "booking_detail": "/api/bookings/{id}/",
            "cancel_booking": "/api/bookings/{id}/cancel/"
        }
    })

urlpatterns = [
    path('', api_root),  # Add this for /api/
    path('rooms/', views.get_rooms),
    path('rooms/<int:id>/', views.get_room_detail),
    path('rooms/create/', views.create_room),
    path('availability/', views.check_availability),
    path('bookings/', views.create_booking),
    path('bookings/<int:id>/', views.get_booking_by_id),
    path('bookings/<int:id>/cancel/', views.cancel_booking),
]