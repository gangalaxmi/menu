
# coding: utf-8

# In[1]:

names = "samba,Anil,Rajesh,Ashok,Sudhakar"
names[0]="names123"


# In[2]:

for i in names:
    print i


# In[3]:

name = "samba"


# In[4]:

names  = ['samba','Anil','Rajesh','Ashok']


# In[5]:

names[0]


# In[6]:

names[-1]


# In[7]:

names[:3]


# In[9]:

names[-3:]


# In[10]:

names[::-1]


# In[11]:

names[::2]


# In[12]:

n=[12,12.34,"python",[1,2,3,4],{1:2,3:4},(1,2,3,4)]


# In[13]:

s="pyton program"
s[1:5]


# In[14]:

s[10:1]


# In[16]:

s[12]


# In[17]:

s[13]


# In[18]:

s[14:2]


# In[19]:

s[10:1]


# In[20]:

names


# In[21]:

names[10]


# In[22]:

names[10:]


# In[23]:

names


# In[24]:

names[0]="python"


# In[25]:

names


# In[26]:

l=[1,2,3,4]
l1=l


# In[27]:

l


# In[28]:

l1


# In[29]:

l[0]=10


# In[30]:

l


# In[31]:

l1


# In[32]:

l=[1,2,3,4]
l1=[1,2,3,4]
l[0]=100


# In[33]:

l


# In[34]:

l1


# In[35]:

l=[1,2,3,4,[10,20,30,40]]


# In[36]:

l[-1]


# In[37]:

l=[10,20,30,40]


# In[38]:

len(l)


# In[39]:

l=[1,2,3,[10,20,30,40]]
len(l)


# In[40]:

l[-1]


# In[41]:

l[-1][1]


# In[42]:

l[-1]=10


# In[43]:

l


# In[44]:

l=[1,2,3,4,[10,20,30,40]]


# In[45]:

l[-1][-1]


# In[46]:

l[-1][2:4]


# In[47]:

l[-1][-1]=400


# In[48]:

l


# In[49]:

l=['a','b','c','d']
l1=['e','f','g','h']
print l+l1


# In[50]:

print l+"python"


# In[51]:

print l+2


# In[52]:

print l+(1,2,3)


# In[53]:

l


# In[54]:

l+['e']


# In[55]:

l


# In[56]:

l1=l+['e']


# In[57]:

l=l+['e']


# In[58]:

l=[1,2,3,4]


# In[59]:

id(l)


# In[61]:

l=l+['e']


# In[62]:

id(l)


# In[ ]:




# In[63]:

l=[10,20,30,40]


# In[64]:

l


# In[65]:

l=l+[50]


# In[66]:

l


# In[67]:

l=l-[50]


# In[68]:

a=10


# In[69]:

del a


# In[70]:

print a


# In[71]:

l


# In[72]:

del l


# In[73]:

print l


# In[74]:

l=[10,20,30,40]


# In[75]:

del l[-1]


# In[76]:

l


# In[77]:

l=[10,20,30,40]
id(l)


# In[78]:

del l[0]


# In[79]:

l


# In[80]:

id(l)


# In[81]:

l[0]


# In[82]:

l


# In[83]:

del l[-2:]


# In[84]:

l


# In[85]:

l=[10,20,30,40]


# In[ ]:

l = l[1:3]+[50]


# In[87]:

l[1:3]+[50]


# In[88]:

l=l[0:2]+[50]+l[2:]


# In[89]:

l


# In[90]:

'''
1.insert
2.update
3.delete
4.search
5.quit
'''


# In[91]:

l=[10,20,30,40]
a=40
for i in l:
    print i


# In[92]:

l=[10,20,30,40]
a=20
for i in l:
    if i == a:
        print "value is there"


# In[93]:

l=[10,20,30,40]
a=1100
for i in l:
    if i == a:
        print "value is there"


# In[94]:

l=[10,20,30,40]
a=20
for i in l:
    if i == a:
        print "value is there"
        break


# In[95]:

l=[10,20,30,40]


# In[96]:

l.append(50)


# In[97]:

l


# In[98]:

l=[10,20,30,40]
print id(l)
l = l+[50]
print id(l)


