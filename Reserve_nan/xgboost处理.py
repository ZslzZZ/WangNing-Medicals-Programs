#以未数值化的数据来处理
from numpy import loadtxt
from xgboost import XGBClassifier
from xgboost import plot_importance
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
df = pd.read_excel('./result1.xlsx')
dataset = df.loc[:, (df != df.iloc[0]).any()] #去除所有值相同的列
# split data into X and y
X = dataset.iloc[:,0:-1]
X = pd.get_dummies(X)
y = dataset.iloc[:,-1]
# fit model no training data
model = XGBClassifier()
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.30, random_state = 7)
#fit model no training data
model.fit(X_train, y_train)
#make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# feature importance
print(model.feature_importances_)
#evaluate predictions
accuracy = accuracy_score(y_test,predictions)
print('Accuracy: %.2f%%' %(accuracy * 100.0))
# plot
plot_importance(model,max_num_features = 20,height = 0.5)
plt.show()
