from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from scipy import sparse
import numpy as np
import random

X_data, y_data = load_svmlight_file("C:/Users/Administrator/Desktop/housing.txt")
X_train, X_very, y_train, y_very = train_test_split(X_data, y_data, train_size=0.5)

X_train = X_train.A
X_very = X_very.A

X_train = np.column_stack((X_train, np.ones(X_train.shape[0])))
X_very = np.column_stack((X_very, np.ones(X_very.shape[0])))

w = np.zeros(X_train.shape[1])
#w = np.random.randn(X_train.shape[1])
n = 0.2
times = 1

while times<=500:
	row = random.randint(0,X_train.shape[0]-1)
	X_random_row = X_train[row]
	y_random_row = y_train[row]
	#graf = -1 * np.dot(X_random_row.T,y_random_row) + np.dot(np.dot(X_random_row.T,X_random_row),w)
	for i in range(w.shape[0]):
		w[i] = w[i] + n * ( y_random_row - np.dot(X_random_row, w)) * X_random_row[i] / X_train.shape[0]
		#print(w[i])
	#w = w - n * graf
	loss_train = 0.5*np.dot((y_train - np.dot(X_train, w)),(y_train - np.dot(X_train, w))) / X_train.shape[0]
	loss_val = 0.5*np.dot(((y_very - np.dot(X_very, w)).transpose()),(y_very - np.dot(X_very, w))) / X_very.shape[0]
	print(loss_train)
	print(loss_val)
	print('\n')
	times = times + 1

"""
loss = 0.5*np.dot(((y_train - np.dot(X_train, w))),(y_train - np.dot(X_train, w))) / X_train.shape[0]

x_pinv = np.linalg.pinv(X_train)

x_pi = np.dot(np.linalg.inv(np.dot(X_train.transpose(),X_train)), X_train.transpose())

w_opt = np.dot(x_pinv, y_train)

loss_train = 0.5*np.dot(((y_train - np.dot(X_train, w_opt))),(y_train - np.dot(X_train, w_opt))) / X_train.shape[0]

loss_val = 0.5*np.dot(((y_very - np.dot(X_very, w_opt))),(y_very - np.dot(X_very, w_opt))) / X_very.shape[0]

print(loss)
print(loss_train)
print(loss_val)
"""