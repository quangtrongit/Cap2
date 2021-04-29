from django.urls import path
from .views import AboutView
from . import views

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
]
