from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
