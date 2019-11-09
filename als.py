
# coding: utf-8

# In[53]:


import numpy as np
import os

n_users = 943
n_items = 1682
k = 100
lamba = 0.5
epoches = 50

R_data = np.zeros((n_users, n_items),dtype=np.int)
R_test = np.zeros((n_users, n_items),dtype=np.int)

with open("./ml-100k/u1.base") as f:
    for line in f.readlines():
        data = line.strip().split()
        R_data[int(data[0])-1][int(data[1])-1] = int(data[2])
        
with open("./ml-100k/u1.test") as f:
    for line in f.readlines():
        data = line.strip().split()
        R_test[int(data[0])-1][int(data[0])-1] = int(data[2])
        
P_user = np.random.random((n_users, k))
Q_item = np.random.random((n_items, k))
#P_user = np.zeros((n_users, k))
#Q_item = np.zeros((n_items, k))

for epoch in range(epoches):
    for i in range(n_users):
        Q_star = np.zeros(k)
        R_star = []
        for j in range(n_items):
            if(R_data[i][j]>0):
                Q_star = np.row_stack((Q_star, Q_item[j]))
                R_star.append(R_data[i][j])
        Q_star = Q_star.reshape((-1,k))
        if Q_star.shape[0] > 0:
            Q_star = Q_star[1:,:]
            R_star = np.array(R_star)
            e = np.identity(k)
            #print(np.dot(np.linalg.inv(np.dot(Q_star.transpose(), Q_star) + lamba * e), Q_star.transpose()))
            P_opt = np.dot(np.dot(np.linalg.inv(np.dot(Q_star.transpose(), Q_star) + lamba * e), Q_star.transpose()), R_star.transpose())
            for j in range(k):
                P_user[i][j] = P_opt[j]
    
    for j in range(n_items):
        P_star = np.zeros(k)
        R_star = []
        for i in range(n_users):
            if(R_data[i][j]>0):
                P_star = np.row_stack((P_star, P_user[i]))
                R_star.append(R_data[i][j])
        P_star = P_star.reshape((-1,k))
        if P_star.shape[0] > 0:
            P_star = P_star[1:,:]
            R_star = np.array(R_star)
            e = np.identity(k)
            Q_opt = np.dot(np.dot(np.linalg.inv(np.dot(P_star.transpose(), P_star) + lamba * e), P_star.transpose()), R_star.transpose())
            for i in range(k):
                Q_item[j][i] = Q_opt[i]
    
    R_predict = np.dot(P_user, Q_item.transpose())
    diff = R_data - R_predict
    Lvalidation = np.sum(np.dot(diff, diff.transpose()))
    print(Lvalidation)


# In[49]:


import numpy as np
x = np.zeros(2)
y = np.array([3,4])
xy = []
xy.append(x)
xy.append(y)
print(xy)
z = np.array(xy)
print(z)

