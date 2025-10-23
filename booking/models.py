from django.db import models

class Reservation(models.Model):
    PAYMENT_CHOICES = [
        ("cash", "Cash"),
        ("card", "Card"),
        ("mpesa", "M-Pesa"),
    ]

    # User Info
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    county = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    # Payment Info
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default="cash")
    card_number = models.CharField(max_length=30, blank=True)
    card_name = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.CharField(max_length=10, blank=True, null=True)
    card_cvc = models.CharField(max_length=10, blank=True, null=True)

    # Booking Info
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date}"
