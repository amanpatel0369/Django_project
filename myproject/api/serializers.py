from rest_framework import serializers
from route.models import Route
from trip.models import Trip
from booking.models import Booking

class RouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class TripSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'