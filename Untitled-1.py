voltage=float(input('Enter the voltage: '))
current=float(input('Enter the current: '))
T2=int(input())
T3=int(input())
T4=int(input())
T5=int(input())
T6=int(input())
T7=int(input())

power=voltage*current
avg=(T2+T3+T4+T5+T6)/5
area=3.14*0.038*0.5
theoritical_Value=(power)/(avg-T7)
