#question:1
a=int(input('enter first no:'))
b=int(input('enter second no:'))
c=int(input('enter third no:'))
Average= a+b+c/3
print ('Average is:',Average)


#question:2
GI=float(input('gross income is:'))
Num_dependents=int(input("enter no. of dependents:"))
sd=10000
dd=3000
Taxable_income=GI-sd-(Num_dependents*dd)
print('taxable income is:', Taxable_income)
Tax_rate_percent=20
Tax=(Taxable_income*Tax_rate_percent)/100
print('tax to be paid:',Tax)

#question:3
SID=int(input("Enter student SID:"))
Name=input("Enter student name:")
Gender=input("Gender of the student (F/M/U):")
Course_name=input("Enter Course name:")
Cgpa=float(input("enter Cgpa:"))
Student_list=[SID,Name,Gender,Course_name,Cgpa]
print (Student_list)

#question:4
a=int(input("Enter marks of 1st student:"))
b=int(input("Enter marks of 2nd student:"))
c=int(input("Enter marks of 3rd student:"))
d=int(input("Enter marks of 4th student:"))
e=int(input("Enter marks of 5th student:"))
Marks_list = [a,b,c,d,e]
Marks_list.sort()
print(Marks_list)

#question:5(a)
list =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list.pop(3)
print ("color",list)

#question:5(b)
List=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
List[3:5]=['Purple']
print ("color",List)


