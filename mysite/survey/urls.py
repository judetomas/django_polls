from django.urls import path

from . import views

app_name = 'survey'

urlpatterns = [
    path('', views.index, name='index'), 
    path('process', views.process, name='process'),
    path('<int:result_id>/results', views.results, name = 'results'),
]