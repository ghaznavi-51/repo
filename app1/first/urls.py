from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data, name='data'),
    path('datatable/', views.datatable, name='datatable'),
    path('saveData/', views.saveData, name='saveData')
]