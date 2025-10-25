from django.contrib import admin
from .models import Reservation as booking

# Register your models here.
@admin.register(booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'county', 'payment', 'date', 'created_at')