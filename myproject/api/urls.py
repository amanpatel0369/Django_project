from django.urls import path
from . import views
from .views import TripList, TripDetail
from .views import RouteList , RouteDetail
from .views import BookingList , BookingDetail

urlpatterns = [
    path('', views.getRoute),
    path('postroute/', views.postRoute),
    path('getroute/',views.getRoute),

    path('postrip/',views.postTrip),
    path('gettrips/',views.getTrips),

    path('getbooking/',views.getBookings),
    path('postbooking/',views.postBooking),

    
    path('trips/', TripList.as_view(), name='trip-list'),    #to see all the trips
    path('trips/<str:pk>/', TripDetail.as_view(), name='trip-detail'), #to see all the trips in detail by using their ids


    path('routes/', RouteList.as_view(), name='route-list'),    #to see all the routes
    path('routes/<str:pk>/', RouteDetail.as_view(), name='route-detail'), #to see all the routes in detail by using their ids

    path('booking/',BookingList.as_view(), name='booking-list'),    #to see all the bookings
    path('booking/<str:pk>/',BookingDetail.as_view(), name='booking-detail'), #to see all the bookings in detail by using their ids
]