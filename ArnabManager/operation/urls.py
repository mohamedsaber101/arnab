from django.urls import path
from . import views
app_name = 'operation'
urlpatterns = [
    path('', views.index, name='index'),
    path('arnaba_create', views.arnaba_create, name='arnaba_create'),
    path('arnab_create', views.arnab_create, name='arnab_create'),
    path('arnaba_list', views.arnaba_list, name='arnaba_list'),
    path('arnab_list', views.arnab_list, name='arnab_list'),
    path('update/<int:id>/', views.arnaba_update, name='arnaba_update'),
    path('delete/<int:id>/', views.arnaba_delete, name='arnaba_delete'),
    path('<int:id>/', views.detail, name='detail')


]