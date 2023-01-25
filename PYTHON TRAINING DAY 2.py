#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input("ENTER A NUMBER:"))
if(n>0 and n<20):
    if(n%2==0):
        print("WEIRD NUMBER")
    else:
        print("NORMAL NUMBER")
elif((n>=20) and (n<30)):
    print("NORMAL NUMBER")
else:
    if(n>=30):
        if(n%2!=0):
            print("NORMAL NUMBER")
        else:
            print("WEIRD NUMBER")
    


# In[5]:


a=list('12345')
print(a)


# In[6]:


b=map(int,a)
print(b)


# In[7]:


b=list(map(int,a))
b


# In[8]:


# printing squares of elements in the given string/numbers.
n='123'
n_1=int(n[0])
print(n_1**2)
n_2=int(n[1])
print(n_2**2)
n_3=int(n[2])
print(n_3**2)


# In[9]:


s='123'
for i in range(len(s)):
    print(int(s[i])**2)


# In[12]:


a={1,2,3,4}
b={3,4,5,6}
d=a.difference(b)
d


# In[13]:


a.add(5)
a


# In[14]:


# TO CHECK WHETHER GIVEN NUMBER IS EVEN OR ODD
n=int(input("ENTER A NUMBER:"))
if(n%2==0):
    print("%d is even" %(n))
else:
    print("%d is odd" %(n))


# In[19]:


n=int(input())
if(n==1):
    print("neither prime nor composite")
elif(n==2):
    print("%d is prime" %(n))
else:
    for i in range(2,n):
        if(n%i==0):
            print("%d is not a prime" %(n))
            break
        else:
            print("%d is a prime" %(n))
            break


# In[20]:


n=int(input("ENTER A NUMBER:"))
if(n==1):
    print("SUNDAY")
elif(n==2):
    print("MONDAY")
elif(n==3):
    print("TUESDAY")
elif(n==4):
    print("WEDNESDAY")
elif(n==5):
    print("THURSDAY")
elif(n==6):
    print("FRIDAY")
elif(n==7):
    print("SATURDAY")
else:
    print("INVALID")


# In[ ]:


size=int(input())
for i in range(size):
    print("*"*(size) + " "*(size-1))


# In[ ]:




