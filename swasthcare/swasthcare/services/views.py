from django.shortcuts import render, redirect
from .models import Test,Booking
from datetime import date, timedelta

def services(request):
    tests = Test.objects.all()
    return render(request, 'services/services.html', {'tests': tests})

def book_test(request, test_id):

    test = Test.objects.get(id=test_id)

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        visit_time = request.POST.get("visit_time")
        visit_date = request.POST.get("visit_date")


        today = date.today()
        tomorrow = today + timedelta(days=1)
        day_after = today + timedelta(days=2)

        if visit_date not in [str(tomorrow), str(day_after)]:
            return render(request, "services/booking.html", {
                "test": test,
                "error": "You can only book for tomorrow or day after tomorrow."
            })

        Booking.objects.create(
            test=test,
            name=name,
            phone=phone,
            address=address,
            visit_time=visit_time,
            visit_date=visit_date
        )

        return redirect("booking_success")

    return render(request, "services/booking.html", {
        "test": test
    })

def booking_success(request):

    return render(request, "services/booking_success.html")

def my_bookings(request):

    bookings = Booking.objects.all()

    return render(request,'services/my_bookings.html',{
        'bookings':bookings
    })