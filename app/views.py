from django.views.generic import ListView, DetailView
from .models import *

class CarView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'car1'

class AboutCar(DetailView):
    model = Car
    template_name = 'about.html'
    context_object_name = 'car2'
    pk_url_kwarg = 'id'