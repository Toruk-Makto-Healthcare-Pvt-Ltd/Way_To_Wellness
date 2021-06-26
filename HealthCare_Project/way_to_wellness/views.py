from django.shortcuts import render
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def home(requests):
   form=AppointmentForm()
   if requests.method == "POST":
      form=AppointmentForm(requests.POST)
      if form.is_valid():
         form.save()
         send_mail=requests.POST.get('email')
         html_content=render_to_string("way_to_wellness/email.html",{"title":'Test Email','content':'Hello'})
         text_content=strip_tags(html_content)
         email=EmailMultiAlternatives(
            #subject
            'Testing',
            #content
            'text_content',
            #from email
            settings.EMAIL_HOST_USER,
            #to email
            [send_mail,settings.EMAIL_HOST_USER],
         )
         email.attach_alternative(html_content,"text/html")
         email.send()
   form=AppointmentForm()
   testimonials=Testimonials.objects.all()
   carousel=Carousel.objects.all().first()
   carousel_items=[]
   for items in Carousel.objects.all():
      carousel_items.append(items)
   if len(carousel_items)>0:
      carousel_items.pop(0)
   services=Services.objects.all()
   about=AboutUs.objects.all()
   context={
         'testimonials':testimonials,
         'carousel':carousel,
         'services':services,
         'about':about,
         'ap_form':form,
         'carousel_items':carousel_items,
      }

   return render(requests,'way_to_wellness/home_page.html',context)