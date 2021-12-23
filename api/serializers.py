from rest_framework import serializers

from booking.models import Rooms, Booking


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        # fields = '__all__'
        fields = ['room_no', 'start_day', 'end_day', 'amount']

    # def create(self, validated_data):
    #     pass
