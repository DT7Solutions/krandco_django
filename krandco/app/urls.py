from django.urls import path
from .views import index,about_us,tobacco_varieties,contact



urlpatterns = [
    path('',index,name='index'),
    path('about/',about_us,name='about_us'),
    path('tobacco-varieties/',tobacco_varieties,name='tobacco_varieties'),
    path('contact/',contact,name='contact'),

]