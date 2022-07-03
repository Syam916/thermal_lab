from django.db import models

# Create your models here.
class Compressor(models.Model):
    p22=models.CharField(max_length=10)
    x1=models.CharField(max_length=10)
    t1=models.CharField(max_length=10)
    
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
    L1=models.CharField(max_length=10)
    X1=models.CharField(max_length=10)
    T1=models.CharField(max_length=10)
    
    
    
