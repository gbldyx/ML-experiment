from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
import numpy as np
import random
import matplotlib.pyplot as plt

X_data, y_data = load_svmlight_file("housing_train.txt")
X_train, X_very, y_train, y_very = train_test_split(X_data, y_data, train_size=0.66)

X_train = X_train.A
X_very = X_very.A

X_train = np.column_stack((X_train, np.ones(X_train.shape[0])))
X_very = np.column_stack((X_very, np.ones(X_very.shape[0])))

w = np.zeros(X_train.shape[1])

n = 0.6
times = 1
loss_train_list = []
loss_val_list = []

fig = plt.figure()
ax = fig.add_subplot(111)

while times<=500:
    row = random.randint(0,X_train.shape[0]-1)
    X_random_row = X_train[row]
    y_random_row = y_train[row]

    for i in range(w.shape[0]):
        w[i] = w[i] + n * ( y_random_row - np.dot(X_random_row, w)) * X_random_row[i] / X_train.shape[0]

    loss_train = 0.5*np.dot((y_train - np.dot(X_train, w)),(y_train - np.dot(X_train, w))) / X_train.shape[0]
    loss_val = 0.5*np.dot((y_very - np.dot(X_very, w)),(y_very - np.dot(X_very, w))) / X_very.shape[0]
    print("loss_train: ", loss_train)
    print("loss_val: ", loss_val)
    print('\n')
    loss_train_list.append(loss_train)
    loss_val_list.append(loss_val)
    times = times + 1

ax.plot(loss_train_list, color="red", label="loss_train")
ax.plot(loss_val_list, color="green", label="loss_val")
plt.legend(bbox_to_anchor=(1.0,1), loc=0, borderaxespad=0.1)
plt.show()
