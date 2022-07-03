#Question 1
n = int(input("Enter the number="))

l1 = []

for i in range(1,n):
    if n%i==0:
        l1.append(i)

sum = 0

for j in range(len(l1)):
    sum = sum + l1[j]

if sum == n:
    print(n,"is a Perfect Number")
else:
    print(n,"is not a Perfect Number")
    
#------------------------------------------------------------------------------------------------------------------------
    
#Question 2
s1 = input("Enter the word:")
s2 = s1.lower()

reverse_s2 = s2[::-1]

if s2 == reverse_s2:
    print(s1,"is a Palindrome.")
else:
    print(s1,"is not a Palindrome.")
    
#------------------------------------------------------------------------------------------------------------------------
    
#Question 3
from math import factorial

n = int(input("Enter the number of rows="))

for i in range(n):
    for j in range(n-i):
        print(end=" ")

    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        
    print()
    
#------------------------------------------------------------------------------------------------------------------------
    
#Question 4
s1 = input("Enter the sentence/word:")
s2 = s1.lower()

l1 = []

for i in range(len(s2)):
    if s2[i]==" ":
        continue
    elif s2[i] not in l1:
        l1.append(s2[i])

if len(l1)==26:
    print(s1,"is a Pangram.")
else:
    print(s1,"is not a Pangram.")
    
#------------------------------------------------------------------------------------------------------------------------
    
#Question 5
s1 = input("Enter the words in a hyphen-separated sequence:")

l1 = list(s1.split("-"))
l1.sort()
print("-".join(l1))

#------------------------------------------------------------------------------------------------------------------------

#Question 6
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")
    
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: {kwargs['student_name']}")
            print(f"Student Class: {kwargs['student_class']}")

 
student_data(student_id='21102033', student_name='chhavi')

student_data(student_id='21102034', student_name='xyz', student_class ='XI')

#------------------------------------------------------------------------------------------------------------------------

#Question 7
class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()

#------------------------------------------------------------------------------------------------------------------------

#Question 8
def findTriplets(arr, n):

	found = False
	for i in range(0, n-2):
	
		for j in range(i+1, n-1):
		
			for k in range(j+1, n):
			
				if (arr[i] + arr[j] + arr[k] == 0):
					print(arr[i], arr[j], arr[k])
					found = True
	if found == False:
		print("No triplets exist")
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input())
	lst.append(ele) 
print(findTriplets(lst,n))                

#------------------------------------------------------------------------------------------------------------------------

#Question 9
class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")
