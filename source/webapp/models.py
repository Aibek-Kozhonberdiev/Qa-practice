from django.db import models


class Front(models.Model):
    avatar = models.ImageField(upload_to='avatar/')
    link = models.CharField(max_length=500)
    menu = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    white_name_button = models.CharField(max_length=50)
    white_link_button = models.CharField(max_length=500)
    black_name_button = models.CharField(max_length=50)
    black_link_button = models.CharField(max_length=500)

class Datasets(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=300)
    link = models.TextField(max_length=500)

class Statistics(models.Model):
    numbers = models.IntegerField()
    title = models.CharField(max_length=100)

class Mentors(models.Model):
    img = models.ImageField(upload_to='portrait/')
    full_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

class Courses(models.Model):
    course_type = models.CharField(max_length=60, null=True, blank=True)
    price = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    fact_1 = models.CharField(max_length=50)
    fact_2 = models.CharField(max_length=50)
    fact_3 = models.CharField(max_length=50)
    fact_4 = models.CharField(max_length=50)
    fact_5 = models.CharField(max_length=50)
    link = models.CharField(max_length=500)

class OffersBlack(models.Model):
    subtitle = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)

class Offers(models.Model):
    title = models.CharField(max_length=35)
    content = models.TextField(max_length=100)
    link = models.CharField(max_length=500)

class Gratitude(models.Model):
    logo = models.ImageField(upload_to='logo/')

class Speakers(models.Model):
    title = models.CharField(max_length=40)
    offer_1 = models.TextField(max_length=100)
    offer_2 = models.TextField(max_length=100, blank=True, null=True)
    offer_3 = models.TextField(max_length=100, blank=True, null=True)
    offer_4 = models.TextField(max_length=100, blank=True, null=True)
    offer_5 = models.TextField(max_length=100, blank=True, null=True)
    offer_6 = models.TextField(max_length=100, blank=True, null=True)
    offer_7 = models.TextField(max_length=100, blank=True, null=True)
    offer_8 = models.TextField(max_length=100, blank=True, null=True)
    offer_9 = models.TextField(max_length=100, blank=True, null=True)
    offer_10 = models.TextField(max_length=100, blank=True, null=True)

