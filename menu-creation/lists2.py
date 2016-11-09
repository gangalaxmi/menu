
# coding: utf-8

# In[1]:

l=['a','A','python','PyThon']
l.pop(0)


# In[2]:

l


# In[3]:

l.pop()


# In[4]:

l


# In[5]:

l.pop(10)


# In[6]:

l


# In[7]:

l.insert(20,"abc")


# In[8]:

l


# In[9]:

l.pop(20)


# In[10]:

l.pop()


# In[11]:

l


# In[12]:

l.remove('A')


# In[13]:

l=['a','b','c','a','d','e']
l.remove('a')


# In[14]:

l


# In[15]:

l=['a','b','c','a','d','e']
for i in l:
    l.remove('a')


# In[16]:

l.remove('a')


# In[17]:

l=['a','b','c','d']
l.remove('z')


# In[19]:

l=['a','b','c','a','d','e']
for i in l:
    print l
    print "iter"
    l.remove('a')


# In[22]:

l=['a','b','c','a','d','e',10,20,30,40,50,50]
for i in l:
    print l
    print "iter"
    if 'a' in l:
        l.remove('a')


# In[23]:

l=['a','b','c','a','d','e',10,20,30,40,50,50]
for i in l:
    print l
    print "iter"
    if 'a' in l:
        l.remove('a')
    else:
        break


# In[ ]:



