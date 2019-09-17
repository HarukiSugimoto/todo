from django.shortcuts import render
from .forms import LoginForm, RegisterForm

# Create your views here.
def login(request):
    if request.method == "POST":
        add = request.POST.get('mail_address')
        password = request.POST.get('password')
        return render(request, 'todo/login.html', {'address': add, 'pass': password})
    else:
        form = LoginForm()
        return render(request, 'todo/login.html', {'form': form})

def register(request):
    if request.method == "POST":
        user = request.POST.get('user_name')
        add = request.POST.get('mail_address')
        password = request.POST.get('password')
        return render(request, 'todo/login.html', {'user': user, 'address': add, 'pass': password})
    else:
        form = RegisterForm()
        return render(request, 'todo/register.html', {'form': form})

def home(request):
    return render(request, 'todo/base.html', {})