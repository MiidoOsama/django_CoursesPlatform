from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from .forms import LoginForm , UserRegesterationForm

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username , password = password)
            if user:
                login(request,user)
                return redirect('index')

    else:
        form = LoginForm()

    context = {
        'form':form
    }
    return render (request , 'users/login.html' , context)



def user_logout(request):
    logout(request)
    return redirect('login')


def user_registeration(request):
    if request.method == 'POST':
        form = UserRegesterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.role = form.cleaned_data['role']
            user.save()
            login(request , user)
            return redirect('index')
    else:
        form = UserRegesterationForm()

    context = {
        'form': form
    }
    return render( request , 'users/register.html' , context)


