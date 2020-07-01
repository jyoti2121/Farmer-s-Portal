from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('rainfall_predict',views.rainfall_predict,name='rainfall_predict'),
    path('labour',views.labour,name='labour'),
    path('tasks',views.tasks,name='tasks'),
    path('production_predict',views.production_predict,name='production_predict'),
    path('add_tasks',views.add_tasks,name='add_tasks'),
    path('add_labour',views.add_labour,name='add_labour')
]