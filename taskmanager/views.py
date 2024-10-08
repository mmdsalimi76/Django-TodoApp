from idlelib.iomenu import errors
from lib2to3.fixes.fix_input import context
from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import GoalForm,TaskForm,IdeaForm
from .models import Task,Goal,Idea
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def task_handler(request):
    if request.method=='POST':

        if request.POST['action']=='add':
            task=TaskForm(request.POST)

            if task.is_valid():
                task.save()
        elif request.POST['action']=='x':
            id=request.POST['id']
            delete_task=Task.objects.get(id=id)
            delete_task.delete()





    context={
        'goals':Goal.objects.filter(user=request.user),
        'tasks':Task.objects.filter(user=request.user)

    }



    return render(request,'./taskmanager/index.html',context)
@login_required
def goal_handler(request):
    if request.method=='POST':
        if request.POST['action']=='save':
            goal=GoalForm(request.POST)
            if goal.is_valid():
                goal.save()
        elif request.POST['action']=='x':
            id=request.POST['id']
            delete_goal=Goal.objects.get(id=id)
            delete_goal.delete()


    goals = Goal.objects.prefetch_related('tasks').filter(user=request.user)

    return render(request,'./taskmanager/goals.html',{'goals':goals})
@login_required
def idea_handler(request):
    if request.method=="POST":
        if request.POST['action']=='add':
            idea=IdeaForm(request.POST)

            if idea.is_valid():
                idea.save()
        elif request.POST['action']=='x':
            id=request.POST['id']
            delete_idea=Idea.objects.get(id=id)
            delete_idea.delete()
    context={'ideas':Idea.objects.filter(user=request.user)}
    return render(request,'./taskmanager/ideas.html',context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,form.errors)


    form = CustomUserCreationForm()

    return render(request, './taskmanager/register.html',{'form':form})

def _login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)

        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,form.errors)
    form=AuthenticationForm()

    return render(request,'./taskmanager/login.html',{'form':form})

def _logout(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')




