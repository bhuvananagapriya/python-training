#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#arrays
r=3
c=3
arr=[]
for i in range(r):
    element=[]
    for j in range(c):
        element.append((int(input("enter the element:"))))
    arr.append(element)

print(arr)


# In[2]:


print(arr)


# In[3]:


r=3
c=3
arr2=[]
for i in range(r):
    element=[]
    for j in range(c):
        element.append((int(input("enter the element:"))))
    arr2.append(element)

print(arr2)


# In[19]:


a=0
b=1
print(a)
print(b)
for x in range(9):
    r=a+b
    print(r)
    a,b=b,r


# In[2]:


s='bhuvana'
s.count('a')


# In[4]:


s.isalnum()


# In[9]:


first=" hello "
second= 2023
last=" welcome "
print( first + str(second) + last)


# In[12]:


num=3.14
print("the square is {:.5f}".format(num*num))


# In[ ]:


a=int(input())
b=int(input())
c=a-b
print(c)


# In[ ]:


a=int(input())
b=int(input())
try:
    print(a/b)
    
except:
    print("b cannot be 0")
    print("after the error")


# In[ ]:


a=int(input("enter value"))
b=int(input("enter value"))
try:
    print(a/b)
except:
    print("b cannot be 0")
print(a+b)
print(a-b)
print(a*b)


# In[8]:


try:
    a=list(map(int,input("enter the numbers:").split(' ')))
    print(a)
except:
    print("enter integer number ")


# In[6]:


n=int(input())
for i in range(n):
    print(i)


# In[13]:


def addition(num1,num2):
    #function body
    result=num1+num2
    return result
print(addition(10,20))  
#print(addition(10))  generates error 


# # ways to check prime number:
# #method 1
# #for i in range(1,num+1) #23 interations
#      #pass
#     
#     
#     # method 2
#     # for i in range(2,num): # 21 iterations
#     #pass
#           
#         # method 3
#         # for i in range(2,num//2): # only 10 iterations   2nd most efficient way
#             #pass
#             
#             # method 4
#             # for i in range(2,int(num**0.5)+1): #only 3 iterations
#                # pass

# In[17]:


a=int(input("enter value"))
b=int(input("enter value"))
try:
    print(a/b)
except:
    print("b cannot be 0")
print(a+b)
print(a-b)
print(a*b)


# In[ ]:




