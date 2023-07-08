from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from operation.forms import *
from django.core import serializers
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
        arnab = Arnaba.objects.get(pk=id)
        fields = arnab._meta.get_fields()
        field_list = []
        for field in fields:
              field_name = field.name
              field_value = arnab._meta.get_field(field.name).value_from_object(arnab)
              slef_field_list = {'name': field_name, 'value': field_value}
              field_list.append(slef_field_list)


        context = {
            'arnab': arnab,
            'fields': fields,
            'field_list': field_list

        }
        return render(request, 'detail.html',context)


## DELETE

def arnaba_delete(request, id):
        arnab = Arnaba.objects.get(pk=id)
        arnab.delete()
        return arnaba_list(request)

###### FORMS
def arnaba_create(request):
    form = NewArnabaForm()

    if request.method == "POST":
        form = NewArnabaForm(request.POST)

        if form.is_valid():
               form.save(commit=True)
               return arnaba_list(request)
        else:
               print('ERROR INVALID')
    context = {
            'form': form
        }
    return render(request, 'arnaba_create.html', context)
    