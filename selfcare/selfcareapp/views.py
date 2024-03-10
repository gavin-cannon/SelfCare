from django.shortcuts import render, HttpResponse
from .models import SelfCareItem
from .forms import SelfCareItemForm
import logging

# Create your views here.
logger = logging.getLogger(__name__)

def home(request):
    return render(request, "home.html")

def taskList(request):
    items = SelfCareItem.objects.all()
    return render(request, "task-list.html", {"tasks": items})

def createTask(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        task = SelfCareItem(title=title, description=description, completed = False)
        task.save()
        return render(request, 'home.html')
    else:
        return render(request, "create.html")

def create_self_care_item(request):
    print(request)
    print("HELLO")
    logger.info("Hello")
    if request.method == 'POST':
      title = request.POST.get("title")
      description = request.POST.get("description")
      task = SelfCareItem(title=title, description=description, completed = False)
      task.save()
    return render(request, 'home.html')