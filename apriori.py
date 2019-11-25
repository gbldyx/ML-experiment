
# coding: utf-8

# In[5]:


x = [0,1,3,4,65,3]
for i in set(x):
    print(type(i))
#print(set(x))


# In[11]:


import numpy as np

test_d = [[3,4],[3,5,6],[3,5],[8],[6,1],[1,3]]

def freq_set_support(dataset, item_set, min_support):
    item_freq = {}
    support = {}
    freq_sets = set()
    n_trans = len(dataset)
    
    for item in item_set:
        for tran in dataset:
            if item.issubset(set(tran)):
                if item not in item_freq:
                    item_freq[item] = 0
                item_freq[item] += 1
    
    for item in item_freq:
        sup = item_freq[item] / n_trans
        if sup >= min_support:
            freq_sets.add(item)
            support[item] = sup
    
    return freq_sets, support

def generate_ck(item_sets, k):
    freq_sets = set()
    n_sets = len(item_sets)
    item_list = list(item_sets)
    
    for i in range(n_sets):
        for j in range(i+1, n_sets):
            l1 = list(item_list[i])
            l2 = list(item_list[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]:
                freq_item = item_list[i] | item_list[j]
                freq_sets.add(freq_item)
    
    return freq_sets
                

def apriori(dataset, min_support, max_items=None):
    n_trans = len(dataset)
    #item_support = {}
    c1 = set()
    
    for tran in dataset:
        for item in tran:
            #item_set = set(item)
            if item not in c1:
                c1.add(frozenset([item]))
                #item_support[item_set] = 0
            #item_support[item_set] += 1
    
    fs, sp = freq_set_support(dataset, c1, min_support)
    c2 = generate_ck(fs, 2)
    #print(sl)
    #print(sp)
    print(c2)

apriori(test_d, 0)

