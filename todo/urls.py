from django.urls import path
from todo import views
urlpatterns = [
    path("list/", views.todo_list),
    path("detail/<int:id>/", views.todo_detail),
    path("detail/<str:name>/", views.todo_detail_name),
]
