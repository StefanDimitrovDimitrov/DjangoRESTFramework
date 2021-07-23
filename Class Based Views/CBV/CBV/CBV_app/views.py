from pyexpat import model

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from CBV.CBV_app import models
from CBV.CBV_app.models import CBVViews


class CBVList(ListView):
    model = CBVViews
    template_name = 'cbv_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Details(DetailView):
    model = CBVViews
    template_name = 'detail_view.html'
    context_object_name = 'current_view'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Create(CreateView):
    fields = '__all__'
    model = models.CBVViews
    template_name = 'create_CBVView.html'
    success_url = reverse_lazy('CBVList')
