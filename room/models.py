from django.db import models

class Room(models.Model):
    ROOM_TYPE_CHOICES = (
        ('standard', 'Standard'),
        ('private', 'Private'),
    )
    name = models.CharField(max_length=100) 
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)
    capacity = models.PositiveIntegerField()  
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)



class Booking(models.Model):
    guest_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    special_request = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
