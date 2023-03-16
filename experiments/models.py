from django.db import models

# Create your models here.
class Compressor(models.Model):
    Delivery_pressure_Guage=models.CharField(max_length=10)
    Delivery_pressure_Absolute=models.CharField(max_length=10)
    pressure_ratio=models.CharField(max_length=10)
    pressure_head_cm=models.CharField(max_length=10)
    pressure_head_m=models.CharField(max_length=10)
    time=models.CharField(max_length=10)
    volumetric_efficiency=models.CharField(max_length=10)
    power_input=models.CharField(max_length=10)
    Isothermal_power=models.CharField(max_length=10)
    Adiabatic_power=models.CharField(max_length=10)
    Isothermal_efficiancy=models.CharField(max_length=10)
    Adiabatic_efficiancy=models.CharField(max_length=10)
    Efficiancy_ratio=models.CharField(max_length=10)

    
class Blower(models.Model):
    s1=models.CharField(max_length=10)
    d1=models.CharField(max_length=10)
    T1=models.CharField(max_length=10)
    t81=models.CharField(max_length=10)
    
class Morse(models.Model):
    W=models.CharField(max_length=10)
    w11=models.CharField(max_length=10)
    w22=models.CharField(max_length=10)
    w33=models.CharField(max_length=10)
    w44=models.CharField(max_length=10)
    

    
    
class Heatbalence(models.Model):
    L1=models.CharField(max_length=10)
    X1=models.CharField(max_length=10)
    T11=models.CharField(max_length=10)
    T111=models.CharField(max_length=10)
    T22=models.CharField(max_length=10)
    Q1=models.CharField(max_length=10)
    T33=models.CharField(max_length=10)
    T44=models.CharField(max_length=10)
    
class Bhpvilliers(models.Model):
    Load=models.CharField(max_length=10)
    Manomertric_reading=models.CharField(max_length=10)
    Time=models.CharField(max_length=10)
'''Brake_power=models.CharField(max_length=10)
    fuel_consumption=models.CharField(max_length=10)
    Volumetric_efficiancy=models.CharField(max_length=10)
    Brake_torque=models.CharField(max_length=10)
    Thermal_efficiancy=models.CharField(max_length=10)'''
    
    
    
    
