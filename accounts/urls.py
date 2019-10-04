from django.urls import path
from accounts import views

urlpatterns = [
    path('profile/',views.profile,name='profile'),path('register/',views.userReg.as_view(),name='register'),
]
