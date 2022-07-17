from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import *

# Create your views here.


def index(request):

    context = {
        'stocks': Stock.objects.all()
    }

    return render(request, 'stock/index.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'


class CreateStock(generic.CreateView):
    model = Stock
    fields = ['title', 'date', 'description', 'jumlah', 'harga']
    template_name = 'stock/createstock.html'
    success_url = reverse_lazy('index')


class DetailStock(generic.DetailView):
    model = Stock
    template_name = 'stock/detailstock.html'


class UpdateStock(generic.UpdateView):
    model = Stock
    template_name = 'stock/updatestock.html'
    fields = ['title', 'date', 'description', 'jumlah', 'harga']
    success_url = reverse_lazy('index')


class DeleteStock(generic.DeleteView):
    model = Stock
    template_name = 'stock/deletestock.html'
    success_url = reverse_lazy('index')
