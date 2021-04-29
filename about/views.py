from django.shortcuts import render
from django.views import View


# Create your views here.

class AboutView(View):
    @staticmethod
    def get(request):
        return render(request, 'about/about.html')
