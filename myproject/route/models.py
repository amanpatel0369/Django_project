from django.db import models
import random
# Create your models here.

def generate_route_id():
    return 'RT' + str(random.randint(10000000, 99999999))
class Route(models.Model):
    route_id = models.CharField(max_length=10, primary_key=True, default=generate_route_id, unique=True)
    user_id = models.CharField(max_length=50)
    route_name = models.CharField(max_length=100)
    route_origin = models.CharField(max_length=100)
    route_destination = models.CharField(max_length=100)
    route_stops = models.JSONField()