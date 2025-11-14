"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from http.client import HTTPResponse

import contex
import render
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from pip._internal.cli.cmdoptions import python

movie_list =[
    {'title': '좀비딸','genre':'판타지'},
    {'title': '귀칼','genre':'애니'},
    {'title': 'F1더무비','genre':'스릴'},
    {'title': '미/임:파이널레코딩','genre':'첩보'},
    {'title': '야당','genre':'현실?'},
]
def index(request):
    return HTTPResponse('Hello')

def book_list(request):
    book_text=''
    for i in range(0, 10):
        book_text += f'book {i},br>'

    return HttpResponse(book_text)

def book(request, num):
    book_text=f"book {num}번 페잊입니다."
    return HttpResponse(book_text)

def language(request, lang):
    return HttpResponse(f'<h1>{lang}언어페이지')
def gugu(request, dan, contex=None):
    context={
        'dan':dan,
        'results': [dan* i for i in range(1, 10)],
    }
    return render(request,'gugu.html', contex)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path ('book list/', book_list),
    path('book_list/<int:num>/', book),
    path( 'language/python/', python),
    path( 'Language/<str: lang>/', language),
    path('movie/', movies),
    path('movie/<int:num>/',movie_detail),
    path('movie/<int:num>',gugu),
],
#이전실습
'/'


# noinspection PyUnreachableCode
def movie_detail(request, index):
    if index > len(movie_list)-1:
        #from django.http import  Http404
        raise Http404

    #movie=moveie_list[index]

    return render(request,template_name:'movie.html', {'movie':moie:movie}


def movies(request):
    #movie_titles=[movie['title'] for movie in movie_list]
    #response_text=',<br>'.join(movie_titles)
    #return HttpResponse(response_text)
    return render(request, 'movies.html',context,{'movie_list': movie_list}




