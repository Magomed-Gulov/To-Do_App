from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoListItem
from django.contrib.auth import authenticate, login, logout



def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todoapp/todolist.html',
    {'all_items':all_todo_items})

def addTodoView(request, email):
    content = str( request.POST['content'] ).strip()
    # email   = str( request.POST['email'] )
    if content != "":
        new_item = TodoListItem( content = content, email=email )
        new_item.save(  )
    return HttpResponseRedirect( '/todoapp/' )

def actionTodoView(request, te, i):
    y = TodoListItem.objects.get(id=i)

    if   te == 'status':
        y.status = not y.status
        y.save_base(  )
    elif te == 'delete':
        y.delete(  )
    return HttpResponseRedirect( '/todoapp/' )