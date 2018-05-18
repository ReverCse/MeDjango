from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LogInForm, SignUpForm
# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm({
            'username': request.POST['username'],
            'first_name': request.POST['first'],
            'last_name': request.POST['last'],
            'email' : request.POST['email'],
            'password': request.POST['password']
        })
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name']
                )
            user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request,user)
            return redirect('index')
        else: 
            return render(request,'forms/signup.html', {'form': form})
    return render(request, 'forms/signup.html')

def user_login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            user_or_email = form.cleaned_data['userID']
            password = form.cleaned_data['password']
            user = authenticate(request,username=user_or_email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LogInForm()

    return render(request, 'forms/login.html', {'form':form})

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return redirect('index')