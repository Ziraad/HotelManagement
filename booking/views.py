from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Rooms, Booking
from api.serializers import RoomsSerializer, BookingSerializer


@api_view(['GET'])
def room(request):
    if request.method == 'GET':
        query = Rooms.objects.all()
        serializer = RoomsSerializer(query, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def room_available(request):
    if request.method == 'GET':
        query = Rooms.objects.filter(is_available=True)
        serializer = RoomsSerializer(query, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def book(request):
    if request.method == 'GET':
        query = Booking.objects.all()
        print('booking: ', query)
        serializer = BookingSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookCreate(APIView):
    print('in book confirm')
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        try:
            if serializer.is_valid():
                room_no = serializer.data.get('room_no')
                room = Rooms.objects.get(id=room_no)
                room.is_available = False
                room.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(str(e))


def index(request):
    return render(request, 'booking/index.html', {})


def cancel_room(request):
    pass


def delete_room(request):
    pass

