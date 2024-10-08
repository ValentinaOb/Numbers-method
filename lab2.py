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
    det= np.linalg.det([[a11,a12,a13,a14],[a21,a22,a23,a24],[a31,a32,a33,a34],[a41,a42,a43,a44]])

    if(det!=0):
    
        det1= np.linalg.det([[data1,a12,a13,a14],[data2,a22,a23,a24],[data3,a32,a33,a34],[data4,a42,a43,a44]])
        det2= np.linalg.det([[a11,data1,a13,a14],[a21,data2,a23,a24],[a31,data3,a33,a34],[a41,data4,a43,a44]])
        det3= np.linalg.det([[a11,a12,data1,a14],[a21,a22,data2,a24],[a31,a32,data3,a34],[a41,a42,data4,a44]])
        det4= np.linalg.det([[a11,a12,a13,data1],[a21,a22,a23,data2],[a31,a32,a33,data3],[a41,a42,a43,data4]])
    
        #det2=a11*data2*a33*a44 +a21*a43*a14+ data1*a34*a41 -   a14*a23*data3*a41 -a34*data4*a11- a13*a31*a44
        #det3=a11*a22*data3*a44 +a21*data4*a14+ a12*a34*a41 -   a14*data2*a32*a41 -a34*a42*a11- data1*a31*a44
        #det4=a11*a22*a33*data4 +a21*a43*data1+ a12*data3*a41 -   data1*a23*a32*a41 -data3*a42*a11- a13*a31*data4

        x1=int(det1/det)
        x2=int(det2/det)
        x3=int(det3/det)
        x4=int(det4/det)

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


    u11=4
    u12=2
    u13=3
    u14=1

    l21=5/4
    l31=3/2
    l41=3/4

    u22=1-l21*u12
    l32=(2-l31*u12)/u22
    l42=(-1-l41*u12)/u22

    u23=2-l21*u13
    u33=4-l31*u13-l32*u23
    l43=(2-l41*u13-l42*u23)/u33
    u24=2-l21*u14
    u34=1-l31*u14-l32*u24
    u44=2-l41*u14-l42*u24-l43*u34
    #print("U23: ",u23,"\nL43: ",l43,"\nU33: ",u33)

    #print("\n\n22: ",(l21*u12+u22==1),"\n23: ",(l21*u13+u23==2),"\n24: ",(l21*u14+u24==2))
    #print("\n\n32: ",(l31*u12+l32*u22==2),"\n33: ",(l31*u13+l32*u23+u33==4),"\n34: ",(l31*u14+l32*u24+u34==1))
    #print("\n\n42: ",(l41*u12+l42*u22==-1),"\n43: ",(l41*u13+l42*u23+l43*u33==2),"\n44: ",(l41*u14+l42*u24+l43*u34+u44==2))

    print("\nL21: ",l21,"\nL31: ",l31, "\nL41: ",l41, "\nL32: ",l32, "\nL42: ",l42, "\nL43: ",l43)
    print("\nU22: ",u22,"\nU23: ",u22, "\nU24: ", u24, "\nU33: ",u33, "\nU34: ",u34, "\nU44: ",u44)

    y1=1
    #l21*y1+y2=3
    y2=3-l21*y1
    #l31*y1+l32*y2+y3=0
    y3=-l31*y1-l32*y2
    #l41*y1+l42*y2+l43*y3+y4=1
    y4=1-l41*y1-l42*y2-l43*y3
    print("\nY1: ",y1,"\nY2: ",y2, "\nY3: ",y3, "\nY4: ",y4)

    print("\n\ny2: ",(l21*y1+y2==3),"\ny3: ",(l31*y1+l32*y2+y3==0),"\ny4: ",(l41*y1+l42*y2+l43*y3+y4==1))

    #u11*x1+u12*x2+u13*x3+u14*x4=y1
    #u22*x2+u23*x3+u24*x4=y2
    #u33*x3+u34*x4=y4
    #u44*x4=y4
    x4=y4/u44
    x3=(y3-u34*x4)/u33
    x2=(y2-u23*x3-u24*x4)/u22
    x1=(y1-u12*x2-u13*x3-u14*x4)/u11

    print("\nX1: ",x1,"\nX2: ",x2, "\nX3: ",x3, "\nX4: ",x4)

    print("\nRes1: ", (4*x1+2*x2+3*x3+x4))
    print("\nRes2: ", (5*x1+x2+2*x3+2*x4))
    print("\nRes3: ", (6*x1+2*x2+4*x3+x4))
    print("\nRes4: ", (3*x1-x2+2*x3+2*x4))
    #4*x1+2*x2+3*x3+x4=3
    #5*x1+x2+2*x3+2*x4=3
    #6*x1+2*x2+4*x3+x4=0 
    #3*x1-x2+2*x3+2*x4=1



two()


