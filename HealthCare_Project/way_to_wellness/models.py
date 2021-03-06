from django.db import models

class Services(models.Model):
    title1=models.TextField()
    paragraph1=models.TextField()
    image1=models.ImageField(upload_to='landing_page_services/')
    title2=models.TextField()
    paragraph2=models.TextField()
    image2=models.ImageField(upload_to='landing_page_services/')
    title3=models.TextField()
    paragraph3=models.TextField()
    image3=models.ImageField(upload_to='landing_page_services/')

    def __str__(self):
        return self.title1+'   '+self.title2+'   '+self.title3

    class Meta:
        verbose_name_plural='Services'


class Testimonials(models.Model):
    name=models.TextField(max_length=30)
    profession=models.TextField(max_length=500)
    statement=models.TextField()
    image=models.ImageField(upload_to='landing_page_testimonials/')
    url=models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Testimonials'

class AboutUs(models.Model):
    title1=models.TextField()
    paragraph1=models.TextField()
    title2=models.TextField()
    paragraph2=models.TextField()
    title3=models.TextField()
    paragraph3=models.TextField()

    def __str__(self):
        return self.title1+'   '+self.title2+'   '+self.title3

    class Meta:
        verbose_name_plural='About Us'

class Carousel(models.Model):
    image=models.ImageField(upload_to='landing_page_carousel/')
    
    class Meta:
        verbose_name_plural='Carousel'


class Appointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile_no=models.CharField(max_length=15)
    weight=models.FloatField()
    height_ft=models.FloatField()
    height_inches=models.FloatField()
    age=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    msg=models.TextField(blank=True)

    def __str__(self):
        return self.name