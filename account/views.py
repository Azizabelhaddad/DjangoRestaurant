from asyncio.windows_events import NULL
from .forms import RegisterForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

# Create your views here.

def ShowProfile(request, slug):
    profile = Profile.objects.filter(state=1, slug=slug)
    print(profile)

    return render(request, 'account/profiles.html', {'profile': profile})


def LogoutUser(request):
    logout(request)
    # messages.info(request, 'your are disconnected')
    return redirect('menu')

def LoginUser(request):
    user= NULL

    if request.user.is_authenticated:
        return redirect(request, 'menu')

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except :
            messages.warning(request, 'Username doesnt exist')
        # check authentication with ids
        authenticate(request, username=username, password=password)
        
        if user:
            # create session with login
            login(request, user)
            messages.success(request, 'User connected ')
            return redirect('menu')
        else:
            messages.warning(request,'Username or password incorrect')

            
    return render(request, 'account/login.html', {'user': user, 'page': 'login'})

def registerUser(request):
   form = RegisterForm()
   if request.method == "POST":
       form = RegisterForm(request.POST)
       print(form)
       if form.is_valid:
           user = form.save()
           messages.success(request, 'User created ')
           return redirect('menu')

   return render(request, 'account/login.html',  {'form': form, 'page': 'register'})