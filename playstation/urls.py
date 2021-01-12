from django.urls import path
from .api import RegistrationAPI, LoginAPI, UserAPI, BookingAPI,ChangePasswordAPI
from knox import views as knox_views
from . import views

urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
    path('booking/', BookingAPI.as_view()),
    path('change-password/',ChangePasswordAPI.as_view()),
    path('profile/',views.ProfileList.as_view())
]