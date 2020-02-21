#!/usr/bin/env python
# coding: utf-8

# ### PROBLEM 49

# In[1]:


from itertools import permutations

def bilanganprima(n):
    is_prima = [True]*n
    is_prima[0] = False
    is_prima[1] = False
    is_prima[2] = True
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prima[index] = False
            index = index+i
    prima = [2]
    for i in range(3, n, 2):
        if is_prima[i]:
            prima.append(i)
    return prima

def create(b):
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            diff = b[j] - b[i]
            if b[j] + diff in b:
                return str(b[i])+str(b[j])+str(b[j]+diff)
    return False

bilprima1 = bilanganprima(10000)
bilprima2 = [x for x in bilprima1 if x > 1487]

for i in bilprima2:
    p = permutations(str(i))
    a = [int(''.join(x)) for x in p]
    a = list(set([x for x in a if x in bilprima2]))
    a.sort()
    if len(a) >= 3:
        if create(a):
            print (create(a))
            break


# In[ ]:




