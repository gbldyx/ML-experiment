from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
import numpy as np

X_data, y_data = load_svmlight_file("housing_train.txt")
X_train, X_very, y_train, y_very = train_test_split(X_data, y_data, train_size=0.66)

X_train = X_train.A
X_very = X_very.A

X_train = np.column_stack((X_train, np.ones(X_train.shape[0])))
X_very = np.column_stack((X_very, np.ones(X_very.shape[0])))

w = np.zeros(X_train.shape[1])

loss = 0.5*np.dot(((y_train - np.dot(X_train, w))),(y_train - np.dot(X_train, w))) / X_train.shape[0]

x_pinv = np.linalg.pinv(X_train)

w_opt = np.dot(x_pinv, y_train)

loss_train = 0.5*np.dot(((y_train - np.dot(X_train, w_opt))),(y_train - np.dot(X_train, w_opt))) / X_train.shape[0]

loss_val = 0.5*np.dot(((y_very - np.dot(X_very, w_opt))),(y_very - np.dot(X_very, w_opt))) / X_very.shape[0]

print("loss: ", loss)
print("loss_train: ", loss_train)
print("loss_val: ", loss_val)

