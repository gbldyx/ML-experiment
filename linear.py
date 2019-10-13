from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from scipy import sparse
import numpy as np

X_data, y_data = load_svmlight_file("C:/Users/Administrator/Desktop/housing.txt")
X_train, X_very, y_train, y_very = train_test_split(X_data, y_data, train_size=0.67)

X_train = X_train.A
X_very = X_very.A
w = np.zeros(13)

loss = 0.5*np.dot(((y_train - np.dot(X_train, w)).transpose()),(y_train - np.dot(X_train, w)))

x_pinv = np.linalg.pinv(X_train)

x_pi = np.dot(np.linalg.inv(np.dot(X_train.transpose(),X_train)), X_train.transpose())

w_opt = np.dot(x_pinv, y_train)

loss_train = 0.5*np.dot(((y_train - np.dot(X_train, w_opt)).transpose()),(y_train - np.dot(X_train, w_opt)))

loss_val = 0.5*np.dot(((y_very - np.dot(X_very, w_opt)).transpose()),(y_very - np.dot(X_very, w_opt)))

print(loss)
print(loss_train)
print(loss_val)