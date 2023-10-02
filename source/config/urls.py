from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
]

handler404 = "webapp.views.page_not_found_view"
