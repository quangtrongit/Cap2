from django.shortcuts import render
from django.views import View


# Create your views here.

class ContactView(View):
    @staticmethod
    def get(request):
        return render(request, 'contact/contact.html')
