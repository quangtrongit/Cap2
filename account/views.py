from django.shortcuts import render
from django.views import View


# Create your views here.

class AccountView(View):
    @staticmethod
    def get(request):
        return render(request, 'account/account.html')
