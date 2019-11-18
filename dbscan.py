
# coding: utf-8

# In[ ]:


import math

COREPT = 'core'
BORDERPT = 'border'
NOISEPT = 'noise'
minPts = 10
eps = 40

sample_pts = []
class point(object):
    def __init__(self, index):
        self.Class = None
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
        if pt.label != -1 or pt.Class == NOISEPT:
            continue
        if len(pt.nhbr) >= minPts:
            pt.Class = COREPT
            pt.label = pt.index
            for nb in pt.nhbr:
                sample_pt = sample_pts[nb]
                sample_pt.label = pt.label
                if len(sample_pt.nhbr) >= minPts:
                    sample_pt.Class = COREPT
                    for nb_nb in sample_pt.nhbr:
                        spt_nb_nb = sample_pts[nb_nb]
                        if spt_nb_nb.label == -1:
                            spt_nb_nb.label = pt.label
                            spt_nb_nb.Class = BORDERPT
                else:
                    sample_pt.Class = BORDERPT
        else:
            pt.Class = NOISEPT


# In[ ]:


docker
k8s
mymatris
oracle
spring

