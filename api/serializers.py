from rest_framework import serializers

from booking.models import Rooms, Booking


class RoomsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rooms
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    # room_no = RoomsSerializer()

    class Meta:
        model = Booking
        fields = '__all__'
