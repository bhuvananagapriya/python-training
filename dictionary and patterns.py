#!/usr/bin/env python
# coding: utf-8

# In[1]:


student_details={}
student_details.update({1:"bhuvana"})
student_details.update({2:"naga"})
student_details.update({3:"priya"})


# In[5]:


print(student_details[1])


# In[5]:


print(student_details)


# In[6]:


for i in student_details:
    print(student_details[i])


# In[6]:


print(student_details.get(3))


# In[19]:


n=int(input())
for i in range(0,n):
    print("*"*(n))


# In[14]:


n=int(input())
for i in range(1,n+1):
    print(i*"*")


# In[17]:


n=int(input())
for i in range(0,n+1):
    print(((n-i)*"*"))


# In[20]:


lst=[1,2,3,4]
for i in lst:
    print(i**2)


# In[ ]:


lst=[1,2,3,4]
k=int(input())
for i in range(len(lst)):
    if(lst[i]=k):
        print("%d" %(i))
    else:
        print("not found")


# In[ ]:


d={}
l=[]
for i in range(2):
    key1:input()
    key2:input()
    l.append(d)
print(l)


# In[ ]:




