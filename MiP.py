ar=[]
t=""
dictionary={}
H_dic={1:0}
Way_dic={}

print("Input data (1-2 5): ")

while t!="end":
    t=input()
    ar.append(t)
ar.pop()

for i in ar:
    key, value = i.split(" ")
    dictionary[key]=int(value)
    
print(dictionary)

print("Input End: ")
n = int(input())

start=[1]
end=[]
for i in range(2,n+1):
    end.append(i)

print("End: ",end)

result=[]
our_key=[]
#for j in dictionary:

while len(end)!=0:
    x=[]
    our_key=[]

    for i in dictionary:
        el1, el2= i.split("-")
        el1=int(el1)
        el2=int(el2)
        if (el1 in start and el2 not in start):
            our_key.append(i)
            #print("D:", dictionary[i])
            for i1 in H_dic:
                if(i1==el1):
                    sum=H_dic[i1]
            x.append(dictionary[i]+sum)
            

    print("X: ",x)
    min_val= min(x)
    ind=x.index(min_val)
    el1, el2= our_key[ind].split("-")
    el1=int(el1)
    el2=int(el2)
    #print("El2: ",el2)
    print("End: ",end)
    start.append(el2)
    #if(el2 in end): end.remove(el2)
    end.remove(el2)

    #Way_dic[our_key[ind]] = dictionary[our_key[ind]]
    Way_dic[our_key[ind]] = min_val
    
    print(Way_dic)
    
    H_dic[el2] = min_val

    print(H_dic)

    #result.append(our_key[ind], " : h = ", dictionary[our_key[ind]])



