from django.urls import path
from . import views



urlpatterns=[

    path('heat',views.heat,name='heat'),
    path('compd',views.compd, name='compd'),
    path('compexp',views.compexp, name='compexp'),
    path('blowexp',views.blowexp, name='blowexp'),
    path('morseexp',views.morseexp, name='morseexp'),
    path('result',views.result, name='result'),
    path('index',views.index, name='index'),
    path('compressor',views.compressor, name ='compressor'),
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('bhp3',views.bhp3,name='bhp3'),
    path('heatexp',views.heatexp, name='heatexp'),
    path('morse1',views.morse1,name='morse1'),
    path('heatresult',views.heatresult, name='heatresult'),
    path('morseresult',views.morseresult, name='morseresult'),
    path('bhp3exp',views.bhp3exp,name='bhp3exp'),
    path('bhp3result',views.bhp3result, name='bhp3result'),
    path('blowresult',views.blowresult, name='blowresult'),
    path('blower',views.blower, name='blower'),
    path('contact',views.contact, name='contact')

]
