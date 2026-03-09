from django.contrib import admin
from .models import Test, Collector, Booking

admin.site.register(Test)
admin.site.register(Collector)
class BookingAdmin(admin.ModelAdmin):

    readonly_fields = (
        'name',
        'phone',
        'address',
        'test',
        'visit_time',

    )

admin.site.register(Booking, BookingAdmin)
