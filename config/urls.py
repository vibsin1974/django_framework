from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.hello_world, name="hello_world"),
    # path("hello_json/",views.hello_world_json, name="hello_json")
    path("list/", include("todo.urls"))
]
