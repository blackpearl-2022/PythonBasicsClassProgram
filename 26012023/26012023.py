#stack operations
size=int(input("enter the size:"))
stk=[]#empty list
top=0

def push(element):
    global top
    print("push-insert a value")
    if(top>=size):
        print("stack is full")
    else:
        stk.append(element)
        top+=1
def pop():
    global top
    if(top<=0):
        print("stack is empty")
    else: stk.pop()
    top-=1
def display():
    print("elements in stack")
    for i in range(0,top):
        print(stk[i])
n=1
while(n!=0):
    option=int(input("enter the function 1.push, 2.pop, 3.display"))
    if(option==1):
        element=int(input("enter the element: "))
        push(element)
    elif(option==2):
        pop()
    elif(option==3):
        display()
    else:
        print("invlaid option")
    n=int(input("press 0 to exit | 1 to continue.."))

    