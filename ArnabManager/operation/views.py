from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')


def arnaba_list(request):
    arnaba_list = Arnaba.objects.all()
    context = {
        'arnaba_list': arnaba_list
    }
    return render(request, 'arnaba_list.html', context)

def detail(request, id):
        arnab = Arnab.objects.get(pk=id)
        context = {
            'arnab': arnab
        }
        return render(request, 'detail.html',context)



