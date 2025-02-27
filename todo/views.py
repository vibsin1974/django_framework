from django.shortcuts import render
from django.http import HttpResponse
from .models import todo
# Create your views here.

def todo_list(request):
    todos =  todo.objects.all()
    return render(request,"todo/todo.html",{"todos":todos})