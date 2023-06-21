from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import NewTaskModels
from rest_framework.response import Response
# Create your views here.

#tasks = []

#class NewTaskForm(forms.Form):
#    task = forms.CharField(label = "New Task")
#    priority = forms.IntegerField(label = "Priority", min_value=1, max_value=10)


def index(request):
    #if "tasks" not in request.session:
    forms = NewTaskModels.objects.all()
    request.session["text"] = []
    return render(request, "task/index.html", {
        "task": forms
})

def add(request):
    if request.method == "POST":
        #form = NewTaskForm(request.POST)
        #form = NewTaskModels(request.POST)
        remarks = request.POST.get("task")
        remarks2 = request.POST.get("number")
        print("str", remarks)
        forms = NewTaskModels.objects.create(
            task = remarks,
            priority = int(remarks2)
        )
        #return Response(dictionary)
        
        #if form.is_valid():
        #task = form.cleaned_data["task"]
        #request.session["tasks"] += [task]
        #return HttpResponseRedirect(reverse("tasks:index"))
        #else:
         #   return render(request, "task/add.html", {
          #      "form": form
           # })
    return render(request, "task/add.html", {
        #"form": NewTaskForm()
        "form": NewTaskModels()
    })
