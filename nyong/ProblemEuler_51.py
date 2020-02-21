#!/usr/bin/env python
# coding: utf-8

# ### PROBLEM 51

# In[1]:


from collections import Counter

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

bilprima = bilanganprima(1000000)
bilprima1 = [x for x in bilprima if len(str(x)) - len(set(str(x))) >= 3]

def ganti(s):
    s = str(s)
    hasil = []
    for duplicate in (Counter(s) - Counter(set(s))):
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        temp = [int(s.replace(duplicate, x)) for x in a]
        hasil.append(temp)
    return hasil

cek = []

def check(m):
    for i in m:
        cek.append(i)
        if i not in bilprima1:
            m.remove(i)
    return m

bil = True
i = 0

while bil:    
    if bilprima1[i] not in cek:
        replacements = ganti(bilprima1[i])
        for j in replacements:
            if len(check(j)) == 8:
                print (j[0])
                bil = False
                break
    i += 1


# In[ ]:




