from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bookmark_list(request):
    return HttpResponse('<h1>북마크리소스페이지</h1>')
