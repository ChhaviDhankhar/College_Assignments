#question 1

s=input("enter the string: ")
k=s[::-1]
print("reverse of entered string is\n",k)

#question 2

l_lim=int(input("lower limit of the range= "))
u_lim=int(input("upper limit of the range= "))
d=int(input("enter number to divide "))

for i in range(l_lim,u_lim):
    if i%d==0:
        print(i)

    else:
         continue
        
#question 3

a = int(input("Enter the length of side 1:"))
b = int(input("Enter the length of side 2:"))
c = int(input("Enter the length of side 3:"))

if (a+b>c and b+c>a and c+a>b):
    s = (a+b+c)/2
    area =  math.sqrt(s*(s-a)(s-b)(s-c))
    print(area)
elif (a+b<=c or b+c<=a or c+a<=b):
    print("Triangle can't be formed!!")
    
  #question 4
    
    n = 5
for i in range(n):
    for j in range(i):
        print("* ", end="")
    print("")

for i in range(n,0,-1):
    for j in range(i):
        print("* ", end="")
    print("")
    
 #question 5
    
    print("ANS.5")
row=int(input("Enter the number of rows"))
n=0

for i in range(0,row+1):
      
      for j in range(i): 
            if n==26:
                n=0 
            else:
                pass
            y=chr(65+n) 
            print(y, end="")
            n+=1
      print("")
      
  #question 6
      
      lower_limit = int(input("Enter the lower limit of the range:"))
upper_limit = int(input("Enter the upper limit of the range:"))

for i in range(lower_limit,upper_limit+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
            
            
   #question 7
    
    for i in range(1,501):
    if (i%7 == 0) and (i%11 == 0):
        print(i)
    else:
        continue
        
        
      #question 8
  for i in n_list:
    if i>=0:
        pos_list.append(i)
    elif i<0:
        neg_list.append(i)


    for j in n_list:
         if j%2==0:
            even_list.append(j) 
         else:
            odd_list.append(j)

          
print("List of Positive Numbers: ", pos_list)
print("List of Negative Numbers: ", neg_list)
print("List of Even Numbers: ", even_list) 
print("List of odd numbers: ", odd_list)  


#question 9

user_list = input("Enter the list of words seperated by comma(,):")

word_list = user_list.split(",")

counts = dict()

for word in word_list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
  
    
