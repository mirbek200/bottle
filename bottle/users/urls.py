from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',
                                                redirect_field_name = ''
                                                ),name='login'),
    path('profile/',profile, name = 'profile'),
    path('', auth_views.LogoutView.as_view(template_name='blog/home.html',
                                                redirect_field_name = ''
                                                ),name='logout'),
    ]