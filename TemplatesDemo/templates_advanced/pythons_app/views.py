from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pythons_core.decorators import group_required
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
# @login_required(login_url='login user')
def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


@group_required(groups=['User_Group'])
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        data = req.POST
        files = req.FILES
        form = PythonCreateForm(data, files)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
