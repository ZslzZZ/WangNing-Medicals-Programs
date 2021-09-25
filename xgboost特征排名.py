#这个是以全部数值化好了的数据来进行程序
from numpy import loadtxt
from xgboost import XGBClassifier
from xgboost import plot_importance
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
dataset = pd.read_excel('./4.xlsx')
# split data into X and y
X = dataset.iloc[:,0:-1]
y = dataset.iloc[:,-1]
# fit model no training data
model = XGBClassifier()
model.fit(X, y)
# feature importance
print(model.feature_importances_)
# plot
plot_importance(model,max_num_features = 20,height = 0.5)
plt.show()
