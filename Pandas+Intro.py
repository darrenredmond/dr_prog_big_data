
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd


# In[4]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[5]:

s


# In[6]:

s.index


# In[7]:

pd.Series(np.random.randn(5))


# In[8]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[9]:

d


# In[17]:

ds = pd.Series(d)
ds.median()


# In[11]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[12]:

s


# In[13]:

s[0]


# In[14]:

s[:3]


# In[15]:

s[s > s.median()]


# In[18]:

s[[4, 3, 1]]


# In[19]:

np.exp(s)


# In[20]:

s['a']


# In[21]:

s['e'] = 12.


# In[22]:

s


# In[25]:

if 'f' in s:
    s['f']


# In[27]:

if 'e' in s:
    print(s['e'])


# In[28]:

'e' in s


# In[29]:

'f' in s


# In[30]:

s.get('f')


# In[31]:

s.get('e')


# In[32]:

s.get('f', np.nan)


# In[33]:

s + s


# In[35]:

s * 3


# In[36]:

s[1:]


# In[37]:

s[:-1]


# In[38]:

s[1:] + s[:-1]


# In[39]:

s['f'] = 0


# In[40]:

s


# In[41]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
   'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[43]:

d


# In[44]:

df = pd.DataFrame(d)


# In[45]:

df


# In[46]:

pd.DataFrame(d, index=['d', 'b', 'a'])


# In[47]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])


# In[48]:

df.index


# In[49]:

df.columns


# In[50]:

d = {'one' : [1., 2., 3., 4.],
   'two' : [4., 3., 2., 1.]}


# In[51]:

d


# In[52]:

pd.DataFrame(d)


# In[53]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[54]:

data


# In[55]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[56]:

data


# In[57]:

pd.DataFrame(data, index=['first', 'second'])


# In[59]:

my_data = pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[60]:

my_data['C']


# In[61]:

my_data['B']


# In[64]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[65]:

pd.DataFrame(data2)


# In[66]:

pd.DataFrame(data2, index=['first', 'second'])


# In[67]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[68]:

df


# In[69]:

df['one']


# In[70]:

df['three'] = df['one'] * df['two']


# In[71]:

df


# In[72]:

df['flag'] = df['one'] > 2


# In[73]:

df


# In[74]:

del df['two']


# In[80]:

three = df.pop('three')
three


# In[81]:

three


# In[82]:

df


# In[83]:

df['foo'] = 'bar'


# In[84]:

df


# In[85]:

df['one_trunc'] = df['one'][:2]


# In[86]:

df.insert(1, 'bar', df['one'])

df['bar'] = df['one']


# In[87]:

df


# In[ ]:



