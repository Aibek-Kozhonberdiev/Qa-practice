from django.db import models


SVG_ICONS = (
    ('M248 8C111 8 0 119 0 256s111 248 248 248 248-111 248-248S385 8 248 8zm0 96c48.6 0 88 39.4 88 88s-39.4 88-88 88-88-39.4-88-88 39.4-88 88-88zm0 344c-58.7 0-111.3-26.6-146.5-68.2 18.8-35.4 55.6-59.8 98.5-59.8 2.4 0 4.8.4 7.1 1.1 13 4.2 26.6 6.9 40.9 6.9 14.3 0 28-2.7 40.9-6.9 2.3-.7 4.7-1.1 7.1-1.1 42.9 0 79.7 24.4 98.5 59.8C359.3 421.4 306.7 448 248 448z', 'Человек'),
    ('M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm144 276c0 6.6-5.4 12-12 12h-92v92c0 6.6-5.4 12-12 12h-56c-6.6 0-12-5.4-12-12v-92h-92c-6.6 0-12-5.4-12-12v-56c0-6.6 5.4-12 12-12h92v-92c0-6.6 5.4-12 12-12h56c6.6 0 12 5.4 12 12v92h92c6.6 0 12 5.4 12 12v56z', 'Аптечка'),
    ('M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256 119.033 8 256 8s248 111.033 248 248zM227.314 387.314l184-184c6.248-6.248 6.248-16.379 0-22.627l-22.627-22.627c-6.248-6.249-16.379-6.249-22.628 0L216 308.118l-70.059-70.059c-6.248-6.248-16.379-6.248-22.628 0l-22.627 22.627c-6.248 6.248-6.248 16.379 0 22.627l104 104c6.249 6.249 16.379 6.249 22.628.001z', 'Галочка'),
)

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

    class Meta:
        pass

    def __str__(self):
        return self.title

class Datasets(models.Model):
    image = models.CharField(max_length=1000, choices=SVG_ICONS)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=300)
    link = models.CharField(max_length=500)

    class Meta:
        pass

    def __str__(self):
        return self.title

class Statistics(models.Model):
    numbers = models.IntegerField()
    title = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return self.title

class Mentors(models.Model):
    img = models.ImageField(upload_to='portrait/')
    full_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    description_2 = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    class Meta:
        pass

    def __str__(self):
        return self.title

class Courses(models.Model):
    course_type = models.CharField(max_length=60, null=True, blank=True)
    price = models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    title = models.CharField(max_length=50)
    fact_1 = models.CharField(max_length=50)
    fact_2 = models.CharField(max_length=50)
    fact_3 = models.CharField(max_length=50)
    fact_4 = models.CharField(max_length=50)
    fact_5 = models.CharField(max_length=50)
    link = models.CharField(max_length=500)

    class Meta:
        pass

    def __str__(self):
        return self.title

class OffersBlack(models.Model):
    subtitle = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)

    class Meta:
        pass

    def __str__(self):
        return self.title

class Offers(models.Model):
    title = models.CharField(max_length=35)
    content = models.TextField(max_length=100)
    link = models.CharField(max_length=500)

    class Meta:
        pass

    def __str__(self):
        return self.title

class Gratitude(models.Model):
    logo = models.ImageField(upload_to='logo/')

    class Meta:
        pass

    def __str__(self):
        return self.logo

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

    class Meta:
        pass

    def __str__(self):
        return self.title

