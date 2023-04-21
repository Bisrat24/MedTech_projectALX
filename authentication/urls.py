from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('pharmacy_register/<int:user>/', views.pharmacy_register, name='pharmacy_register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
