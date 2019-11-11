
# coding: utf-8

# In[ ]:


import math
import numpy as np

LEAF = 'leaf'
INTER = 'internal'
class Tree:
    def __init__(self, node_type, label=None, feature=None):
        self.node_type = node_type
        self.label = label
        self.feature = feature
        self.dict = {}
    
    def add_tree(self, key, tree):
        self.dict[key] = tree
    
    
def split_dataset(dataset, feature, value):
    ret_dataset = []
    for sample in dataset:
        if sample[feature]==value:
            ret_sample = sample[:feature]
            ret_sample.extend(sample[feature+1:])
            ret_dataset.append(ret_sample)
    return ret_dataset

def calc_Shannon_entropy(dataset):
    n_samples = len(dataset)
    label_cnt = {}
    for sample in dataset:
        label = sample[0]
        if label not in label_cnt.keys():
            label_cnt[label] = 0
        label_cnt[label] +=1
    Shannon_entropy = 0
    for key in label_cnt:
        p = float(label_cnt[key]) / n_samples
        Shannon_entropy -= p * math.log(p, 2)
    return Shannon_entropy

def calc_SplitInfo(dataset, feature):
    n_samples = len(dataset)
    feature_classes = {}
    values = dataset[:, feature]
    for v in values:
        if v not in feature_classes.keys():
            feature_classes[v] = 0
        feature_classes[v] += 1
    split_info = 0
    for key in feature_classes:
        p = feature_classes[key] / n_samples
        split_info -= p * math.log(p, 2)
    return split_info

def calc_feature_entropy(dataset, feature):
    n_samples = len(dataset)
    feature_classes = {}
    values = dataset[:, feature]
    for v in values:
        if v not in feature_classes.keys():
            feature_classes[v] = 0
        feature_classes[v] += 1
    feature_entropy = 0
    for key in feature_classes:
        sub_set = split_dataset(dataset, feature, key)
        p = feature_classes[key] / n_samples
        se = calc_Shannon_entropy(sub_set)
        feature_entropy += p * se
    return feature_entropy

def build_tree(dataset):
    labels = set(dataset[:, 0])
    if len(labels) == 1:
        return Tree(LEAF, label = labels.pop())
    
    max_igr = 0
    max_feature = 0
    for ftr in range(n_features):
        igr = calc_Shannon_entropy(dataset) - calc_feature_entropy(dataset, ftr)
        spin = calc_SplitInfo(dataset, ftr)
        if spin != 0:
            igr = igr / spin
        if igr > max_igr:
            max_igr = igr
            max_feature = ftr
            
    tree = Tree(INTER, feature=max_feature)
    
    
    
    

