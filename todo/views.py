from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

def index(request):
    search_query = request.GET.get('q')  # Get the search query from the GET request
    if search_query:
        item_list = Todo.objects.filter(title__icontains=search_query).order_by("-date")
    else:
        item_list = Todo.objects.order_by("-date")
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')

    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
