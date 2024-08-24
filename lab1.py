from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np


def one():

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

def f(x):
    y=x**4-2*x**3+x-1.5
    return y

'''
def inp():
    a=input("A: ")
    b=input("B: ")
    E=input("E: ")
    return a,b,E
    
    #a,b,E=inp()
'''

def res(a,b,E,k):

    x=(b+a)/2

    if(b-a < 2*E):
        print("\nX: ", x,"\nK: ", k)
        print("b-a: ", (b-a))
        print("F: ", f(x))
        status=True
        return status,a,b,k
    else:
        if(f(x) == 0):
            print("\nX: ", x,"\nK: ", k)
            print("F: ", f(x))
            status=True
            return status,a,b,k
        else:
            if(f(a)*f(x) < 0):
                b=x
            else:
                a=x
            k+=1
            status=False
            return status,a,b,k
            

def two():

    a=float(input("A: "))
    b=float(input("B: "))
    E=float(input("E: "))
    
    while (f(a)*f(b)>=0):
        a=input("A: ")
        b=input("B: ")
        E=input("E: ")
    
    k=0

    status=False

    while status==False:
        status,a,b,k=res(a,b,E,k)
        
two()
        
