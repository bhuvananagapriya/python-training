#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Student:
    name="bhuvana"
    roll_number="18"
    branch="aiml"
    marks=0
    attendance=0.0
    is_using_transport=False
    def view_attendance(self):        #self doesnot always want to accept any argument 
        pass
    def view_marks(self):
        pass
    def view_name(self):
        pass
    def update_name(self,new_name):
        pass


# In[6]:


#constructors are used to provide defs1=ault values /initial values for variable object
class Student:
    def __init__(self,name):
        print("object created")
        print(name)
s1=Student("bhuvana")   # here we are not calling any method but object is created


# In[8]:


class Student:
    student_name="no name"
    def __init__(self,name):
        print("object created")
        print(name)
        print(self.student_name)
s1=Student("bhuvana") 


# In[13]:


class Student:
    student_name="no name"
    def __init__(self,name):
        self.student_name=name
s1=Student("bhuvana")
s2=Student("naga")
s3=Student("priya")
print(s1.student_name)
print(s2.student_name)
print(s3.student_name)


# In[16]:


#program to raotate a array for k rotations
n=int(input())
if(n<=0):
    print("Invalid Input")
else:
    arr=list(map(int,input().split()))
    k=int(int(input()))
    if(k>n):
        print("Invalid Input")
    else:
        first=arr[:n-k]
        last=arr[n-k:]
        res=last+first
        print(res)
        print(*res)


# In[17]:


#program to print the count of pairs whose sum is eqaul to given k value from a array
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
res=[]
for i in range(0,n-1):
    for j in range(i+1,n):
        if(arr[i]+arr[j]==k):
            res.append([arr[i],arr[j]])
#print(res)
ans=[]
for i in res:
    if i not in ans:
        ans.append(i)
print(len(ans))


# In[3]:


#Login System   this is user class
class UserClass:
    full_name=""
    email=""
    __password=""
    mobile_number=""
    def __init__(self,name,email,password):
        self.full_name=name
        self.email=email
        self.password=password
    def update_name(self,new_name):
        self.full_name=new_name
    def get_name(self):
        return self.full_name
    """ setter method for private variable password"""
    def update_password(self,new_password):
        pass
    def update_mobile_number(self,new_number):
        pass
    """ getter method for private variable password"""
    def get_user_password(self):
        return self.__password


# In[5]:


from User import UserClass

class Login:
    __db=[]
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("Welcome user")
        print("1.Register")
        print("2.Login")
        print("3.Exit")
    def create_user(self,name,email,password):
        new_user=User(name,email,password)
        self.__db.append(new_user)
    def validate_user(self,email,password):
        pass
    
obj=Login()
while True:
    option=input("Enter your choice:")
    if(option=='1'):
        name=input("Enter your full name:")
        email=input("Enter your email:")
        password=input("Enter your password:")
        res=obj.create_user(name,email,password)
        if(res==True):
            print("user object created")
    elif(option=='2'):
        pass
    elif(option=='3'):
        pass
    else:
        print("Invalid Input")
        


# # INHERITANCE
# #single level inheritance

# In[8]:


class A:
    name="bhuvana"
    age=6
class B(A):
    color="blue"
    
obj=B()
print(obj.name)  
print(obj.age)


# In[ ]:


#example for multilevel inheritance
class 
    


# In[9]:


#hierarical inheritance
class Person:
    name=""
    gender=""
    
class Student(Person):
    roll_number=""
    branch=""

class Faculty(Person):
    

class VC(Person):


# In[ ]:


class Phones:
    size=""
    comp

class realme(Phones):

class redmi(Phones):

class apple(Phones):


# In[12]:


class A:
    def m1(self):
        print("this is parent 1")
class B:
    def m1(self):
        print("this is parent 2")
class C(A,B):
    pass
obj=C()
print(obj.m1())
    


# In[ ]:


#hybrid inheritance
class Restaurant:
    
class veg_food:
    
