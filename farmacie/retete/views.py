from django.shortcuts import render
from retete.models import Retete
from django.views.generic import CreateView
# Create your views here.

class CreateReteteView(CreateView):
    model = Retete
    template_name = 'retete.html'
    fields = '__all__'