from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Rooms, Booking
from api.serializers import RoomsSerializer, BookingSerializer


@api_view(['GET'])

def roomApi(request):
    if request.method == 'GET':
        query = Rooms.objects.all()
        serializer = RoomsSerializer(query, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def booking_api(request):
    if request.method == 'GET':
        query = Booking.objects.all()
        serializer = BookingSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        room = Rooms.objects.get(room_no=int(request.data['room_no']))
        print('room: ', room)
        if serializer.is_valid():
            room.is_available = False
            room.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, 'booking/index.html', {})


def book(request):
    pass


def book_now(request):
    pass


def cancel_room(request):
    pass


def delete_room(request):
    pass


def book_confirm(request):
    pass
