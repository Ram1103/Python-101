#while loop
'''print("when did india get its independence")
year=int(input())
while(year!=1947):
    print("you got it wrong, try again")
    year=int(input())
print("you got it right")'''


#factorial of a number
'''print("enter a number")
n=int(input())
i=1
answer=1
while(i<=n):
    answer=answer*i
    i+=1
print(answer) '''   

#while with absolute function
'''print("enter a number")
num=abs(int(input()))
digits=1
while(num>9):
    num=num // 10
    digits=digits+1
print(digits)'''

#reversing a number
'''print("enter a number")
num=int(input())
if(num>=0):
    rev=num%10
    num=num//10
    while(num>0):
        r=num%10
        num=num//10
        rev=rev*10+r
    print(rev)    
else:
    absnum=abs(num) 
    rev=absnum%10
    absnum=absnum//10
    while(absnum>0):
        r=absnum%10
        absnum=absnum//10
        rev=rev*10+r
    print(rev-2*rev) '''


#palindrome
'''print("enter a number")
num=int(input())
absnum=abs(num) 
rev=absnum%10
absnum=absnum//10
while(absnum>0):
     r=absnum%10
     absnum=absnum//10
     rev=rev*10+r
if(num<0):
    rev=rev-2*rev
if(num==rev):
    print("Palindrome")
else:
    print("Not  a Palindrome")'''


x=120.25555
print(f'{x:1.2f}')




