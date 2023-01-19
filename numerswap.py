num1=int(input("input first numer:"))  # input first number
num2=int(input("input second numer:")) # input second number
print("first number is",num1,",", "second number is",num2)
#swaping with 3rd variable
temp=num1
num1=num2
num2=temp
print("after swaping num1 is",num1,"and num2 is",num2)
#swap without 3rd variable
num2=num1+num2
num1=num2-num1
num2=num2-num1
print("after swaping again num1 is ", num1,"and num2 is " ,num2)
