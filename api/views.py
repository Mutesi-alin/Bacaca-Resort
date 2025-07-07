
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.conf import settings
company_phone = settings.COMPANY_WHATSAPP

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Q
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer, AvailabilityCheckSerializer

# ✅ GET all rooms
@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_room_detail(request, id):
    try:
        room = Room.objects.get(pk=id)
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    except Room.DoesNotExist:
        return Response({'error': 'Room not found'}, status=404)

@api_view(['POST'])
def create_room(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def check_availability(request):
    serializer = AvailabilityCheckSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        room_id = data['room_id']
        check_in = data['check_in_date']
        check_out = data['check_out_date']
        
        overlapping = Booking.objects.filter(
            room_id=room_id,
            check_in_date__lt=check_out,
            check_out_date__gt=check_in
        )
        return Response({'available': not overlapping.exists()})
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_booking(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        room = data['room']
        check_in = data['check_in_date']
        check_out = data['check_out_date']
        
        overlapping = Booking.objects.filter(
            room=room,
            check_in_date__lt=check_out,
            check_out_date__gt=check_in
        )
        if overlapping.exists():
            return Response({'error': 'Room is not available for the selected dates.'}, status=409)
        
        booking = serializer.save()
        
        # Create WhatsApp message
        company_phone = "+250786766391"  # Your company WhatsApp number
        message = f"Hello! I've booked {room.name} from {check_in} to {check_out}. Booking ID: {booking.id}. Please confirm payment details."
        whatsapp_url = f"https://wa.me/{company_phone.replace('+', '')}?text={message}"
        
        return Response({
            'message': 'Booking confirmed!',
            'booking': serializer.data,
            'whatsapp_url': whatsapp_url,
            'payment_instructions': 'Please contact us via WhatsApp to complete payment'
        }, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_booking_by_id(request, id):
    try:
        booking = Booking.objects.get(pk=id)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=404)

@api_view(['DELETE'])
def cancel_booking(request, id):
    try:
        booking = Booking.objects.get(pk=id)
        booking.delete()
        return Response({'message': 'Booking canceled successfully'})
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=404)
