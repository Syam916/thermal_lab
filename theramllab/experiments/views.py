from django.shortcuts import render
import math

# Create your views here.
def home(request):
    return render(request,'index.html')


def compressor(request):
    return render(request,'compressor.html')

def index(request):
    return render(request,'index.html')


def compexp(request):
    return render(request,'compexp.html')



def result(request):
    p22=int(request.POST['p2'])
    x1=float(request.POST['X'])
    t1=int(request.POST['t'])
    T=30
    p1=1.033
    p3 = p22+p1
     # PR is the pressure ratio
    PR= p3/p1
     # theorytical disacharge is Q
    Q = 0.0094333
     # A be the area of orifice 
    A = 0.000452
     # R be the density of air at room temperature
    R = (1.033*10**4)/(29.27*(273+T))
     # h be the head of air column causing air flow
    h = (x1/100)*(1000/R)
     # let y be the air flow through orifice 
    cd = 0.6
    k = 2*9.81*h
    y = cd*A*(k**0.5)
     # v b ethe volumetric efficiancy
    v = (y/Q)

    # PI be the power inut to the compressor
    n=5
    PI=((n/200)*3600*0.85*(1/t1))
    # IP be the isothermal power
    IP =101.325*y*math.log(PR)
    # IE be the isothermal efficiancy
    IE = IP/PI
    # AP  BE THE ADIABATIC POWER
    # r be the gamma 
    AP=(((2*1.4)/(1.4-1))*101.325*y*(math.pow(PR,((1.4-1)/(2*1.4)))-1))
    # AE be the adiabatic efficiancy
    AE = AP/PI

    # E be the efficiancy ratio 
    E = AE/IE
    v2=v*100
    IE1=IE*100
    AE1=AE*100
    context={
        'p4':p3,
        'PR1':PR,
        'h1':h,
        'v3':v2,
        'PI1':PI,
        'IP1':IP,
        'AP1':AP,
        'IE2':IE1,
        'AE2':AE1,
        'E1':E

    }




    return render (request,'result.html',context)


