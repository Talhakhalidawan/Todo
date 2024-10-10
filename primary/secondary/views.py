from django.shortcuts import render , redirect
from django.http import JsonResponse
from .models import Todos

# Create your views here.

def home(request):
    data = Todos.objects.all().order_by("-time_created")
    if request.method == "POST":
        checked = request.POST.get("checked") == 'true'
        # checked = bool(checked)
        sno = request.POST.get("sno")
        print(f"Checked: {checked} , {sno}")
        todo = Todos.objects.get(sno = sno)
        todo.status = checked
        todo.save()
        return JsonResponse({"message": "Checkbox state received", "checked": checked})
    context = {
        "data" : data,
    }
    return render(request, "index.html" , context)

def create_todo(request):
    if request.method == "POST":
        desc = request.POST.get("desc")
        data = Todos.objects.create(desc = desc)
        data.save()
        print("saved")
        return redirect("/")
    print("here")
    context = {
        "data" : "create",
    }
    return render(request , "create-todo.html" , context)

def delete_todo(request , sno):
    todo = Todos.objects.get(sno = sno)
    todo.delete()
    return redirect("/")

def edit_todo(request , sno):
    todo = Todos.objects.get(sno = sno)
    if request.method == "POST":
        desc = request.POST.get("desc")
        todo.desc = desc
        todo.save()
        return redirect("/")
    context = {
        "data" : "edit",
        "todo" : todo,
    }
    return render(request , "create-todo.html" , context)

def view(request , sno):
    todo = Todos.objects.get(sno = sno)
    time = todo.formated_time
    context = {
        "data" : "view",
        "todo" : todo,
        "time" : time,
    }
    return render(request , "create-todo.html" , context)