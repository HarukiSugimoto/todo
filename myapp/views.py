from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm
from .models import Register
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        add = request.POST.get('mail_address')
        password = request.POST.get('password')
        if Register.objects.filter(mail_address=str(add)).exists():
            login = Register.objects.get(mail_address=str(add))
            login_password = login.password
            name = str(login.user_name)
            if str(login_password) == str(password):
                return redirect('mypage', username=name)
            else:
                messages.error(request, 'パスワードが違います。')
                form = LoginForm()
                return render(request, 'todo/login.html', {'form': form})
        else:
            messages.error(request, '　そのメールアドレスは登録されていません。')
            form = LoginForm()
            return render(request, 'todo/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'todo/login.html', {'form': form})

def register(request):
    if request.method == "POST":
        user = request.POST.get('user_name')
        add = request.POST.get('mail_address')
        password = request.POST.get('password')
        if Register.objects.filter(user_name=str(user)).exists():
            messages.error(request, 'すでに使われている名前です。')
            form = RegisterForm()
            return render(request, 'todo/register.html', {'form': form})
        elif Register.objects.filter(mail_address=str(add)).exists():
            messages.error(request, 'すでに登録されているメールアドレスです。')
            form = RegisterForm()
            return render(request, 'todo/register.html', {'form': form})
        else:
            confirm(name=user, address=add, password=password)
            return render(request, 'todo/base.html', {})
    else:
        form = RegisterForm()
        return render(request, 'todo/register.html', {'form': form})

def home(request):
    return render(request, 'todo/base.html', {})

def confirm(name, address, password):
    register = Register(user_name=str(name), mail_address=str(address), password=str(password))
    register.save()

def mypage(request, username):
    account = Register.objects.get(user_name=str(username))
    name = account.user_name
    add = account.mail_address
    password = account.password
    return render(request, 'todo/mypage.html', {'name': name, 'add': add, 'pass': password})
