from django.urls import path
from . import views
app_name = 'operation'
urlpatterns = [
    path('', views.index, name='index'),
    path('arnaba_create', views.arnaba_create, name='arnaba_create'),
    path('arnaba_list', views.arnaba_list, name='arnaba_list'),
    path('<int:id>/', views.detail, name='detail'),


]