a11=4
a12=2
a13=3
a14=1

a21=5
a22=1
a23=2
a24=2

a31=6
a32=2
a33=4
a34=1

a41=3
a42=-1
a43=2
a44=2

data1=1
data2=3
data3=0
data4=1

import numpy as np

def one():
    #det=a11*a22*a33*a44 +a21*a43*a14+ a12*a34*a41 -   a14*a23*a32*a41 -a34*a42*a11- a13*a31*a44
    det= np.linalg.det([[a11,a12,a13,a14],[a22,a22,a23,a24],[a31,a32,a33,a34],[a41,a42,a43,a44]])

    if(det!=0):
    
        det1= np.linalg.det([[data1,a12,a13,a14],[data2,a22,a23,a24],[data3,a32,a33,a34],[data4,a42,a43,a44]])
        det2= np.linalg.det([[a11,data1,a13,a14],[a21,data2,a23,a24],[a31,data3,a33,a34],[a41,data4,a43,a44]])
        det3= np.linalg.det([[a11,a12,data1,a14],[a21,a22,data2,a24],[a31,a32,data3,a34],[a41,a42,data4,a44]])
        det4= np.linalg.det([[a11,a12,a13,data1],[a21,a22,a23,data2],[a31,a32,a33,data3],[a41,a42,a43,data4]])
    
        #det2=a11*data2*a33*a44 +a21*a43*a14+ data1*a34*a41 -   a14*a23*data3*a41 -a34*data4*a11- a13*a31*a44
        #det3=a11*a22*data3*a44 +a21*data4*a14+ a12*a34*a41 -   a14*data2*a32*a41 -a34*a42*a11- data1*a31*a44
        #det4=a11*a22*a33*data4 +a21*a43*data1+ a12*data3*a41 -   data1*a23*a32*a41 -data3*a42*a11- a13*a31*data4

        x1=det1/det
        x2=det2/det
        x3=det3/det
        x4=det4/det

        print("Det: ",det,"\nDet1: ",det1,"\nDet2",det2,"\nDet3",det3,"\nDet4",det4,"\nX1: ",x1,"\nX2: ",x2,"\nX3: ",x3,"\nX4: ",x4)

        print(4*x1+2*x2+3*x3+x4)
        print(5*x1+1*x2+2*x3+2*x4)
        print(6*x1+2*x2+4*x3+x4)
        print(3*x1-1*x2+2*x3+2*x4)

def two():

    det1= a11
    det2= np.linalg.det([[a11,a12],[a21,a22]])
    det3= np.linalg.det([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
    det4= np.linalg.det([[a11,a12,a13,a14],[a21,a22,a23,a24],[a31,a32,a33,a34],[a41,a42,a43,a44]])

    print ("Det1: ",(det1!=0),"\nDet2: ",(det2!=0),"\nDet3: ",(det3!=0),"\nDet4: ",(det4!=0))
    print ("Det1: ",det1,"\nDet2: ",det2,"\nDet3: ",det3,"\nDet4: ",det4,"\n")


two()