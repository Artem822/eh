from django.contrib.syndication.views import Feed  
from django.template.defaultfilters import truncatewords  
from models.models import News 
from django.urls import reverse
import requests
class NewsFeed(Feed):  
    title = 'News'  
    link = ''  

    def items(self):  
        return News.objects.all()
        
    def item_title(self, item):  
        return item.title  
    

    def item_description(self, item):
        return item.description
    

