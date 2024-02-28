from django.db import models
import random

# Create your models here.


def generate_trip_id():
    return 'TP' + str(random.randint(10000000, 99999999))


class Trip(models.Model):
    trip_id = models.CharField(max_length=10, primary_key=True, default=generate_trip_id, unique=True)
    user_id = models.CharField(max_length=50)
    vehicle_id = models.CharField(max_length=50)
    route_id = models.ForeignKey('route.Route', on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=100)