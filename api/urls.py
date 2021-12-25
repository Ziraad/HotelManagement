from django.urls import path, include
from rest_framework import routers
from .views import RoomViewSet, BookDetail, rooms_available, Book, BookConfirm, BookCancel

route = routers.DefaultRouter()
route.register(r'room', viewset=RoomViewSet)
# route.register(r'book-now', viewset=BookingViewSet)
app_name = 'api'

urlpatterns = [
    path('', include(route.urls)),
    # path('room', RoomViewSet.as_view(), name='room'),
    path('rooms-available/', rooms_available),
    path('book/', Book.as_view()),
    path('book/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    # path('book-confirm/', BookCreate.as_view()),
    # path('book-now/<int:id>', book_now, name='book-now'),
    path('confirm-now-booking/', BookConfirm.as_view(), name="book_confirm"),
    path('cancel-room/', BookCancel.as_view(), name='cancel-room'),
]