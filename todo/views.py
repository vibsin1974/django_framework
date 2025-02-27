from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import todo
import random
# Create your views here.
from django.views.generic import View, TemplateView

def hello_world(request):
    return render(request,"hello_world.html")

def hello_world_json(request):
    return JsonResponse({"message":"hello world"})


def todo_list(request):
    todos =  todo.objects.all()
    return render(request,"todo/todo.html",{"todos":todos})


def todo_detail(request, id):
    try :
        object = todo.objects.get(pk=id)
    except todo.DoesNotExist :
        return HttpResponse("없는 페이지 입니다")
    
    return render(request, "todo/detail.html", {"todo":object})

def todo_detail_name(request, name):
    object = todo.objects.filter(name__icontains=name).first()
    print(object)
    if object is None:
        return HttpResponse("페이지가 존재하지 않습니다")
    
    first = object.first()
    last = object.last()

    return render(request, "todo/detail.html", {"todo":object, "first":first,"last":last})



# class RandomNumber(View):
#     def get(self,request):
#         n = random.randint(1,100)
#         return render(request, "random.html", {"n":n})
    

    
# class RandomTemplate(TemplateView):
#     template_name = "random.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["n"] = random.randint(0,100)
        return context
