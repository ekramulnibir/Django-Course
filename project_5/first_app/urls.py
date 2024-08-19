from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('form/', views.submit_form, name = 'submit_form'),
    # path('django_form/', views.StudentForm, name = 'django_form')
    path('django_form/', views.PasswordValidationForm, name = 'django_form')
]


