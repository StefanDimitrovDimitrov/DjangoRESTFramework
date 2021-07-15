from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Pythons.python_core.decorators import group_required
from .forms import PythonCreateForm, FilterForm
from .models import Python


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }


# Create your views here.
# @login_required(login_url='login user')
def index(req):
    params = extract_filter_values(req.GET)
    order_by = 'name' if params['order'] == FilterForm.ORDER_ASC else '-name'
    pythons = Python.objects.filter(name__icontains=params['text']).order_by(order_by)

    context = {
        'pythons': pythons,
        'filter_form': FilterForm(initial=params),
    }

    return render(req, 'index.html', context)


# @group_required(groups=['User_Group'])
# @login_required
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        data = request.POST
        files = request.FILES
        form = PythonCreateForm(data, files)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'create.html', context)