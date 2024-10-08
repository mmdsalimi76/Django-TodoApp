from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    due_date=models.DateTimeField(null=True,blank=True)
    goal=models.ForeignKey('Goal',on_delete=models.SET_NULL,null=True,blank=True ,related_name='tasks')
    reminder=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title
    def days_left(self):
        if self.due_date:
            DL = (self.due_date - timezone.now()).days
            if DL <= 0:
                return 'Over'
            else:
                return f'{DL} Days Left'

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CATEGORY_CHOICES=[('w','Work'),('hf','Health and Fitness'),('e','Education'),('p','Personal Development'),('h','Home and Family'),('s','Social'),('f','Finance'),('o','Other')]
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    category=models.TextField(choices=CATEGORY_CHOICES,blank=True,null=True)
    start_date=models.DateTimeField(default=timezone.now)
    end_date=models.DateTimeField(null=True,blank=True)


    def __str__(self):
        return self.name

    def days_left(self):
        if self.end_date:
            DL=(self.end_date - timezone.now()).days
            if DL<=0:
                return 'Over'
            else:
                return f'{DL} Days Left'
class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea=models.TextField()

    def __str__(self):
        return self.idea


