from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # 추가
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login
from django.urls import reverse
# Create your views here.
def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())
        return redirect(reverse('blog_list')) # url을 찾는 reverse함수와 urls.py에 적은 name을 활용해 동적으로 작성

    else:
        form = AuthenticationForm(request)

    context = {
        'form': form
    }

    return render(request, 'registration/login.html', context)