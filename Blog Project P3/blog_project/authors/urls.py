from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registration/',views.registration, name = 'registration'),
    # path('login/',views.user_login, name = 'login'),
    path('login/',views.UserLoginView.as_view(), name = 'login'),
    # path('logout/',views.user_logout, name = 'logout'),
    path('logout/',views.LogoutView.as_view(), name = 'logout'), #Not working
    path('profile/',views.profile, name = 'profile'),
    path('profile/edit_profile/',views.edit_profile, name = 'edit_profile'),
    path('profile/edit_profile/change_pass/',views.change_pass, name = 'change_pass'),
]