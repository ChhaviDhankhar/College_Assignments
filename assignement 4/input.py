#QUESTION 1
marks=int(input("enter marks ="))
if marks<25:
    print("grade is F")
elif 25<=marks<45:
    print("grade is E")
elif 45<=marks<50:
    print("grade is D")
elif 50<=marks<60:
    print("grade is C")
elif 60<=marks<80:
    print("grade is B") 
else :
    print("grade is A")
    
 #QUESTION 2
y=int(input("enter year= "))
if y%4==0 and y%100!=0:
    print(y,"is a leap year")
elif y%4==0 and y%100==0:
    if y%400==0:
        print(y,"is a leap year")
    else:
        print(y,"is not a leap year") 
else: 
    print(y,"is not a leap year") 
    
    
#QUESTION 3
from random import randint, random

for i in range(1,11):
    x = randint(0,9)
    y = randint(0,9)
    answer = x*y

    print("Question ", i,":",x,"x",y,"=")
    ans = int(input())
    if ans==answer:
        print("Right!")
    else:
        print("Wrong. The answer is",answer)
        
   
  
#QUESTION 4

for candies in range(200):
    if candies % 5 == 2:
        if candies % 6 == 3:
            if candies % 7 == 2:
                print(candies,'candies are in the bowl!')
