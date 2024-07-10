from django.http import JsonResponse
from django.shortcuts import render
from .models import Contact,ProductItem
from django.core.mail import send_mail,EmailMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import os 

# Create your views here.


# def index(request):
#     return render(request, 'uifiles/index.html')
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        comments = request.POST.get('comments')

        errors = {}
        if not name:
            errors['name'] = 'Please fill the name field.'
        
        if not email:
            errors['email'] = 'Please fill the email field.'

        if not phone:
            errors['phone'] = 'Please fill the phone field.'

        if not address:
            errors['address'] = 'Please fill the address field.'

        if not comments:
            errors['comments'] = 'Please fill the comments field.'

        if errors:
            return JsonResponse({'success': False, 'errors': errors})
        else:
            oContact = Contact(Name=name, Email=email, Phone=phone, Address=address, Comments=comments)
            oContact.save()

            # Send an email
            email_subject = 'New Contact Submission'
            email_body = f"""
            Name: {name}
            Email: {email}
            Phone: {phone}
            Address: {address}
            Comments: {comments}
            """
            send_mail(
                email_subject,
                email_body,
                'krandco@krandco.in',
                ['krandco@krandco.in'],
                fail_silently=False,
            )

            return JsonResponse({'success': True})
    
    return render(request, 'uifiles/index.html')

def about_us(request):
    return render(request, 'uifiles/about.html')

def tobacco_varieties(request):
    return render (request, 'uifiles/tobacco-varieties.html')

def csractivity(request):
    return render(request, 'uifiles/csr.html')

def csrdetails(request):
    return render(request, 'uifiles/csr.html')
def version(request):
    return render(request, 'uifiles/version.html')


def stock_update(request):
    Product = ProductItem.objects.all()
    # paginator = Paginator(Productitem, 6)
    # page = request.GET.get('page')
    # listproducts = paginator.get_page(page)
    

    return render(request, 'uifiles/stock-update.html',{'Products':Product})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        comments = request.POST.get('comments')

        errors = {}
        if not name:
            errors['name'] = 'please fill the name field.'
        
        if not email:
            errors['email'] = 'please fill the email field.'

        if not phone:
            errors['phone'] = 'please fill the phone field.'

        if not address:
            errors['address'] = 'please fill the address field.'

        if not comments:
            errors['comments'] = 'please fill the comments field.'
        

        else:
            oContact = Contact(Name=name, Email=email, Phone=phone, Address=address, Comments=comments)
            oContact.save()

            # Manually send email
            try:
                msg = MIMEMultipart()
                msg['From'] = 'krandco@krandco.in'
                msg['To'] = 'krandco@krandco.in'
                msg['Subject'] = 'New Contact Submission'
                body = f"""
                Name: {name}
                Email: {email}
                Phone: {phone}
                Address: {address}
                Comments: {comments}
                """
                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('krandco@krandco.in', 'igxgkbkmwwquhinu')
                text = msg.as_string()
                server.sendmail('krandco@krandco.in', 'manideep723@gmail.com', text)
                server.quit()

                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'errors': str(e)})
    
    return render(request, 'uifiles/contact.html')
