import numpy as np
import matplotlib.pyplot as plt
# 3D描画を行うために必要なライブラリです
from mpl_toolkits.mplot3d import Axes3D
#%matplotlib inline

t = np.linspace(-2*np.pi, 2*np.pi)
X, Y = np.meshgrid(t, t)
Z = np.array((X+Y)*(X+Y))

# Figureオブジェクトを作成します
fig = plt.figure(figsize=(9,9))
# サブプロットaxを作成してください
ax  = fig.add_subplot(1, 1, 1, projection="3d" )
# プロットして表示します
ax.plot_surface(X, Y, Z)
plt.show()


