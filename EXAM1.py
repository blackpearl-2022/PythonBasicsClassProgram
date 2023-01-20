#1.Print First 10 natural numbers using while loop
# num=0
# while (num<10):
#     sum=num+1
#     print (sum)
#     num=num+1

#Count the total number of digits in a number using while loop
# num=int(input("Enter the number: ")) #123
# count=0
# while num!=0: #123!=0 | 12!=0 | 1!=0 | 0!=0 - false
#     num//=10 # num= 123//10 = 12| num= 12//10=1 | num= 1//10 = 0
#     count+=1 # count=0+1=1 | count=1+1=2 | count=2+1=3
# print(count) # print count = 3

#Display numbers from -10 to -1 using for loop
# for i in range (-10,0):     # i=-10         | i=-9
#     print(i)                # print -10     | i=-9
#                             # i=-10+1=-9    | i=-9+1

#Write a program to display all prime numbers within a range

# lower=int(input("enter the lower limit: "))
# upper=int(input("Enter the upper limnit: "))
#
# for i in range (lower,upper):
#     if i>1:
#             for n in range (2,i):
#                 if (i%n)==0:
#                     break
#             else:
#                 print (i)



#.Display Fibonacci series up to 10 terms using for loop

#Write a Python function to find the Max of three numbers.
# def max(a,b,c):
#     if a>b:
#         if a>c:
#             print (a, ":first number is greater")
#         else:
#             if c>a:
#                 print (c,": third number is greater")
#     else:
#         if b>c:
#             print (b,": second number is greater")
#         else:
#             print(c, ":third number is greater")
#
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# num3=int(input("Enter third number: "))
# max(num1,num2,num3)

#Write a Python function to calculate the factorial of a number
def fact(n):
    f=1
    for i in range (1,n + 1):
        f=f*i
    return(f)

num = int(input("Enter a number: "))
t=fact(num)
print(t)


