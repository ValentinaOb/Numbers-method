
x=3
h=1.725
t =0.511

y0_1=-0.113
y0_2=-0.726
y0_3=-3.391
y0_4=-5.286


import numpy as np
import math

'''f_1=1/h * ( y0_1 + (y0_2*(2*t-1)/2) + (y0_3*(3*t**2-6*t+2)/6) + (y0_4*(4*t**3-18*t**2+22*t-6)/24))

f_2=1/h**2 * ( y0_2 + (y0_3*(t-1)) + (y0_4*(6*t**2-18*t+11)/12))

print("a) F_1: ",f_1)
print("a) F_2: ",f_2)

f_1=1/h * (y0_1 - (1/2)*y0_2+(1/3)*y0_3-(1/4)*y0_4)

f_2=1/h**2 *(y0_2 - y0_3+(11/12)*y0_4)

print("\nb) F_1: ",f_1)
print("b) F_2: ",f_2)'''

'''x1=1
x2=1.075
add=0.075
s=0
for i in range(20):
    x_=round((x1+x2)/2,4)
    e=round(math.e**(x_),4)
    f=round(e/((1+x_)**2),4)

    s+=f

    print(x_, " ", e, " ", f)
    x1+=add
    x2+=add
print(s)
print("I: ",add*s)'''


n=12
x=1
add=1.5/n
s1=0
s2=0
f=[]
for i in range(n+1):
    
    e=round(math.e**(x),5)
    f_el=round(e/((1+x)**2),5)
    f.append(f_el)

    if i%2==0 and i !=0 and i!=n:
        s1+=f_el
    elif i !=0 and i!=n:
        s2+=f_el

    print(x, " ", e, " ", f_el)
    x+=add

i_hc=round(((1/n)/3)*(f[0]+f[-1]+4*s2+2*s1),5)
print(s1, " ",s2)
print("I: ",i_hc)





