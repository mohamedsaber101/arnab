from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from operation.forms import *
from django.core import serializers
# Create your views here.
### GLOBAL vars
disabled_fields = ['id', 'age', 'image']


def index(request):
    return render(request, 'index.html')


def arnaba_list(request, alert='nothing'):
    arnaba_list = Arnaba.objects.all()
    context = {
        'arnaba_list': arnaba_list,
        'alert': alert
    }
    return render(request, 'arnaba_list.html', context)

def arnab_list(request, alert='nothing'):
    arnab_list = Arnab.objects.all()
    context = {
        'arnab_list': arnab_list,
        'alert': alert
    }
    return render(request, 'arnab_list.html', context)

#### DETAIL
def detail(request, id):
        arnab = Arnaba.objects.get(pk=id)
        fields = arnab._meta.get_fields()
        field_list = []
        arnab_list = []
        for field in fields:
              foreign = False
              field_name = field.name
              field_value = getattr(arnab, field.name)
              field_type = arnab._meta.get_field(field.name).__class__.description
              if 'Foreign Key' in str(field_type):
                  foreign = True
                  arnab_list = Arnab.objects.all()
              self_field_list = {'name': field_name, 'value': field_value, 'type': field_type, 'foreign': foreign }
              field_list.append(self_field_list)
              
        print (field_list)
        context = {
            'arnab': arnab,
            'fields': fields,
            'field_list': field_list,
            'disabled_fields': disabled_fields,
            'arnab_list': arnab_list

        }
        return render(request, 'detail.html',context)

def arnab_detail(request, id):
        arnab = Arnab.objects.get(pk=id)
        fields = arnab._meta.get_fields()
        field_list = []
        print (arnab)
        print (fields)
        for field in fields:
              if 'Rel:' in str(field):
                   pass
              else:
                field_name = field.name
                field_value = getattr(arnab, field.name)
                field_type = arnab._meta.get_field(field.name).__class__.description
                self_field_list = {'name': field_name, 'value': field_value, 'type': field_type }
                field_list.append(self_field_list)
              

        context = {
            'arnab': arnab,
            'fields': fields,
            'field_list': field_list,
            'disabled_fields': disabled_fields

        }
        return render(request, 'arnab_detail.html',context)

## DELETE

def arnaba_delete(request, id):
        arnab = Arnaba.objects.get(pk=id)
        alert="تم حـــــذف الأرنبـــــــــــــة " + arnab.name
        arnab.delete()
        return arnaba_list(request, alert)

## DELETE

def arnab_delete(request, id):
        arnab = Arnab.objects.get(pk=id)
        alert="تم حـــــذف الأرنــــــــــــــب " + arnab.name
        arnab.delete()
        return arnab_list(request, alert)

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
    

def arnab_create(request):
    form = NewArnabForm()

    if request.method == "POST":
        form = NewArnabForm(request.POST)

        if form.is_valid():
               form.save(commit=True)
               return arnab_list(request)
        else:
               print('ERROR INVALID')
    context = {
            'form': form
        }
    return render(request, 'arnaba_create.html', context)


##### ARNABA UPDATE
def arnaba_update(request, id):
    print (request.POST)
    print ("=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-")
    print ("=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-")

    print ("=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-")
    print ("=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-")
    print ("=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-")

    print (id)
    arnaba = Arnaba.objects.get(pk=id)
    fields = arnaba._meta.get_fields()
    

    field_list = []
    for field in fields:
        field_type = arnaba._meta.get_field(field.name).__class__.description
        print (str(field_type))
        if field.name not in disabled_fields:
            if 'Foreign Key' not in str(field_type):
                 setattr(arnaba, field.name, request.POST[field.name])
            else:
                 arnab = Arnab.objects.get(name=request.POST[field.name])
                 setattr(arnaba, field.name, arnab)
                 
                 
                 
    arnaba.save()
    alert="تم تحــــــديث بيانات الارنبـــــــة "+ arnaba.name 
    return arnaba_list(request, alert)


def arnab_update(request, id):
    print (request.POST)
    print (id)
    arnab = Arnab.objects.get(pk=id)
    fields = arnab._meta.get_fields()
    field_list = []
    for field in fields:
        if field.name not in disabled_fields:
            setattr(arnab, field.name, request.POST[field.name])
    arnab.save()
    alert="تم تحــــــديث بيانات الارنـــــــــب "+ arnab.name 
    return arnab_list(request, alert)