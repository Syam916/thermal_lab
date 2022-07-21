from socket import IP_HDRINCL
from django.shortcuts import render
import math
from experiments.models import  Compressor,Blower,Heatbalence,Bhpvilliers,Morse

# Create your views here.
def home(request):
    return render(request,'home.html')


def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')



def compressor(request):
    return render(request,'compressor1.html')

def index(request):
    return render(request,'index.html')


def compexp(request):
    data1=[1,2,3]
    context={
        'data2':data1
    }
    return render(request,'compexp.html',context)

def blowexp(request):
    return render(request,'blowexp.html')

def morseexp(request):
    return render(request,'morseexp.html')


def compd(request):
    return render(request,'compd.html')



def result(request):

    p22=int(request.POST['p2'])
    x1=float(request.POST['x'])
    t1=int(request.POST['t'])
    T=30
    p1=1.033
    p3 = p22+p1
    p3=round(p3,2)
                # PR is the pressure ratio
    PR= p3/p1
    PR=round(PR,2)
                # theorytical disacharge is Q
    Q = 0.0094333
                # A be the area of orifice 
    A = 0.000452
                # R be the density of air at room temperature
    R = (1.033*10**4)/(29.27*(273+T))
                # h be the head of air column causing air flow
    h = (x1/100)*(1000/R)
    h=round(h,2)
                # let y be the air flow through orifice 
    cd = 0.6
    k = 2*9.81*h
    y = cd*A*(k**0.5)
                # v b ethe volumetric efficiancy
    v = (y/Q)
    v=round(v,2)

                # PI be the power inut to the compressor
    n=5
    PI=((n/200)*3600*0.85*(1/t1))
    PI=round(PI,2)
                # IP be the isothermal power
    IP =101.325*y*math.log(PR)
    IP=round(IP,2)
                # IE be the isothermal efficiancy
    IE = IP/PI
    IE=round(IE,2)
                # AP  BE THE ADIABATIC POWER
                # r be the gamma 
    AP=(((2*1.4)/(1.4-1))*101.325*y*(math.pow(PR,((1.4-1)/(2*1.4)))-1))
    AP=round(AP,2)
                # AE be the adiabatic efficiancy
    AE = AP/PI
    AE=round(AE,2)

                # E be the efficiancy ratio 
    E = AE/IE
    v2=v*100
    IE1=IE*100
    AE1=AE*100
    AE1=round(AE1,2)
    IE1=round(IE1,2)
    E=round(E,2)
    v2=round(v2,2)
    context={
        'p22':p22,
        'x1':x1,
        't1':t1,
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
    #ins=Compressor(p22=p22,x1=x1,t1=t1)
    #ins.save()




    return render (request,'compresult.html',context)

def heat(request):
    return render(request,'heat1.html')

def bhp3(request):
    return render(request,'bhp3.html')

def morse1(request):
    return render(request,'morse.html')


def heatexp(request):
    return render(request,'heatexp.html')

def heatresult(request):
    L1=int(request.POST['L'])
    X1=float(request.POST['X'])
    T11=int(request.POST['T'])
    T111=int(request.POST['T1'])
    T22=int(request.POST['T2'])
    Q1=int(request.POST['Q'])
    T33=int(request.POST['T3'])
    T44=int(request.POST['T4'])
    
     # converting the load in kgf to newtons
    W=L1*9.81
    # BRAKE POWER
    d=0.257
    N=1500
    BP = (3.14*d*N*W)/(60*1000)
    # HEAT ENERGY BRAKE POWER
    HEBP=BP*60
    #HEAT ENERGY SUPPLIED
    cv=41870
    Mf = (20*60*1000*0.78)/(T11*10**6)
    HES=Mf *cv
    # ENERGY TO COOL WATER 
    cp = 4.186
    ECW = Q1*cp*(T22-T111)
    # ENERGY TO EXHAUST GAS
    e=T111+273
    Ra = (1.01325*10**5)/(287*e)
    A = (3.14*d**2)/4
    cd=0.5
    h=(X1/100)*(1000/Ra)
    Va = cd*A*math.pow((2*9.81*h),1/2)
    Ma=Ra*Va
    Mg = Ma + Mf
    Cpg=1.066
    EEG= Mg*Cpg*(T33-T44)
    # PERCENT OF HEAT ENERGY TO POWER
    X11 = (HEBP/HES)*100
    # % ENERGY TO COOL WATER
    X2= (ECW/HES)*100
    # % ENERGY TO EXHAUST GAS
    X3 = (EEG/HES)*100
    #  HEAT UNACCOUNTED
    X4 = HES-HEBP-ECW-EEG
    # % OF HEAT UNACCOUNTED
    X14 = (X4/HES)*100
    BP=round(BP,2)
    HES=round(HES,2)
    HEBP=round(HEBP,2)
    ECW=round(ECW,2)
    EEG=round(EEG,2)
    X4=round(X4,2)
    X11=round(X11,2)
    X2=round(X2,2)
    X3=round(X3,2)
    X14=round(X14,2)
    context={
        'L1':L1,
        'X1':X1,
        'T11':T11,
        'T111':T111,
        'T22':T22,
        'Q1':Q1,
        'T33':T33,
        'T44':T44,
        'BP1':BP,
        'HES1':HES,
        'HEBP1':HEBP,
        'ECW1':ECW,
        'EEG1':EEG,
        'X44':X4,
        'X111':X11,
        'X22':X2,
        'X33':X3,
        'X141':X14

    }
    #ins=Heatbalence(L1=L1,X1=X1,T11=T11,T111=T111,T22=T22,Q1=Q1,T33=T33,T44=T44)
    #ins.save()

    return render(request,'heatresult.html',context)

def bhp3exp(request):
    return render(request,'bhp3exp.html')

def bhp3result(request):
    L1=float(request.POST['L'])
    X1=float(request.POST['X'])
    T1=int(request.POST['T'])
    
    W =L1*9.81
    N= 3000
    D=0.1942
    A2 = (3.14*D**2)/4
    r= (D+2*0.006)/2
    BP = (2*3.14*N*r*W)/(60*1000)

       # DENSITY OF AIR
    R=(1.01325*10**5)/(287*(273+29))  

#              MANOMETRIC HEAD

    h = (X1/100)*(1000/R)

# air flow through orifice
    cd=0.6
    d =16
    A =(3.14*d**2)/(4*1000**2)
    y = cd*A*math.pow((2*9.81*h),1/2)
#           fuel consumption
    FC=(20*0.78*1000*60*60)/(T1*10**6)
    fc1 = FC/60
# air fuel ratio
    AFR= (y*R*60)/fc1
# specific fuel consumption
    SFC=FC/BP
# VOLUMETRIC EFFICIANCY    
    L2 = 0.0667
    A1 = (3.14*0.07**2)/4
    VE = (y*60*2)/(A1*L2*N)
    VE=VE*100
# BRAKE MEAN EFFECTIVE PRESSURE
    BMEP = (BP*60*2)/(L2*A2*N)
# BRAKE TORQUE
    BT=(BP*60)/(2*3.14*N)
# EFFICIANCY OF BRAKE THERMAL
    CV = 44380
    EBT = (BP*60)/(fc1*CV)
    EBT=EBT*100
    W=round(W,2)
    BP=round(BP,2)
    FC=round(FC,2)
    SFC=round(SFC,2)
    VE=round(VE,2)
    BMEP=round(BMEP,2)
    AFR=round(AFR,2)
    BT=round(BT,5)
    EBT=round(EBT,2)
    context={
        'W1':W,
        'BP1':BP,
        'FC1':FC,
        'SFC1':SFC,
        'VE1':VE,
        'BMEP1':BMEP,
        'AFR1':AFR,
        'BT1':BT,
        'EBT1':EBT,
        'L1':L1,
        'X1':X1,
        'T1':T1

    }
    '''ins=Bhpvilliers(Load=L1,Manometric_reading=X1,Time=T1,Brake_power=BP,Volumetric_efficiancy=VE,Fuel_consumption=FC,Brake_torque=BT,Thermal_efficianc=EBT)
    ins.save()'''

    return render(request,'bhp3result.html',context)



def blower(request):
    return render (request,'blower1.html')

def blowresult(request):
    s1=float(request.POST['s'])
    d1=float(request.POST['d'])
    T1=int(request.POST['T'])
    t81=int(request.POST['t'])
    
    n=5 #number of revolutions of energy meter
    roomPressure=1.0132*(10**5) #in n/mm^2
    EMconstant=150
    efficiency_mec=0.95
    A1=1.96*(10**-3)
    A2=4.9*(10**-4)
    cd=0.96
    g=9.81
    #density of air
    density=(1.01325*10**5)/(287*(273+T1))  

    #Static head in m of air
    H1=(s1*1000)/(100*density) #m of air
    #delivery head
    H2=(d1*1000)/(100*density) # m of air
    #input Power
    Ip=(n/t81)*(1/EMconstant)*3600*efficiency_mec
    #Discharge
    discharge=cd*((A1*A2)/(A1**2-A2**2)**0.5)*(2*g*H2)**0.5
    #velocity 
    velo=discharge/A1
    #dynamic head
    dynHead=(velo**2)/2*g
    #total head
    Total_head=H1+dynHead
    #Air power 
    Air_power=((density*discharge*Total_head)/75)*0.736
    #Efficiency
    Effi=(Air_power/Ip)*100

    Effi=round(Effi,2)
    Air_power=round(Air_power,2)
    Ip=round(Ip,2)
    velo=round(velo,2)
    discharge=round(discharge,2)
    Total_head=round(Total_head,2)
    dynHead=round(dynHead,2)
    H1=round(H1,2)
    H2=round(H2,2)


    context= {
        's1':s1,
        'd1':d1,
        'T1':T1,
        't81':t81,
        'E1':Effi,
        'A1':Air_power,
        'IP1':Ip,
        'V':velo,
        'D':discharge,
        'TH':Total_head,
        'D1':dynHead,
        'H2':H2,
        'H1':H1
        
        
        
    }
    #ins=Blower(s1=s1,d1=d1,T1=T1,t81=t81)
    #ins.save()
    
    
    
    return render(request,'blowresult.html',context)



def morseresult(request):
    W=int(request.POST['w'])
    w11=float(request.POST['w1'])
    w22=float(request.POST['w2'])
    w33=float(request.POST['w3'])
    w44=float(request.POST['w4'])
    
            # FOR BRAKE POWER
    N= 1500
    x=(W*N)/2717
    x1=(w11*N)/2717
    x2=(w22*N)/2717
    x3=(w33*N)/2717
    x4=(w44*N)/2717
    #indicated power at each cylinder
    L1=x-x1
    L2=x-x2
    L3=x-x3
    L4=x-x4
            # total indicated power
    IP = L1+L2+L3+L4
            # total brake power
    BP = x
        # efficiancy
    EF= BP/IP
                # FRICTIONAL POWER
    FP = IP-BP
    
    context ={
        'x11':x1,
        'x22':x2,
        'x33':x3,
        'x44':x4,
        'L11':L1,
        'L22':L2,
        'L33':L3,
        'L44':L4,
        'BP1':BP,
        'EF1':EF,
        'FP1':FP,
        'IP1':IP
        
    }
    #ins=Morse(W=W,w11=w11,w22=w22,w33=w33,w44=w44)
    #ins.save()
    
    
    
    return render(request,'morseresult.html',context)
