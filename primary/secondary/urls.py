from django.urls import path
from . import views 

urlpatterns = [
    path("" , views.home , name = "home"),
    path("create/" , views.create_todo , name = "create"),
    path("delete-todo/<int:sno>" , views.delete_todo , name = "delete-todo"),
    path("edit-todo/<int:sno>" , views.edit_todo , name = "edit-todo"),
    path("view/<int:sno>" , views.view , name = "view"),
]