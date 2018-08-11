from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/regist.html')

def tra(request):
    return render(request, 'blog/trans.html')
