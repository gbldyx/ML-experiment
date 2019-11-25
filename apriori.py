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
                

def apriori(dataset, min_support, max_len=None):
    #n_trans = len(dataset)
    #item_support = {}
    set_len = 2
    item_set = set()
    freq_set = []
    supports = {}
    
    for tran in dataset:
        for item in tran:
            #item_set = set(item)
            if item not in c1:
                item.add(frozenset([item]))
                #item_support[item_set] = 0
            #item_support[item_set] += 1
    
    c1, support1 = freq_set_support(dataset, c1, min_support)
    freq_set.append(c1)
    supports.update(support1)
    
    print(freq_set)
    print(support1)
    
    if max_len == None:
        max_len = float('inf')
        
    while set_len <= 3:
        ci = generate_ck(freq_set[-1], set_len)
        fs, sp = freq_set_support(dataset, ci, min_support)
        
        if fs:
            freq_set.append(fs)
            supports.update(sp)
            set_len += 1
        else:
            break
    #c2 = generate_ck(fs, 2)
    #print(sl)
    #print(sp)
    #print(c2)
    return freq_set, supports

fs, sp = apriori(test_d, 0)
print(fs)
print(sp)
