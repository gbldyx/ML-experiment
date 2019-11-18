
# coding: utf-8

# In[ ]:


import math

#COREPT = 'core'
#BORDERPT = 'border'
#NOISEPT = 'noise'
minPts = 10
eps = 40

sample_pts = []
class point(object):
    def __init__(self, index):
        #self.Class = None
        self.is_visited = False
        self.label = -1
        self.index = index
        self.nhbr = []

def calc_distance(data, index):
    ret_dist = []
    for i in range(data.shape[0]):
        dist = 0
        for ftr in range(data.shape[1]):
            dist += math.abs(data[i][j] - data[index][j])
        ret_dist.append(dist)
    return ret_dist

def find_nhbr(data):
    for i in range(data.range[0]):
        pt = point(i)
        pts_dist = calc_distance(data, i)
        pt.nhbr = [x[0] for x in enumerate(pst_dist)]
        sample_pts.append(pt)
        
def dbscan(data):
    for pt in sample_pts:
        if pt.is_visited:
            continue
        if len(pt.nhbr) >= minPts:
            pt.is_visited = True
            pt.label = pt.index
            nhbrs = pt.nhbr.copy()
            while len(nhbrs) > 0:
                nb_pt = sample_pts[nhbrs[0]]
                if not nb_pt.is_visited :
                    nb_pt.is_visited = True
                    #nb_pt.label = pt.label
                    if len(nb_pt.nhbr) >= minPts:
                        #nb_pt.Class = COREPT
                        for nb_nb_pt in nb_pt.nhbr:
                            if nb_nb_pt not in nhbrs:
                                nhbrs.append(nb_nb_pt)
                if nb_pt.label == -1:
                    nb_pt.label = pt.label
                nhbrs = nhbrs[1:]
        else:
            pt.Class = NOISEPT


# In[ ]:


s = [3,4,8,2,6]
for i in s:
    print(i)
    if len(s) == 15:
        break
    s.append（i+100）

