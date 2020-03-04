import numpy as np
import os
from matplotlib import pyplot as plt

n_users = 943
n_items = 1682
k = 10
lamda = 0.5
epoches = 30

R_data = np.zeros((n_users, n_items))
R_test = np.zeros((n_users, n_items))

losses = []

with open("./ml-100k/u1.base") as f:
    for line in f.readlines():
        data = line.strip().split()
        R_data[int(data[0])-1][int(data[1])-1] = data[2]
        
with open("./ml-100k/u1.test") as f:
    for line in f.readlines():
        data = line.strip().split()
        R_test[int(data[0])-1][int(data[0])-1] = data[2]
        
P_user = np.random.random((n_users, k))
Q_item = np.random.random((n_items, k))

for epoch in range(epoches):
    P_user = np.dot(R_data, np.dot(np.linalg.inv(np.dot(Q_item.T, Q_item) + lamda), Q_item.T).T)
    Q_item = np.dot(R_data.T, np.dot(np.linalg.inv(np.dot(P_user.T, P_user) + lamda), P_user.T).T)

    R_predict = np.dot(P_user, Q_item.transpose())

    diff = 0
    for i in range(R_test.shape[0]):
        for j in range(R_test.shape[1]):
            if R_test[i, j] != 0:
                diff += (R_test[i, j] - R_predict[i, j]) ** 2

    Lvalidation = diff / (n_users * n_items)
    losses.append(Lvalidation)

fig, ax = plt.subplots()
ax.plot(losses)
plt.show()