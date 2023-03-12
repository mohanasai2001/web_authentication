from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from authapp.forms import signup
# Create your views here.
def home(request):
    return render(request, 'authapp/home.html')
@login_required
def java(request):
    return render(request, 'authapp/java.html')
@login_required
def python(request):
    return render(request, 'authapp/python.html')
#def signup(request):
    #return render(request, 'authapp/signup.html')
def login(request):
    return render(request, 'authapp/login.html')
def logout(request):
    return render(request, 'authapp/logout.html')
def signupForm(request):
    form = signup()
    if request.method=='POST':
        form = signup(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'authapp/signup.html',{'form': form})
def logout(request):
    return render(request, 'authapp/logout.html')
