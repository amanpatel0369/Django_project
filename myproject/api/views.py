from rest_framework.response import Response
from rest_framework.decorators import api_view
from route.models import Route
from .serializers import RouteSerializers
from trip.models import Trip
from .serializers import TripSerializers
from booking.models import Booking
from .serializers import BookingSerializers
from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination): # create a custom pagination class
    page_size = 5 # set the default page size to 5
    page_query_param = 'page' # set the query parameter name for page number
    max_page_size = 10

@api_view(['GET'])
def getRoute(request):
    routes = Route.objects.all()
    paginator = CustomPagination()
    page = paginator.paginate_queryset(routes, request) 
    serializer = RouteSerializers(page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
def postRoute(request):
    serializer = RouteSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("-------------------------------------------------------------------")
        print(serializer.data)
        print("-------------------------------------------------------------------")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #return Response(serializer.data , status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getTrips(request):
    Trips = Trip.objects.all()
    paginator = CustomPagination()
    page = paginator.paginate_queryset(Trips, request) 
    serializer = TripSerializers(page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
def postTrip(request):
    serializer = TripSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("-------------------------------------------------------------------")
        print(serializer.data)
        print("-------------------------------------------------------------------")
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getBookings(request):
    book = Booking.objects.all()
    paginator = CustomPagination()
    page = paginator.paginate_queryset(book, request)
    serializer = BookingSerializers(page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
def postBooking(request):
    serializer = BookingSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("-------------------------------------------------------------------")
        print(serializer.data)
        print("-------------------------------------------------------------------")
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TripList(generics.ListCreateAPIView):
    # specify the queryset and serializer class
    queryset = Trip.objects.all()
    serializer_class = TripSerializers

    #ordering = ['trip_distance', 'driver_name']
    #ordering_fields = ['trip_distance', 'driver_name', 'route_id']

    # use the search parameter to search by driver_name and route__route_name
    search = ['driver_name', 'route_name']
    # allow the clients to specify the search query
    #search_fields = ['driver_name', 'route_name']

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializers

class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializers

class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializers

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers