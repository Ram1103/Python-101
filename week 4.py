#lists
'''l=[1,2,2]
print(l)
l.remove(2)
print(l)'''

#birthday paradox
'''import random
l=[]
for i in range(30):
    l.append(random.randint(1,365))
l.sort()
print(l)
i=0
flag=0
while(i<len(l)-1):
    if(l[i]==l[i+1]):
         print("repeats",l[i],l[i+1])
         flag=1
         break
    i=i+1

if(flag==0):
    print("no repetition")'''

#sorting
'''l=[2,5,7,9,1,4,8,3,6,0,7]
x=[]
while(len(l)>0):
    least=l[0]
    for i in range(len(l)):
        if(least>l[i]):
            least=l[i] 
    x.append(least)
    l.remove(least)
print(l)
print(x)'''

#dot product
'''x=[1,2,3]
y=[4,5,6]
sum=0
for i in range(len(x)):
    sum=sum+(x[i]+y[i])
print(sum)'''

#matrix addition
'''dim=3

r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,3]
s2=[4,5,6]
s3=[7,8,9]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)

B=[]
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(dim):
    for j in range(dim):
         C[i][j]=A[i][j]+B[i][j]
print(C)'''

#matrix multiplicatiuon
'''dim=3

r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,3]
s2=[4,5,6]
s3=[7,8,9]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)

B=[]
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
             C[i][j]=C[i][j] + A[i][k]*B[k][j]
print(C)


#or 

import numpy
print(A)
print(B)
x=numpy.mat(A)
y=numpy.mat(B)
print(x*y)'''

#GrPA 1

xlist=[]
i=int(0)
xsum=0
while(i>=0):
    response=input()
    if response=="END":
        break
    xlist.insert(i,int(response))
    xsum+=int(response)
    i=i+1

n=len(xlist)
xbar=xsum/n
newlist =[(x-xbar)**2 for x in xlist]   
xsum=0
for x in newlist:
    xsum += x
stddev=(xsum/(n-1))**0.5
#stddev=round(stddev,2)
print(stddev,end='')    



