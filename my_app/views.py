from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.


def home(request):
    return render(request,'my_app/base.html')


def new_search(request):
    search = request.POST.get('search')
    context = {'search':search}
    return render(request,'my_app/new_search.html',context)