#!/usr/bin/env python
# coding: utf-8

# # Assignment no:1
# # String Functions

# In[97]:


str1 = 'I am a python developer'#  capitalize firt letter of a string
str1.capitalize()


# In[6]:


str1.title() # capitalize every first letter


# In[7]:


str1.isupper()# check whether every letter is upper or not?


# In[8]:


str1.islower()# check whether every letter is lower or not?


# In[9]:


str1.lower()# convert into lower case


# In[10]:


str1.upper()#convert into upper


# In[13]:


len(str1)# this function count overall length 


# In[14]:


str1.count('o')# count occurance of any specific letter


# In[17]:


str1="".join(reversed(str1))# reversed() function
print(str1)


# In[18]:


str1.split()


# In[5]:


str1="".join(reversed(str1))
print(str1)


# In[6]:


str1.swapcase()


# In[15]:


str1.center(27,'*')


# # List Functions

# In[21]:


lst = [10,'python',20,30,2.56,'hi']# to count length len(list name)
(len(lst))


# In[22]:


lst.count(4)# tocount specific occurences


# In[25]:


lst.index(20)#  this function specify index value of specific element


# In[26]:


lst.append('payal')# to add elements at the end of the list


# In[27]:


print(lst)


# In[28]:


lst.extend([80,67,'lkj'])
print(lst)


# In[31]:


lst.insert(4,[67,78])
print(lst)


# In[32]:


lst.pop(2)# remove 2nd index number valuelst


# In[34]:


lst.remove(30)# remove mention element
print(lst)


# In[35]:


lst.reverse()
print(lst)


# # Tuple Functions

# In[53]:


tup=(1,2,5,6,8,0)# all() function return false if tuple contain (o or false)
print(all(tup))


# In[51]:


print(any(tup)) #any() function returns true if any one element is true in the tuple.


# In[54]:


min(tup)


# In[55]:


max(tup)


# In[56]:


tup.index(5)#this function return index number ofperticular value mentioned.


# In[57]:


sum(tup)


# In[59]:


tup=list(tup)
print(tup)


# In[62]:


tup=tuple(tup)
print(tup)


# # Set Functions

# In[72]:


se={50,88,67,89,99,66,56,55,99}
print(se)


# In[74]:


se.add(8)
print(se)


# In[76]:


se.discard(8)
print(se)


# In[78]:


se1={7,5,5,6,6,8,6,4,3,4}
print(se1)


# In[79]:


se.isdisjoint(se1)# this function returns True if both are empty sets or if both sets contains non-matching elements.


# In[80]:


se.issubset(se1)


# In[82]:


se.issubset(se1)


# # Dictionary Functions

# In[90]:


dict={}
dict['name']='payal'
dict['age']=23
dict['a']=1
dict['z']=100
print(dict)


# In[92]:


dict.keys()


# In[93]:


dict.values()


# In[94]:


dict.get('name')#this function is used to get the value of specified key.


# In[95]:


tup=(1,2,3,4,5) #we can use tuple elements as keys in the dict and the elements must be unique
dict.fromkeys(tup)


# In[96]:


dict.items()#Items(): this function is used to get all items. All key and value pairs will be displayed in tuple format.


# In[ ]:




