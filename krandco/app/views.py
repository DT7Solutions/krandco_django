from django.http import JsonResponse
from django.shortcuts import render
from .models import Contact,Product
from django.core.mail import send_mail,EmailMessage
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import os 

# Create your views here.


def index(request):
    return render(request, 'uifiles/index.html')


def about_us(request):
    return render(request, 'uifiles/about.html')


def tobacco_varieties(request):
    Products = Product.objects.filter().order_by('-Id')
    paginator = Paginator(Products, 6)
    page = request.GET.get('page')
    listproducts = paginator.get_page(page)
    

    return render(request, 'uifiles/tobacco-varieties.html',{'Products':listproducts,'posts':listproducts,'page':page})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        comments = request.POST.get('comments')

        errors = {}
        if not name:
            errors['name'] = 'please fil the name field.'
        
        if not email:
            errors['email'] = 'please fill the email field.'

        if not phone:
            errors['phone'] = 'please fill the phone field.'

        if not address:
            errors['address'] = 'please fill the phone field.'

        if not comments:
            errors['comments'] = 'please fill the phone field.'
        

        else:
            oContact = Contact(Name=name,Email=email,Phone=phone,Address=address,Comments=comments)
            oContact.save()
            return JsonResponse({'success':True})
    
    return render(request, 'uifiles/contact.html')
