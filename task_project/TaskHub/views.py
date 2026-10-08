from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from TaskHub.models import *


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        
        user_exist = UserModel.objects.filter(username = username).exists()
        if user_exist:
            messages.warning(request, 'User already exists.')
            return redirect('register_view')
        
        if password == conf_password:
            UserModel.objects.create_user(
                username = username,
                full_name = full_name,
                email = email,
                password= password,
            )
            messages.success(request, 'User created successfully')
            return redirect('login_page')
        else:
            messages.warning(request, 'Password doesnot match.')
            return redirect('register_view')

    return render(request, 'auth/register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, 'User login successfully')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid credentials.')
            return redirect('login_page')

    return render(request, 'auth/login.html')


@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required
def home(request):
    task_data = TaskModel.objects.all()

    context = {
        'task_data': task_data
    }
    return render(request, 'pages/home.html', context)


@login_required
def task_list(request):
    task_data = TaskModel.objects.filter(created_by = request.user)

    context ={
        'task_data':task_data
    }
    return render(request, 'pages/task_list.html',context)

@login_required
def task_detail(request, t_id):
    task = get_object_or_404(TaskModel, id=t_id)

    context = {
        'task': task
    }

    return render(request, 'pages/task_detail.html', context)


@login_required
def add_task(request):
    current_user = request.user
    
    if request.method == 'POST':
        title = request.POST.get ('title')
        description = request.POST.get ('description')
        status = request.POST.get ('status')
        deadline = request.POST.get ('deadline')

        TaskModel.objects.create(
            title = title,
            description = description,
            status = status,
            deadline = deadline,
            created_by = current_user
        )
        
        messages.success(request, 'Task added successfully.')
        return redirect('task_list')
    return render(request, 'pages/add_task.html')

@login_required
def edit_task(request, t_id):
    task = TaskModel.objects.get(id=t_id)
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        if deadline:
            task.deadline = deadline
        task.save()
        messages.success(request, 'Task updated successfully.')
        return redirect('task_list')

    context = {
        'task': task
    }
    return render(request, 'pages/edit_task.html', context)


@login_required
def delete_task(request, t_id):
    
    TaskModel.objects.get(id = t_id).delete()
    messages.success(request, 'Task deleted successfully.')
    
    return redirect('task_list')


