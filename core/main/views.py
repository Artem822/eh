from django.shortcuts import render
from django.views.generic import TemplateView
from models.models import *
import requests
from .forms import SearchForm
from django.shortcuts import redirect
from django.db.models import Q
class Main(TemplateView):
    template_name = 'main.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employees"] = requests.get("http://127.0.0.1:8000/api/employee/").json()
        context["events"] = requests.get("http://127.0.0.1:8000/api/events/").json()
        context["news"] = requests.get("http://127.0.0.1:8000/api/news/").json()
        context['form'] = SearchForm()
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if request.POST.get("search") == "":
            return redirect("/")
        try:
            job_title = Position.objects.get(title__contains=request.POST.get('search'))
        except:
            job_title = 0
        try:
            author_news = Employee.objects.get(username__contains=request.POST.get('search'))
        except:
            author_news = 0
        form = SearchForm(request.POST)
        employees = Employee.objects.filter(Q(username__contains=request.POST.get("search")) | Q(position_id=job_title) | Q(work_phone__contains=request.POST.get("search")) | Q(email__contains=request.POST.get("search"))| Q(birthday__contains=request.POST.get("search")))
        events = Event.objects.filter(Q(title__contains=request.POST.get("search")) | Q(description__contains=request.POST.get("search")) | Q(main_employee=author_news)| Q(date_since__contains=request.POST.get("search")))
        news = News.objects.filter(Q(title__contains=request.POST.get("search")) | Q(description__contains=request.POST.get("search")) | Q(date__contains=request.POST.get("search")))   
        context["employees"] = employees
        context["search_form"] = form
        context['events'] = events
        context['news'] = news
        for i in events:
            i.date_since = i.date_since.strftime("%d.%m.%Y")
        for i in news:
            i.date = i.date.strftime("%d.%m.%Y")
        for i in employees:
            i.birthday = i.birthday.strftime("%Y-%m-%d")
        return render(request, self.template_name, context)


    
