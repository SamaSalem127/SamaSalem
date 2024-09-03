from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Subject, Section
from .forms import SubjectForm, SectionForm,SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'main/home.html')

def detailed_subject(request, id):
    subject = get_object_or_404(Subject, id=id)
    context = {'subject': subject}
    return render(request, 'main/detailed.html', context)

def todo_by_status(request, st):
    todos = Subject.objects.filter(status=st)
    context = {'todos': todos}
    return render(request, 'main/todosstatus.html', context)

def todo_list_section(request, id):
    todos = Subject.objects.filter(section=id)
    sections = Section.objects.all()
    context = {"subjects": todos, 'sections': sections}
    return render(request, 'main/index.html', context)

def create_todo(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubjectForm()
    return render(request, 'main/create_todo.html', {'form': form})

def create_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SectionForm()
    return render(request, 'main/createSections.html', {'form': form})

def update_subject(request, id):
    subject = get_object_or_404(Subject, id=id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'main/updatesubject.html', {'form': form})

def delete_subject(request, id):
    subject = get_object_or_404(Subject, id=id)
    subject.delete()
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid credentials'})
    return render(request, 'main/login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')

def dashboard(request):
    subjects = Subject.objects.all().order_by('due_date')
    sections = Section.objects.all()
    context = {'subjects': subjects, 'sections': sections}
    return render(request, 'main/index.html', context)
