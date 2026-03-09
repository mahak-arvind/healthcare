from django.urls import path
from .views import services, book_test, booking_success,my_bookings

urlpatterns = [

    path("", services, name="services"),
    path("book/<int:test_id>/", book_test, name="book_test"),
    path("success/", booking_success, name="booking_success"),
    path('my-bookings/', my_bookings, name="my_bookings"),

]