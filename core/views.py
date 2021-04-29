from django.shortcuts import render
from django.views import View


# Create your views here.

class HomeView(View):
    @staticmethod
    def get(request):
        return render(request, 'homepage/index.html')
