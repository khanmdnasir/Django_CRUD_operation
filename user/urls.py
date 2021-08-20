from django.urls import path
from . import views

urlpatterns=[
    path('registration/',views.user_register,name='registration'),
    path('',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]