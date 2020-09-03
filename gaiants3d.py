import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 3D描画を行うために必要なライブラリです
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('giantsdata.csv')#
shisyo     = np.array
shisyo     = df.values
height=[]
weight=[]
nenpo=[]
for s in shisyo:
    #print(s[3])#巨人用
    height.append(s[4])
    weight.append(s[5])
    nenpo.append(s[6])

print(height)
print(weight)
print(nenpo)
# Figureオブジェクトを作成します
fig = plt.figure(figsize=(9, 9))
# サブプロットaxを作成します
ax  = fig.add_subplot(1, 1, 1, projection="3d")
# X,Y,Zを1次元に変換します
x = np.ravel(height)
y = np.ravel(weight)
z = np.ravel(nenpo)
# 3D散布図を作成してください
ax.scatter3D(x, y, z)
plt.show()
print("end")
