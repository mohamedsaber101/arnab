from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from operation.forms import *
from django.core import serializers
# Create your views here.
### GLOBAL vars
disabled_fields = ['id', 'age', 'image']

state_after_talqeeh = [
        {'current': 'fadya', 'next': 'Metlaqa7a'},
        {'current': '7amel', 'next':'7amel'},
        {'current': 'Metlaqa7a', 'next':'Metlaqa7a'},
        {'current': 'Morde3a', 'next':'Metlaqa7a w Morde3a'},
        {'current': '7amel w Morde3a', 'next':'7amel w Morde3a'},
        {'current': 'Metlaqa7a w Morde3a', 'next':'Metlaqa7a w Morde3a'} ]





#####################################

def index(request):
    arnaba_count = Arnaba.objects.all().count()
    arnab_count = Arnab.objects.all().count()
    context = {
         'arnaba_count': arnaba_count,
         'arnab_count': arnab_count
    }
    return render(request, 'index.html', context)


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
        todays_year = str(datetime.date.today()).split ('-')[0]
        todays_month = str(datetime.date.today()).split ('-')[1]
        todays_day = str(datetime.date.today()).split ('-')[2]
        todays_date = todays_year + '-' + todays_month + '-' + todays_day

        for field in fields:
              foreign = False
              field_name = field.name
              field_value = getattr(arnab, field.name)
              field_type = arnab._meta.get_field(field.name).__class__.description
              if 'Foreign Key' in str(field_type):
                  foreign = True
                  arnab_list = Arnab.objects.all()
              elif field_name == 'talqeeh_datestamp':
                   field_value = getattr(arnab, 'talqeeh_datestamp').strftime("%Y-%m-%d")
              self_field_list = {'name': field_name, 'value': field_value, 'type': field_type, 'foreign': foreign }
              field_list.append(self_field_list)
              
        print (field_list)
        context = {
            'arnab': arnab,
            'fields': fields,
            'field_list': field_list,
            'disabled_fields': disabled_fields,
            'arnab_list': arnab_list,
            'todays_date': todays_date,
            'state_after_talqeeh': state_after_talqeeh

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
    print (len(request.POST))
    print (request.POST)

    print (id)
    arnaba = Arnaba.objects.get(pk=id)
    fields = arnaba._meta.get_fields()
    
    if len(request.POST) == 3 and 'talqeeh_zakar' in str(request.POST) and 'talqeeh_datestamp' in str(request.POST):
        arnab = Arnab.objects.get(name=request.POST['talqeeh_zakar'])
        setattr(arnaba, 'talqeeh_zakar', arnab)
        day = int(str(request.POST['talqeeh_datestamp']).split('-')[2])
        month = int(str(request.POST['talqeeh_datestamp']).split('-')[1])
        year = int(str(request.POST['talqeeh_datestamp']).split('-')[0])
        formatted_date = datetime.date(year, month, day)
        setattr(arnaba, 'talqeeh_datestamp', formatted_date)
        for state in state_after_talqeeh:
            if state['current'] == arnaba.state:
                setattr(arnaba, 'state', state['next'] )

    else:
        field_list = []
        for field in fields:
            field_type = arnaba._meta.get_field(field.name).__class__.description
            print (str(field_type))
            if field.name not in disabled_fields:

                if 'talqeeh_zakar' == str(field.name):
                    arnab = Arnab.objects.get(name=request.POST[field.name])
                    setattr(arnaba, 'talqeeh_zakar', arnab)
                elif 'talqeeh_datestamp' == str(field.name):
                    day = int(str(request.POST[field.name]).split('-')[2])
                    month = int(str(request.POST[field.name]).split('-')[1])
                    year = int(str(request.POST[field.name]).split('-')[0])
                    formatted_date = datetime.date(year, month, day)
                    setattr(arnaba, 'talqeeh_datestamp', formatted_date)
                else: 
                    setattr(arnaba, field.name, request.POST[field.name])
                    
                    
                 
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
        if 'Rel:' in str(field):
            pass
        elif field.name not in disabled_fields:
            setattr(arnab, field.name, request.POST[field.name])
    arnab.save()
    alert="تم تحــــــديث بيانات الارنـــــــــب "+ arnab.name 
    return arnab_list(request, alert)