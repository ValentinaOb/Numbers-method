from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np



n=4
a4=1
a3=-2
a2=0
a1=1
a0=-1.5

if(a3**2 > a4*a2):
    print("True     a3^2 > a4*a2")
else:
    print("False    a3^2 > a4*a2")
if(a2**2 > a3*a1):
    print("True     a2^2 > a3*a1")
else:
    print("False    a2^2 > a3*a1")
if(a1**2 > a2*a0):
    print("True     a2^2 > a2*a0")
else:
    print("False    a2^2 > a2*a0")

a=max(abs(a0),abs(a1),abs(a2),abs(a3))
b=max(abs(a1),abs(a2),abs(a3),abs(a4))

print("A: {}\nB: {}".format(a,b))
p1=abs(a0)/(abs(a0)+b)
p2=1+(a/abs(a4))
print("P1: ", abs(a0), " / ", (abs(a0)+b))
print("P2: ", a , " / ", abs(a4))
print("We get:\n{}  <=  |x| <=  {}".format(p1,p2))

###


t=[['X','Y']]

x=-p2
while x<=p2:
    y=x**4 - 2*x**3 + x -1.5
    t.append([x, y])
    x+=0.5


print(tabulate(t))

gr_x=[]
gr_y=[]
x=-p2
while x<=p2:
    y=x**4 - 2*x**3 + x -1.5
    gr_x.append(x)
    gr_y.append(y)
    x+=0.1

plt.plot(gr_x, gr_y)
plt.grid()
plt.show()
