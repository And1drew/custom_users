from django.shortcuts import render
from django.urls import reverse
from My_User.models import custom_user
from My_User.forms import signup_form, login_form
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


@login_required
def index(request):
    custom_user_model = "My_User.custom_user"
    return render(request, 'index.html', {"user_model": custom_user_model})


def login_view(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            user = authenticate(request, username=form.get('username'), password=form.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = login_form
    return render(request, 'generic_form.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_user = custom_user.objects.create_user(username=form.get('username'), password=form.get('password'), displayname=form.get('displayname'), age=form.get('age'))
            return HttpResponseRedirect('/')
    form = signup_form()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginpage'))