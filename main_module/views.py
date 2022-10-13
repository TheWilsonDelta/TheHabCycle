from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import ToDoList, Category, Progress


@login_required
def create(request):
    todos = ToDoList.objects.filter(user=request.user)
    categories = Category.objects.all()

    if request.method == "POST":

        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            Todo = ToDoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category),
                            user=request.user, progress=Progress.objects.get(elevation="on_hold"))
            Todo.save()
            return HttpResponseRedirect(request.path_info)

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = ToDoList.objects.get(id=int(todo_id))
                todo.delete()

    return render(request, "main_module/create.html", {"todos": todos, "categories": categories})


@login_required
def home(response):
    context = {
        'on_hold': ToDoList.objects.filter(user=response.user, progress__elevation="on_hold"),
        'in_progress': ToDoList.objects.filter(user=response.user, progress__elevation="in_progress"),
        'done': ToDoList.objects.filter(user=response.user, progress__elevation="done"),
        'archived': ToDoList.objects.filter(user=response.user, progress__elevation="archived")
    }

    return render(response, "main_module/home.html", context=context)


@staff_member_required
def staff(response):
    return render(response, "main_module/staff_list.html", {})


@login_required
def invite(response):
    return render(response, "main_module/manager_invite.html", {})


def logout_now(request):
    logout(request)
    return render(request, "registration/logout.html", {})
