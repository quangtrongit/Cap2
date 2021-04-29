from django.urls import path
from .views import AccountView
from . import views

urlpatterns = [
    path('', AccountView.as_view(), name='account'),
]
