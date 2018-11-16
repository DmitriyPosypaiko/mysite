from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Category, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import Profile


def sign_up(request):
    get_form = UserCreationForm()
    if request.method == 'POST':
        post_form = UserCreationForm(request.POST)
        if post_form.is_valid():
            username = post_form.cleaned_data['username']
            password = post_form.cleaned_data['password1']
            new_user = User.objects.create_user(username=username, password=password)
            user=authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect('/')
    return render(request, 'registration.html',{'reg_form':get_form})


@login_required
def profile(request):
    user = request.user
    form = Profile(instance=user)
    print('test1')
    if request.method == 'POST':
        form = Profile(request.POST, instance=request.user)
        print('test2')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'index.html', {'form':form})


def products(request):
    context = {}
    context['category'] = Category.objects.all()
    context['product'] = Product.objects.all()

    return render(request, 'products.html', context)

def index(request):
    context = {}
    context['category'] = Category.objects.all()
    context['product'] = Product.objects.all()[:5]
    return render(request, 'index.html', context)
