from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def bookmark_list(request):
    return render(request, template_mame='bookmark/bookmark_list.html')


def bookmark_detail(request, num):
    return render(request, template_mame='bookmark/bookmark_detail.html', context={'number':number})
