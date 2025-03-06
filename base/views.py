from django.shortcuts import render,redirect
from .models import User,Task,TaskActivity
from .forms import TaskForm, UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    return render(request,'base/index.html',context)

def add_task(request):
    form = TaskForm()
    context = {"form":form}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'base/create_task.html',context)

def delete_task(request,pk):
    task = Task.objects.get(id=pk)
    context = {"task":task}
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request,'base/delete_task.html',context)

def edit_task(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    context = {"form":form}
    if request.method == 'POST': 
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'base/create_task.html',context)


#login page
def user_login(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        try:
            user = User.objects.get(username=username)
        except:
            user = messages.error(request,'User does not exist')
            
        if user:
            login(request,user)
            return redirect('home')
    return render(request,'base/login_register.html',{'page':page})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            messages.success(request,'User created successfully')
            return redirect('login')
        except:
            messages.error(request,'An error occured')
    return render(request,'base/login_register.html')

@login_required
def edit_profile_view(request):
    profile = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('home')
    else:
        form = UserForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})