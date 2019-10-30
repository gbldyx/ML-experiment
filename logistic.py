from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
import numpy as np
import random
import math

X_train, y_train = load_svmlight_file("a9atrain.txt")
X_test, y_test = load_svmlight_file("a9a.t")

X_train = X_train.A
X_test = X_test.A

X_train = np.column_stack((X_train, np.ones(X_train.shape[0])))
X_test = np.column_stack((X_test, np.ones(X_test.shape[0])))

y_train[y_train<0]=0
y_test[y_test<0]=0

w = np.zeros(X_train.shape[1])

n = 0.1
times = 1
batch_size = 50
loss = []

fig=plt.figure()
ax=fig.add_subplot(111)

while times<=300:
    Lvalidation = 0
    score = 0
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
        dl=0
        for j in range(batch_size):
            dl += (y_batch[j]-1/(1+math.exp(-1*np.dot(w_tmp, X_batch[j]))))*X_batch[j][i]
        dl /= batch_size
        w[i] = w[i] + n*dl
   
    for i in range(X_test.shape[0]):
        Lvalidation  += y_test[i]*math.log(1/(1+math.exp(-1*np.dot(w, X_test[i]))))+(1-y_test[i])*math.log(1-1/(1+math.exp(-1*np.dot(w, X_test[i]))))

    times += 1
    Lvalidation /= X_test.shape[0]
    loss.append(-Lvalidation)

ax.plot(loss)
plt.show()