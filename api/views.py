from datetime import datetime

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from booking.models import Rooms, Booking
from api.serializers import RoomsSerializer, BookingSerializer


class RoomViewSet(ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


@api_view(['GET'])
def rooms_available(request):
    if request.method == 'GET':
        query = Rooms.objects.filter(is_available=True)
        serializer = RoomsSerializer(query, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class Book(APIView):
    def get(self, request):
        query = Booking.objects.all()
        serializer = BookingSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookConfirm(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        try:
            if serializer.is_valid():
                now = datetime.now().date()
                start_day = serializer.validated_data.get('start_day')
                assert start_day >= now, 'Date must be longer than now'
                end_day = serializer.validated_data.get('end_day')
                no_of_days = (end_day - start_day).days
                room_no = serializer.validated_data.get('room_no')
                room = Rooms.objects.get(id=room_no.id)
                assert room.is_available, 'This room is booked'
                assert room.no_of_days_advance >= no_of_days, 'The selected room is booked between the desired date'
                amount = room.price * int(no_of_days)
                room.is_available = False
                room.save()
                serializer.save(amount=amount)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BookCancel(APIView):
    def post(self, request):
        try:
            assert request.body, 'Body is empty'
            book = Booking.objects.get(id=request.POST.get('id'))
            room = book.room_no
            room.is_available = True
            room.save()
            book.delete()
            return Response({'msg': 'Room reservation was canceled'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
