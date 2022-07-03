from django.contrib import admin
from experiments.models import Compressor,Blower,Heatbalence,Bhpvilliers,Morse



admin.site.register(Compressor)
admin.site.register(Blower)
admin.site.register(Morse)
admin.site.register(Heatbalence)
admin.site.register(Bhpvilliers)



# Register your models here.
