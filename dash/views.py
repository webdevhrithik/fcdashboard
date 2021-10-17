from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'dash/dash.html', context)

def charts(request):
    context = {}
    return render(request, 'dash/charts.html', context)

def learning(request):
    context = {}
    return render(request, 'dash/learning.html', context)