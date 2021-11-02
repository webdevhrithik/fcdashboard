from django.shortcuts import render
from .models import *

def home(request):
    posts = Post.objects.all()
    context = {'posts': 'posts'}
    return render(request, 'dash/dash.html', context)

def charts(request):
    context = {}
    return render(request, 'dash/charts.html', context)

def learning(request):
    context = {}
    return render(request, 'dash/learning.html', context)