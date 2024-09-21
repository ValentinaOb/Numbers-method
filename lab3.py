import math
import numpy as np

'''print(-2*math.sin(2*1.8-1))
print(math.sin(1.6))
print(-(math.cos(2*1.8-1) +1.6-0.8))
print(-(1.8-math.cos(1.6)-2))
'''

'''print(-99957000/203055667)
print(100000000/203055667)
print(100000000/203055667)
print(103100000/203055667)'''

#print(max((1.85611 - 1.8), (1.71474 - 1.6)))

k=0
x1=1.8
x2=1.6
delta=1
print("\n")

while delta>0.001:
    W11= -2*math.sin(2*x1-1)
    W12 = 1
    W21=1
    W22=math.sin(x2)

    F11=-(math.cos(2*x1-1) +x2-0.8)
    F21=-(x1-math.cos(x2)-2)

    #W^(-1)
    det=np.linalg.det([[W11,W12],[W21,W22]])

    A11=W22
    A12=-W21
    A21=-W12
    A22=W11

    T11=(1/det) * A11
    T12=(1/det) * A21
    T21=(1/det) * A12
    T22=(1/det) * A22

    delta1=T11*F11+T12*F21
    delta2=T21*F11+T22*F21

    x1_first=x1
    x2_first=x2

    x1=delta1+x1_first
    x2=delta2+x2_first

    delta=max(abs(x1-x1_first),abs(x2-x2_first))
    k+=1

    print(k, "   X1: ", x1,"   X2: ",x2,"   Delta: ", delta)

print("\n")