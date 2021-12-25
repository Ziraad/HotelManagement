from django.urls import path, include
from rest_framework import routers
from .views import RoomViewSet, rooms_available, Book, BookConfirm, BookCancel

route = routers.DefaultRouter()
route.register(r'room', viewset=RoomViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(route.urls)),
    path('rooms-available/', rooms_available),
    path('book/', Book.as_view()),
    path('confirm-now-booking/', BookConfirm.as_view(), name="book_confirm"),
    path('cancel-room/', BookCancel.as_view(), name='cancel-room'),
]