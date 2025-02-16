from django.shortcuts import render
from .forms import TodoInputForm
from .models import TodoListModel


# Create your views here.


def index_view(request):
    form = TodoInputForm()

    if request.method == 'POST':
        form = TodoInputForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data["task"]

            TodoListModel.objects.create(task=data)

    todo_list = TodoListModel.objects.all()

    return render(request, 'todoApp/index.html', {"form": form, "todo_list": todo_list})
