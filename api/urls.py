from django.urls import path, include
from rest_framework import routers
from booking.views import index, book, book_now, cancel_room, delete_room, book_confirm, roomApi, booking_api

# route = routers.DefaultRouter()
# route.register(r'book', viewset=RoomsViewSet)
# route.register(r'book-now', viewset=BookingViewSet)

urlpatterns = [
    # path('', include(route.urls)),
    path('all-rooms/', roomApi),
    path('book/', booking_api)
    # path('', index, name='index'),
    # path('book', book, name='book'),
    # path('book-now/<int:id>', book_now, name='book-now'),
    # path('cancel-room/<int:id>', cancel_room, name='cancel-room'),
    # path('delete-room/<int:id>', delete_room, name='delete-room'),
    # path('confirm-now-booking', book_confirm, name="book_confirm")
]