#!/usr/bin/env python
# coding: utf-8

# In[18]:


lst=[1,2,3,4]
k=4
for i in range(0,len(lst)):
    if(k==lst[i]):
        print(i)
        break
else:
    print("not found")


# In[16]:


l=[]
for i in range(0,10):
    l.append(i)
print(l)


# In[19]:


l=[x for x in range(10)]
print(l)


# In[21]:


l=[num for num in range(11) if num%2==0]   # list comprehension
print(l)


# In[23]:


l=[num for num in range(1,101) if num%7==0 or num%11==0]
print(l)


# In[24]:


l=[num for num in range(1,101) if num%7==0 and num%11==0]
print(l)


# In[42]:


l=[1,2,3,4,5]
for i in range(len(l)-1,-1,-1):
    print(l[i])


# In[60]:


l=[-1,2,4,7,-3,-5]
sum=0
for i in range(1,len(l)):
    if(l[i]>0):
        temp=l[i]
        sum=sum+temp
print(sum)    


# In[1]:


N=int(input())

    l2.reverse()
for i in range(len(l)):
    res=l[i]^l2[i]
    print(*res)  


# In[ ]:




