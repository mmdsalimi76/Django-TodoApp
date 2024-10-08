from django.urls import path
from . import views


app_name='taskmanager'
urlpatterns =[
    path('',views.task_handler,name='index'),
    path('Goals/',views.goal_handler,name='goals'),
    path('Ideas/',views.idea_handler,name='ideas'),
    path('Register/',views.register,name='register'),
    path('Login/',views._login,name='login'),
    path('Logout/',views._logout,name='logout'),
]