'''
                # WHILE LOOP
print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
print("7")
print("8")
print("9")
print("10")

        #Print 1 to 100
i = 1
while(i<=100):
    print(i)
    i+=1

        #Print 100 to 1 
i = 100
while(i>0):
    print(i)
    i-=1

        #Print 100 - 1 even number
i=100
while(i>=0):
    if i%2!=0:
        print(i, end=" ")
    i-=1

        #Sum of first 5 natural numbers
i = 1
sum = 0
while(i<=5):
    sum += i
    i+=1
print(sum)

        #Sum of first 100 even number
i=1 
sum=0
while(i<=100):
    if i%2 ==0:
        sum+=i
    i+=1

print(sum)

        #Product of first 100 natural odd numbers
i=1
prod=1
while(i<=100):
    if i%2!=0:
        prod*=i
    i+=1
print(prod)
                    # FOR LOOP

        #Print from 1 to 100
for i in range(1,101):
    print(i)

    
        #Print 100 to 1
for i in range(100,0,-1):
    print(i)


        #Print even numbers
for i in range(1,101):
    if i%2==0:
        print(i, end=" ")

        
        #Sum of even numbers 
sum = 0
for i in range(1,101):
    if i%2==0:
        sum+=i
    i+=1
print(sum)


        #Product of Odd numbers
prod=1
for i in range(1,101):
    if i%2 != 0:
        prod*=i
print(prod)


        # 1 4 9 16
str=1
num= int(input("Enter the series : "))
for i in range(1,num):
    i=i*i
    print(i)


        # 1 2 4 7 11
number= int(input("Enter the series : "))
num=1
for i in range(number):
    num=num + i
    print(num)


        #3 6 9 12 
num=int(input("Enter the num : "))
for i in range(1,num):
    num=3*i
    print(num, end=",")

        #4 8 16 32
num=int(input("Enter the Series limit : "))
for i in range(2,num+2):
    res=2**i
    print(res)

    
        #1.5 3.0 4.5 6.0
num=int(input("Enter the seriws limit : "))
for i in range(1,num+1):
    res= i + (0.5)*i
    print(res)

    
        #1 9 25 49
num=int(input("Enter series : "))
for i in range(1,(2*num),2):
    res= i**2
    print(res)


        #4 16 36 64
num=int(input("Enter series limt : "))
for i in range(1,num+1):
    res= i*i*4
    print(res)

        #0 3 8 15 
num=int(input("Enter the limit: "))
a=0
print(a)
for i in range(3,(2*num),2):
    res= a + i
    print(res)
    a=res

    
        # 0 7 26 63
num=int(input("Enter a number : "))
for i in range(1,num+1):
    sum = (i**3)-1
    print(sum)

    
        #2 5 10 17
num=int(input("Enter the limit: "))
a=2
print(a)
for i in range(3,(2*num),2):
    res= a + i
    print(res)
    a=res

    
        #24 99 224 399
num=int(input("Enterthe serie : "))
for i in range(5,(num*5)+1,5):
    res=(i**2)-1
    print(res)
    

    # Counting in a number
num=int(input("enter number : "))
count=0
while(num>0):
    num=num//10
    count+=1
print(count)


    # Reverse of a Number
num=1234
while(num>0):
    rev = num%10
    num= num//10
    print(rev,end="")

    # OR

num=int(input("Enter the num : "))
rev = 0
while(num>0):
    rem = num%10
    rev = rev*10+rem
    num= num//10
print(rev)


        #Prime number
num = 46
check_prime=True
for i in range(2,num):
    if num%i==0:
        check_prime = False
        break
if check_prime==True:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")  

    
        # Prime number printing 
count = 0
sum = 0
prod = 1
for j in range(1,101):
    num = j
    check_prime=True
    for i in range(2,num):
        if num%i==0:
            check_prime = False
            break
    if check_prime==True:
        count+=1
        sum+=num
        prod*=num
        print(num, end=" ")
print()
print("The total number of prime number :", count)
print("The sum of prime number :", sum)
print("The product of prime number :", prod)




        #Armstrong
num=int(input("Enter a number : "))
count=0
a=num
b=num
sum=0
while(num>0):
    num= num//10
    count+=1
while(a>0):    
    rem= a % 10
    sum= sum + rem**count
    a= a // 10
if b==sum:
    print(b,"is Armstrong Number")
else:
    print(b,"is not an Armstrong Number")

    
    #Printing Armstrong number
count=0
a_sum=0
product=1
for i in range(100,10000):
    num=i
    t1= num
    digit=0
    while(t1>0):
        t1//=10
        digit+=1
    t2=num
    sum=0
    while(t2>0):
        rem=t2%10
        sum=sum+rem**digit
        t2//=10
    if num==sum:
        print(num,end=" ")
        count+=1
        a_sum+=num
        product*=num
print()         
print(count)
print(a_sum)
print(product)


for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


num=5
for i in range(num):
    for j in range(i,5):
        print(" ",end="")
        for k in range(1,j+1):
            print(i)

num=int(input("Enter the seriws limit : "))
for i in range(1,num+1):
    res= i + (0.5)*i
    print(res, end=" ")


#SRTING 
name= "laddha"
first_index=0
middle_index=len(name)//2
last_index= len(name)-1

print(name[first_index])
print(name[middle_index])
print(name[last_index])

print(name[0])
print(len(name))


    #STRING SLICING
#s[start_from : end_at : straight or reverse]
s = input("Enter a name : ")
rev=s[::-1]
if rev==s:
    print("Palindrome")
else:
    print("Not Palindrome")

# first question
s="JhonDipPeta"
ans=s[4:7]
print(ans)

#Second Question
s1= "Ault"
s2= "Kelly"
ans=s1[0:2]+s2[:]+s1[2:4]
print(ans)

#Third Question
s1="America"
s2="Japan"
middle_1=len(s1)//2
last_1=len(s1)-1
last_2=len(s2)-1
middle_2=len(s2)//2

ans=s1[0]+s2[0]+s1[middle_1]+s2[middle_2]+s1[last_1]+s2[last_2]
print(ans)

#4th Question
s1="Jmaes"
middle=len(s1)//2
last=len(s1)-1
ans=s1[0]+s1[middle]+s1[last]
print(ans)


#Reversing a string without using slicing
s="python is a programming language"
last=len(s)-1
for i in range(last,-1,-1):
    print(s[i],end="")

#Counting each Letter in the String
s = "python is a programming language"
letter_count = {}

for letter in s:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

for letter, count in letter_count.items():
    print(f"Letter {letter} = {count}")

'''
























