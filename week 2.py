#variables can be alpha numeric numbers and underscore symbol
'''Roll=10
ROLL=15
roll=20
print(ROLL,Roll,roll)'''               


#operators used within such that we can reduce the code
'''count = 10
print(count)
count += 2
print(count)    '''                      


#answer is true, in operator
#print("rem" in "remember")                



#sting methods
'''x="RAM"                                     
print(x.lower())
print(x.upper())'''



#if condition
'''print("enter your birth year")                
i=int(input())
c=2021
age= c-i
if (age<13):
    print("you can't watch")
else:
    print(age)
    print("you can watch")'''


#moving from a to b
'''print("to move from A to B")
time= int(input("Enter time:"))
longer = int(input("enter longer tinme:"))
if (time>=longer):
    price=int(input("enter the price:"))
    higher=int(input(("enter higher:")))
    if(price>=higher):
        print("train")
    else:
        print("coach")
else:
     price=int(input("enter the price:"))
     higher=int(input(("enter higher:")))
     if(price>=higher):
        print("day time flight")
     else:
        print("red eye flight")
print("reached b")     '''


#importing library
'''import math
print(math.log(10))
print(math.pow(3, 2))'''


#stimulating a coin  toss
'''import random
a=random.random()
if(a<0.5):
    print("heads")
else:
    print("tails")'''

#stimulating 6 faced dice
'''import random
print(random.randrange(1, 7)) '''


#calender
'''import calendar
print(calendar.calendar(2021))'''

'''from calendar import*
print(month(2021, 5))'''

x=bool(input())
print(x)










from os import system
ls = lambda: system('cls')