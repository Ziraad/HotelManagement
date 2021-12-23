from django.urls import path, include
from rest_framework import routers
from booking.views import room, room_available, book, BookCreate

# route = routers.DefaultRouter()
# route.register(r'book', viewset=RoomsViewSet)
# route.register(r'book-now', viewset=BookingViewSet)

urlpatterns = [
    # path('', include(route.urls)),
    path('rooms/', room),
    path('rooms-available/', room_available),
    path('book/', book),
    path('book-confirm/', BookCreate.as_view()),
    # path('', index, name='index'),
    # path('book', book, name='book'),
    # path('book-now/<int:id>', book_now, name='book-now'),
    # path('cancel-room/<int:id>', cancel_room, name='cancel-room'),
    # path('delete-room/<int:id>', delete_room, name='delete-room'),
    # path('confirm-now-booking', book_confirm, name="book_confirm")
]