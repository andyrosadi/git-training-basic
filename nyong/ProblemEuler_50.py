#!/usr/bin/env python
# coding: utf-8

# ### PROBLEM 50

# In[1]:


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
selisih = 0
bilterbesar = 0
bilterakhir = len(bilprima)

for i in range(len(bilprima)):
    for j in range(i+selisih, bilterakhir):
        hasiljumlah = sum(bilprima[i:j])
        if hasiljumlah < 1000000:
            if hasiljumlah in bilprima:
                selisih = j-i
                bilterbesar = hasiljumlah
        else:
            bilterakhir = j+1
            break

print (bilterbesar)


# In[ ]:




