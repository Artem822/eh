from django.urls import path, include
from .views import Main
from .feeds import NewsFeed
urlpatterns = [
    path('', Main.as_view()),
    path('swagger/', NewsFeed()),

]