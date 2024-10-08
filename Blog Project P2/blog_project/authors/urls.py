from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.registration, name = 'registration'),
    path('login/',views.user_login, name = 'login'),
    path('logout/',views.user_logout, name = 'logout'),
    path('profile/',views.profile, name = 'profile'),
    path('profile/edit_profile/',views.edit_profile, name = 'edit_profile'),
    path('profile/edit_profile/change_pass/',views.change_pass, name = 'change_pass'),
]