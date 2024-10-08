from django import forms
from .models import Task,Goal,Idea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','due_date','goal','user']

class GoalForm(forms.ModelForm):
    class Meta:
        model=Goal
        fields=['name','description','category','end_date','user']

class IdeaForm(forms.ModelForm):
    class Meta:
        model=Idea
        fields=['idea','user']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

