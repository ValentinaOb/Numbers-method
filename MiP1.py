ar=[]

dictionary={}
inverse = {}
way={}

H_dic={1:0}

with open('d.txt', 'r') as file:
    for line in file:
        ar.append(line)

for i in ar:
    key, value = i.split(" ")
    dictionary[key]=int(value)
    inverse[key]=0
    
print(dictionary)
print(inverse)

print("Input End: ")
n = int(input())

result=[]
our_key=[]

start=1
t=[]
max_val=[]
r=[]
status=False
ways=[]
bad=[]

H_dic={}
H_Bad_dic={}

st=[]
end =False
min_r=[]
need_to_continue=False

while status == False:
    
    t=[]
    max_val=[]
    while start!=n :
        x=[]
        our_key=[]

        for i in dictionary:
            if end==True:
                break
            el1, el2= i.split("-")
            el1=int(el1)
            el2=int(el2)
            
            
            if (start == el1):
                if el2 not in st:                
                    our_key.append(i)
                    sub = dictionary[i] - inverse[i]
                
                    if(sub==0):
                        bad.append(t)
                        if i not in r:
                            r.append(i)

                    x.append(sub)

        if len(x)==0:
            break
        max_val.append(max(x))
        if max(x)==0:
            break
        ind=x.index(max(x))
        t.append(our_key[ind])
        print(t)
        
        el1, el2= our_key[ind].split("-")
        el1=int(el1)
        el2=int(el2)
        start=el2
        
    
    if end==True:
        break
    ways.append(t)
    min_val=min(max_val)
    min_r.append(min_val)
    for i in t:
        inverse[i] += min_val

    for i in dictionary:
        sub = dictionary[i] - inverse[i]
                
        if(sub==0):
            bad.append(t)
            if i not in r:
                r.append(i)
    start=1

    n1=1
    while n1!=n+1:
        k1=0
        k=0
        for i in dictionary:
            el1, el2= i.split("-")
            el1=int(el1)
            el2=int(el2)
            if el1 == n1:
                k1+=1
        H_dic[n1]=k1
        n1+=1

    for i in range(1,n+1):   
        H_Bad_dic[i]=0

    for i in dictionary:
        if i in r:
            el1, el2= i.split("-")
            el1=int(el1)
            H_Bad_dic[el1]+=1

    one_cicle =False
    st=[]
    use=[]
    for k in range(len(r)):
        if status == True: 
            break
        if one_cicle == True:
            for i in dictionary:
                el1, el2= i.split("-")
                el1=int(el1)
                el2=int(el2)
                if H_Bad_dic[el2]==H_dic[el2] and H_Bad_dic[el2]!=0 and el2 not in st and i not in r:
                    H_Bad_dic[el1]+=1
                    st.append(el2)
                    use.append(el1)
                    

        for i in dictionary:
            el1, el2= i.split("-")
            el1=int(el1)
            el2=int(el2)
            if H_Bad_dic[el2]==H_dic[el2] and H_Bad_dic[el2]!=0 and el1 not in use and i not in r:
                H_Bad_dic[el1]+=1
                if el2 not in st:
                    st.append(el2)
                if el1 not in use:
                    use.append(el1)
            if H_Bad_dic[1]==H_dic[1] and H_Bad_dic[1]!=0: 
                status=True
                break
        
        one_cicle=True
                    
    need_to_continue=False

print("\nWays: ", ways)    
print("R: ", r) 
print("Min_r: ", min_r) 
        


