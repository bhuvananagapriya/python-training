#!/usr/bin/env python
# coding: utf-8

# In[1]:


N=int(input())
l=[]
l2=[]
for i in range(N):
    ele=int(input())
    l.append(ele)
    l2.append(ele)
    l2.reverse()
for i in range(len(l)):
    print(l[i]^l3[i])


# In[16]:


l=[1,2,3,4]
l.reverse()
l


# In[12]:


print("",l.reverse())


# In[ ]:



n1=int(input())
n2=int(input())
op=input()
if(op=='^'):
    print(n1^n2)
if(op=='&'):
    print(n1&n2)
if(op=='|'):
    print(n1|n2)
if(op=='!'):
    print("!n1")


# In[ ]:


N=int(input())
l=[]
l2=[]
for i in range(N):
    l.append(ele)
    l2.append(ele)
    l2.reverse()
for i in range(len(l)):
    res=l[i]^l2[i]
    print(*res)    


# In[ ]:


n1=int(input())
n2=int(input())
print(n1^n2)


# In[ ]:


def invert(string):
    res=""
    for i in string:
        if i=='0':
            res +='1'
        else:
            res +='0'
    return res
a=5
b=7
op='^'
new_a=bin(a)[2:]
new_b=bin(b)[2:]
new_a=invert(new_a)
new_b=invert(new_b)
print(new_a,new_b)
print(int(new_a,2))

