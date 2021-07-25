from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
import requests
from . import models

BASE_CRAIGSLIST_URL = 'https://olist.ng/filter?keyword={}'

# Create your views here.


def home(request):
    return render(request,'my_app/base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    
    response = requests.get(final_url)
    data = response.text
 
    soup = BeautifulSoup(data,features='html.parser')
    post_listings = soup.find_all('a', {'class':'item'} )

    final_postings = []
    for post in post_listings :
        post_title = post.find(class_='title').text
        post_url = post.get('href')
        post_price = post.find(class_='price').text
        post_img = post.find('img').get('src')
        final_postings.append((post_title,post_url,post_price,post_img))

    

    context = {'search':search, 'postings':final_postings}
    return render(request,'my_app/new_search.html',context)