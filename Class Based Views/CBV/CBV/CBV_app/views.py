

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from CBV.CBV_app.models import CBVViews


class CBVList(ListView):
    model = CBVViews
    template_name = 'cbv_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Details(DetailView):
    pass
