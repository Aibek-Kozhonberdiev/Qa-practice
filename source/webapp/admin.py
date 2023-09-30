from django.contrib import admin

from .models import *

class FrontAdmin(admin.ModelAdmin):
    pass

admin.site.register(Front)
admin.site.register(Datasets)
admin.site.register(Statistics)
admin.site.register(Mentors)
admin.site.register(Courses)
admin.site.register(OffersBlack)
admin.site.register(Offers)
admin.site.register(Gratitude)
admin.site.register(Speakers)

