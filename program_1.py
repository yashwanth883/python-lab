#!/usr/bin/env python
# coding: utf-8

# In[2]:


m1 = int(input("Enter marks for test 1 : "))
m2 = int(input("enter marks for test 2 : "))
m3 = int(input("Enter the marks for test 3 : "))

if m1 <= m2 and m1 <= m3:
  avgMarks = (m2 +m3)/2
elif m2<= m1 and m2<=m3:
  avgMarks = (m1+m3)/2
elif m3 <= m1 and m3<= m2: 
  avgMarks = (m1+m2)/2
print("the average is ", avgMarks)
    
    


# In[3]:


type(avgMarks)


# In[21]:


val = int(input("Enter the sequence of numbers"))
str_val = str(val)
if(str_val == str_val[::-1]):
 print("Palindrome")
else:
 print("Not a palindrome")
for i in range(10):
  if str_val.count(str(i))>0:
   print(str(i), "appears", str_val.count(str(i)),"times");   

