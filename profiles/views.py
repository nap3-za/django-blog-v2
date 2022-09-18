from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import RegForm, LoginForm
from django.contrib.auth import login, authenticate

userm = get_user_model()
# Create your views here.

def RegView(request, *args, **kwargs):
    form  = RegForm(request.POST or None)

    if form.is_valid() and form != None:

        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = User.objects.create_user(username, email, password=None)
        user.save()
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect("http://127.0.0.1:8000/")


    context = {}
    return render(request, "profiles/html/reg.html", context)

def LoginView(request):
    form = LoginForm(request.POST or None)
    if form.is_valid() and form != None:
        username = form.cleaned_data.get("username")
        password = form.data.get("password")
        user = authenticate(request, username=username, password=password)
        user_obj = User.objects.get(username=username)
        login(request, user_obj)
        return redirect('http://127.0.0.1:8000/')

    context = {}
    return render(request, "profiles/html/login.html", context)
        



