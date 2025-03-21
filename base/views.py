from django.shortcuts import render,redirect
from .models import User,Task,TaskActivity
from .forms import TaskForm, UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .forms import UserForm

# import Q for search
from django.db.models import Q #for search

@login_required(login_url="login")
def home(request):
    tasks = Task.objects.filter(user=request.user)  # Filter tasks for the logged-in user
    activities = TaskActivity.objects.filter(user=request.user).order_by('-timestamp')[:5]  # Get the latest 5 activities
    
    # Handle search query
    search_query = request.GET.get('q')
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) |  # Search by title
            Q(description__icontains=search_query) |  # Search by description
            Q(priority__icontains=search_query) |  # Search by priority
            Q(due_date__icontains=search_query)  # Search by due date
        )
    
    # Calculate statistics
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = total_tasks - completed_tasks
    
    # Calculate "Next Up" tasks (due in the next 24 hours)
    now = timezone.now()
    next_24_hours = now + timedelta(hours=24)
    next_up_tasks = tasks.filter(due_date__range=[now, next_24_hours], completed=False).count()
    
    # Calculate "Overdue" tasks
    overdue_tasks = tasks.filter(due_date__lt=now, completed=False).count()
    
    context = {
        "tasks": tasks,
        "activities": activities,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "next_up_tasks": next_up_tasks,
        "overdue_tasks": overdue_tasks,
        "search_query": search_query,  # Pass the search query to the template
    }
    return render(request, 'base/index.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the task to the logged-in user
            task.save()
            
            # Log the activity
            TaskActivity.objects.create(
                user=request.user,
                task=task,
                action="Created"
            )
            
            return redirect('home')
    else:
        form = TaskForm(initial={'user': request.user})  # Pre-fill the 'user' field
    
    context = {"form": form}
    return render(request, 'base/create_task.html', context)

def delete_task(request,pk):
    task = Task.objects.get(id=pk)
    context = {"task":task}
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request,'base/delete_task.html',context)

def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            
            # Log the activity
            TaskActivity.objects.create(
                user=request.user,
                task=task,
                action="Updated"
            )
            
            return redirect('home')
    context = {"form": form}
    return render(request, 'base/create_task.html', context)


#login page
def user_login(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email') 
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, 'base/login_register.html', {'page': page})

        user = authenticate(request, email=email, password=password)  
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'base/login_register.html', {'page': page})

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
            messages.error(request,'An error occurred')
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
    return render(request, 'base/edit_profile.html', {'form': form})

def mark_task_complete(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    if request.method == 'POST':
        # Mark the task as complete
        task.completed = True
        task.save()
        
        # Log the activity in TaskActivity
        TaskActivity.objects.create(
            user=request.user,
            task=task,
            action="Completed"
        )
        
        # Redirect back to the home page
        return redirect('home')
    
    # If it's not a POST request, redirect to home
    return redirect('home')