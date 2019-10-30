from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
import numpy as np
import random
import math
import matplotlib.pyplot as plt

X_train, y_train = load_svmlight_file("a9atrain.txt")
X_test, y_test = load_svmlight_file("a9a.t")

X_train = X_train.A
X_test = X_test.A

X_train = np.column_stack((X_train, np.ones(X_train.shape[0])))
X_test = np.column_stack((X_test, np.ones(X_test.shape[0])))

w = np.zeros(X_train.shape[1])

n = 0.001
times = 1
batch_size = 50
c = 1.0
loss = []

fig=plt.figure()
ax=fig.add_subplot(111)

while times<=500:
    Lvalidation = 0
    for i in range(0,batch_size):
        row = random.randint(0,X_train.shape[0]-1)
        if(i==0):
            X_batch = np.array(X_train[row])
            y_batch = np.array(y_train[row])
        else:
            X_batch = np.row_stack((X_batch,X_train[row]))
            y_batch = np.row_stack((y_batch,y_train[row]))

    w_tmp=w.copy()

    for i in range(X_train.shape[1]):
        g=0
        for j in range(batch_size):
            if 1-y_batch[j]*np.dot(w_tmp, X_batch[j]) >=0:
                g+=(-(y_batch[j]*X_batch[j][i]))
        g /= batch_size
        if i == X_train.shape[1]-1:
            w[i] = w[i] - n*g*c
        else:
            w[i] = w[i] - n*(w[i] + g*c)
   
    for i in range(X_test.shape[0]):
        Lvalidation += max(0, 1-y_test[i]*(np.dot(w, X_test[i])))

    times += 1
    Lvalidation = Lvalidation*c/X_test.shape[0] + 0.5*(np.dot(w[:-2],w[:-2]))
    loss.append(Lvalidation)

ax.plot(loss)
plt.show()
