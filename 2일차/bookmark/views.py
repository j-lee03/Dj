from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def bookmark_list(request):
    return render(request, template_name='bookmark_list.html')