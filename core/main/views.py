from django.shortcuts import render
from django.views.generic import TemplateView
from models.models import *
import requests
class Main(TemplateView):
    template_name = 'main.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employees"] = requests.get("http://127.0.0.1:8000/api/employee/").json()
        context["events"] = requests.get("http://127.0.0.1:8000/api/events/").json()
        context["news"] = requests.get("http://127.0.0.1:8000/api/news/").json()
        return context
    
