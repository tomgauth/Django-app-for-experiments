from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
import datetime

# Create your views here.

def index(request):
    return HttpResponse("hello world, this is index view")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def list_blog_posts(request):
    blog_posts = BlogPost.objects.all()
    return HttpResponse(blog_posts)