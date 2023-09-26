from django.shortcuts import render
from django.views import View

from .models import *


class IndexView(View):
    def get(self, request):
        context = {'test': 'ok'}
        return render(request, 'courses/index.html', context)