class non_veg_food:

class passenger:


# In[18]:


from random import random,randint
a=randint(1,100)
id=random()+1000
print(id)
a


# In[21]:


#creation of rock paper scissor game
from random import random,randint
choice=['rock','paper','scissor']
print("1.Rock\n2.Paper\n3.Scissor")
com_choice=randint(1,3)
if(com_choice=='choice[0]'):
    print("")

    


# In[24]:


print("1->Rock\n")
print("2->Paper\n")
print("3->Scissor")
user_choice=int(input("Enter a number:"))
if user_choice==1:
    item="Rock"
if user_choice==2:
    item="Paper"
if user_choice==3:
    item="Scissor"
comp_choice=randint(1,3)
if user_choice==comp_choice:
    print("Draw")
elif user_choice>=comp_choice:
    print("paper")


# In[3]:


#polymorphism
class A:
    def method(self,a,b):
        print("Sum of two numbers:",a+b)
class B(A):
    def method(self,a,b):
        print("multiplication of two numbers:",a*b)
ob=B()
ob.method(10,20)


# In[7]:


#polymorphism     # METHOD OVERLOADING   COMPILE TIME POLYMORPHISM
class A:
    def method(self,a,b):
        print("Sum of two numbers:",a+b)
class B(A):
    def method(self,a,b):
        print("multiplication of two numbers:",a*b)
    def method(self,abc):
        print("Value is ",abc)
ob=B()
ob.method(10,20)                 #error is geenrated because of function overriding
                                 #when 2 same methods are present in the same class the latest method in 
                                 #the memory will be executed rather than the first method


# In[9]:


class A:
    def method(self,a,b):
        print("Sum of two numbers:",a+b)
class B(A):
    def method(self,a,b):
        print("multiplication of two numbers:",a*b)
    def method(self,abc):
        print("Value is ",abc)
ob=B()
ob.method(10)   #here we have no error because the method is called for lastest method


# In[ ]:


from random import randint
choice=['rock','paper','scissor']
p_score=0
c_score=0
limit=5
while p_score!=limit and c_score!=limit:
    print(f"enter among the folloowing",choice)
    my_ch=input("Player choice:").lower()
    if my_ch not in choice:
        print("invalid input")
        continue
    sys_ch=choice[int(randint(0,2))]
    print(f"System choice: {sys_ch}")
    if my_ch==sys_ch:
        print("Draw")
        continue
    if my_ch=="rock" and sys_ch=="scissor":
        p_score+=1
    elif my_ch=="paper" and sys_ch=="rock":
        p_score+=1
    elif my_ch=="scissor" and sys_ch=="paper":  
        p_score+=1
    else:
        c_score+=1
    print(f"your score: {p_score},system score: {c_score}")
    
    
if p_score>c_score:
    print("you win the match")
else:
    print("system wins the match")


# In[4]:


#method overriding   --------->  same method same signatures but in different classes
class A:
    def m1(self):
        print("in class A")
class B:
    def m1(self):
        print("in class B")
obj=B()


# In[2]:


#same method name but different signatures  is method overloading


# In[9]:


#example for method overriding
class Animal:
    def speak(self):
        print("every animal speaks")
class Dog(Animal):
    def speak(self):
        print("Barks")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Cow(Animal):
    def speak(self):
        print("amba")
obj=Cow()
sound=Dog()
sound.speak()
obj.speak()


# In[10]:


#ANNOTATIONS ARE USED TO DEFINE ABOUT WHAT THE METHOD IS DOING
#IT IS STARTED WITH THE SYMBOL @


# In[ ]:





# # ABSTRACTION

# In[16]:


from abc import ABC,abstractmethod

class Area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass                   #in abstarct class the method body is not written in the  abstarct class
class Square(Area):
    def calculate_area(self):
        print("in square method")
class Rectangle(Area):
    pass
obj=Square()
obj.calculate_area()


# In[ ]:




