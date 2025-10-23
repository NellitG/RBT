from django.urls import path
from . import views

urlpatterns = [
    # path('times/', views.AvailableTimesView.as_view(), name='available_times'),
    path('reservations/', views.ReservationCreateView.as_view(), name='create_reservation'),
]