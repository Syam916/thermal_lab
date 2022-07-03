from django.urls import path
from . import views



urlpatterns=[
    path('compexp',views.compexp, name='comp.exp'),
    path('result',views.result, name='result'),
    path('index',views.index, name='index'),
    path('compressor',views.compressor, name ='compressor'),
    path('',views.home, name='home')
]
