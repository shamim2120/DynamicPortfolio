from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
                messages.info(request, 'Passwords do not match.')
                return redirect('/auth/signup/')
        try:
             if User.objects.get(username=email):
                  messages.warning(request, 'Email is taken')
                  return redirect('/auth/signup/')
        except Exception as identifier:
             pass
        myuser = User.objects.create_user(name,email,email,pass1)
        myuser.save()
        messages.success(request, 'User is created please login')
        return redirect('/auth/login/')     
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'login.html')