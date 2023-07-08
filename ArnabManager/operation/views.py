from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from operation.forms import *
from django.core import serializers
# Create your views here.
### GLOBAL vars
disabled_fields = ['id', 'birth_date', 'image']


def index(request):
    return render(request, 'index.html')


def arnaba_list(request, alert='nothing'):
    arnaba_list = Arnaba.objects.all()
    context = {
        'arnaba_list': arnaba_list,
        'alert': alert
    }
    return render(request, 'arnaba_list.html', context)

def detail(request, id):
        arnab = Arnaba.objects.get(pk=id)
        fields = arnab._meta.get_fields()
        field_list = []
        for field in fields:
              field_name = field.name
              field_value = arnab._meta.get_field(field.name).value_from_object(arnab)
              field_type = arnab._meta.get_field(field.name).__class__.description
              self_field_list = {'name': field_name, 'value': field_value, 'type': field_type }
              field_list.append(self_field_list)
              

        context = {
            'arnab': arnab,
            'fields': fields,
            'field_list': field_list,
            'disabled_fields': disabled_fields

        }
        return render(request, 'detail.html',context)


## DELETE

def arnaba_delete(request, id):
        arnab = Arnaba.objects.get(pk=id)
        arnab.delete()
        return arnaba_list(request)

###### FORMS
### ARANABA CREATE
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
    


##### ARNABA UPDATE
def arnaba_update(request, id):
    print (request.POST)
    print (id)
    arnab = Arnaba.objects.get(pk=id)
    fields = arnab._meta.get_fields()
    field_list = []
    for field in fields:
        if field.name not in disabled_fields:
            setattr(arnab, field.name, request.POST[field.name])
    arnab.save()
    alert="تم تحــــــديث بيانات الارنبـــــــة "+ arnab.name 
    return arnaba_list(request, alert)