# In[101]:

l=[10,20,30,40]
print id(l)
l.append(50)
print id(l)


# In[102]:

s="python"
s.replace('p','z')
print s


# In[103]:

l=[1,2,3,4]
l.append(5)
print l


# In[104]:

s="python"
s1=s.replace('p','z')
print s
print s1


# In[106]:

l=[1,2,3,4]
l1=l.append(5)
print l
print l1


# In[107]:

def replace(s):
    return s
def append(l):
    l


# In[108]:

l=['p1','p2','p3']
l1=l.append('p4')
for i in l1:
    print i


# In[109]:

l


# In[110]:

l.append(12)


# In[111]:

l


# In[112]:

l.append([10,203,30])


# In[113]:

l


# In[114]:

l.append()


# In[115]:

a=''
l.append(a)


# In[116]:

l


# In[117]:

a=None


# In[118]:

l.append(a)


# In[119]:

l


# In[120]:

l=[10,20,30,40]
max(l)


# In[121]:

min(l)


# In[122]:

sum(l)


# In[123]:

max([10,'abc',20,23.45])


# In[124]:

sum([10,'abc',20,23.45])


# In[125]:

sum(['a','b','c','d'])


# In[126]:

sum([10,20,304])


# In[127]:

sum([10.23,34])


# In[128]:

"bac">20


# In[129]:

l=[10,20,30,40]


# In[130]:

l.extend([100,200,300])


# In[131]:

l


# In[132]:

l=[1,2,3,4]
l.append('python')


# In[133]:

l


# In[134]:

l.extend("python")


# In[135]:

l


# In[136]:

l.append(10)


# In[137]:

l.extend("10")


# In[138]:

l


# In[139]:

l.extend(10)


# In[140]:

for i in 10:
    print i


# In[141]:

s="python"
l=[1,2,3,4]
for i in s:
    l.append(i)
l


# In[142]:

l=[10,20,30,40]
l1=[50,60,70]
l.extend(l1)


# In[143]:

l


# In[144]:

l.append(l1)


# In[145]:

l


# In[146]:

l=[1,2,3,4]
print id(l)
l.extend([10,20,30,4])
print id(l)


# In[147]:

l=['a','b','c','d']
l.insert(2,"python")


# In[148]:

l


# In[149]:

l.insert(-1,"345")


# In[150]:

l


# In[151]:

l.insert(20,"345")


# In[152]:

l


# In[153]:

l.index('345')


# In[154]:

l=[10,20,30,40]


# In[155]:

l.index(30)


# In[156]:

l=['a','b','a','a','c','d','a']
l.index('a')


# In[157]:

# findout an nth occurnace index in a list or string


# In[158]:

l.index('1000')


# In[159]:

l


# In[161]:

l=[10,20,30,10,30,40,50,60,40,50,60]
l.count(10)


# In[162]:

l=[10,20,30,10,30,40,50,60,40,50,60]
for i in l:
    if l.count(i)>1:
        print i
    


# In[163]:

l=[10,20,30,10,30,40,50,60,40,50,60]
unique = []
for i in l:
    if l.count(i)>1:
        unique.append(i)
unique


# In[164]:

40 in l


# In[165]:

l=[10,20,30,10,30,40,50,60,40,50,60]
uniqu = []
for i in l:
    if i not in uniqu:
        uniqu.append(i)
uniqu
    


# In[168]:

l=[10,20,30,10,30,40,50,60,40,50,60,20,30,40,50]
for i in l:
    if i not in uniqu:
        uniqu.append(i)
for i in uniqu:
    if l.count(i)>1:
        print i,l.count(i)
    


# In[169]:

# take a list, ask the user to enter element. check whrther that element repeated or not
l=['a','A','python','PyThon']
inp = raw_input("Enter a value:")
if l.count(inp)>1:
    print "Elemt repeated"
else:
    print "Not repeated"


# In[170]:

# take a list, ask the user to enter element. check whrther that element repeated or not
l=['a','A','python','PyThon']
inp = raw_input("Enter a value:")
inp = inp.upper()
if l.count(inp)>1:
    print "Elemt repeated"
else:
    print "Not repeated"


# In[ ]:



