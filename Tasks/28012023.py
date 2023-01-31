# # # 1.Check if a list contains an element
# lst=(1,2,3,4,5,6,7,8,9,10)
# i=int(input("enter the element to check:- "))
# if i in lst:
#     print("the element is in the list") 
# else:
#     print("element not found")
   

#Remove duplicates from a list2
# lst=[]
# n=int(input("enter the range for lst:- "))
# for i in range(0,n):
#     if n!=0:
#         ele=int(input("enter the elements for list:- "))
#         lst.append(ele)
#     else:
#         print("enter diffrent range")
#     break
# print("Orginal list" ,lst)
# dup=list(set(lst))
# print("after removing duplicates:- ",dup)

#Concate two lists
# lst1=[]
# lst2=[]
# n=int(input("enter the range for lst:- "))
# for i in range (0,n):
#     ele1=int(input("enter the elements for list-1:- "))
#     lst1.append(ele1)
#     ele2=int(input("enter the elements for list-2:- "))
#     lst2.append(ele2)
# print("first list is",lst1)
# print("second list is",lst2)
# for t in lst2:
#     lst1.append(t)
# print ("The list after concate is:- ", lst1)

# 4.Find length of list
# lst=[1,2,3,4,5]
# print("The list is :- ",lst)
# l=len(lst)
# print (l)

# lst=[]
# t=int(input("enter 1 to enter element, 0 after completing entering:- "))
# if t==1:
#     for i in range:
#         element=int(input("enter the elements for list:- "))
#         lst.append(element)
#         break
# else:
#     print("stop")


# 5.Remove elements in a list at a specific index
# lst=[]
# n=int(input("enter the range for lst:- "))
# for i in range(0,n):
#     ele=int(input("enter the elements for list:- "))
#     lst.append(ele)
# print ("The List is:- ", lst)
# t=int(input("Enter the index number to remove:- "))
# if t<=(n-1):
#     del lst[t]
#     print ("The List after removing element is:- ", lst)
# else:
#     print("The index is greater than the range")


# 6.Sort a list of integers in ascending order
# lst=[]
# n=int(input("enter the range for lst:- "))
# for i in range(0,n):
#     ele=int(input("enter the elements for list:- "))
#     lst.append(ele)
# print ("The List is:- ", lst)
# lst.sort()
# print("the sorted list is :- ", lst)



# 7.Get the first element from each nested list
# lst=[]
# n=int(input("enter the range for lst:- "))
# for i in range (0,n):
#     lst1=[]
#     ele=lst1
#     m = int(input("enter the range for nested list:- "))
#     for i in range (0,m):
#         ele=int(input("enter the elements for list:- "))
#         lst1.append(ele)
#     print(lst1)
#     lst.append(lst1[0])
# print("The First element of the nested list is:- ", lst)

# 8.Use a list as a stack
lst=[]
n=int(input("enter the limit for stack:- "))
for i in range (0,n):
    ele=int(input("enter the elements for stack:- "))
    lst.append(ele)
for i in lst:
    global n
    i=n
    print (lst[i])
