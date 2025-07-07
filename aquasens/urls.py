from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({
        "message": "Welcome to Bacaca Resort API",
        "status": "online",
        "version": "1.0",
        "endpoints": {
            "admin": "/admin/",
            "api": "/api/",
            "rooms": "/api/rooms/",
            "availability": "/api/availability/",
            "bookings": "/api/bookings/"
        },
        "documentation": "Visit /api/ for API endpoints"
    })

urlpatterns = [
    path('', api_home),  # Add this line for the root URL
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]