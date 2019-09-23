from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm, ScheduleForm
from .models import Register, Schedule
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
                messages.error(request, 'The password in incorrect')
                form = LoginForm()
                return render(request, 'todo/login.html', {'form': form})
        else:
            messages.error(request, "Don't register the mail-addresws")
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
            messages.error(request, 'Already the name exists')
            form = RegisterForm()
            return render(request, 'todo/register.html', {'form': form})
        elif Register.objects.filter(mail_address=str(add)).exists():
            messages.error(request, 'Already the mail-address exists')
            form = RegisterForm()
            return render(request, 'todo/register.html', {'form': form})
        else:
            confirm(name=user, address=add, password=password)
            return render(request, 'todo/mypage.html', {'name': user})
    else:
        form = RegisterForm()
        return render(request, 'todo/register.html', {'form': form})

def home(request):
    return render(request, 'todo/firstpage.html', {})

def confirm(name, address, password):
    register = Register(user_name=str(name), mail_address=str(address), password=str(password))
    register.save()

def mypage(request, username):
    account = Register.objects.get(user_name=str(username))
    name = account.user_name
    add = account.mail_address
    password = account.password
    return render(request, 'todo/mypage.html', {'name': name})

def myschedule(request, username):
    if request.method == 'POST':
        username = username
        year = request.POST.get('year')
        month = request.POST.get('month')
        date = request.POST.get('date')
        action = request.POST.get('action')
        schedule_register(username, year, month, date, action)
        return redirect('home')

    else:
        form = ScheduleForm()
        return render(request, 'todo/schedule_register.html', {'form': form, 'name': username})

def schedule_register(username, year, month, date, action):
    schedule = Schedule(user_name=username, year=year, month=month, date=date, action=action)
    schedule.save()
        
def schedule_check(request, username):
    account = Schedule.objects.filter(user_name=username).order_by('year', 'month', 'date')
    return render(request, 'todo/schedule_check.html', {'lists': account, 'name': username})

