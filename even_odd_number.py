#!/usr/bin/env python
# coding: utf-8

# #Write a Python program to count the number of even and odd numbers from a series of numbers.
# 
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# 
# Expected Output :
# 
# Number of even numbers : 4
# 
# Number of odd numbers : 5

# In[4]:


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = 0
odd_count = 0
index = 0
while index < len(numbers):
    num = numbers[index]
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    index += 1
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)


# In[ ]:




