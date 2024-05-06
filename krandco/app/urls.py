from django.urls import path
from .views import index,about_us,tobacco_varieties,stock_update,contact,csractivity,csrdetails,version



urlpatterns = [
    path('',index,name='index'),
    path('about/',about_us,name='about_us'),
    path('tobacco-varieties/',tobacco_varieties,name='tobacco_varieties'),
    path('stock-update/',stock_update,name='stock_update'),
    # path('csractivity/',csractivity,name='csractivity'),
    path('csrdetails/', csrdetails , name='csrdetails'),
    path('contact/',contact,name='contact'),
    path('version/',version,name='version'),

]