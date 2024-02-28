from django.db import models
from django.core.validators import RegexValidator
import random

# Create your models here.
def generate_ticket_id():
    return 'RT' + str(random.randint(10000000, 99999999))

class Booking(models.Model):
    ticket_id = models.CharField(max_length=10, primary_key=True, default=generate_ticket_id, unique=True)
    trip_id = models.ForeignKey('trip.Trip', on_delete=models.CASCADE)
    traveller_name = models.CharField(max_length=100)
    traveller_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    ticket_cost = models.FloatField()
    traveller_email = models.EmailField()