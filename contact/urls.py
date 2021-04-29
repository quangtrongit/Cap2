from django.urls import path
from .views import ContactView
from . import views

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
]