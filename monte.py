import matplotlib.pyplot as plt
import numpy as np
import math
import time 
#%matplotlib inline

np.random.seed(100)
X1 = 0 # 的に当たった回数です
X2  =0
# 試行回数Nを指定してください
N = 10000
# 四分円の境界の方程式[y=√(1-x^2)(0<=x<=1)]を描画しています
circle_x = np.arange(0, 1, 0.001)
circle_y = np.sqrt(1- circle_x * circle_x)
plt.figure(figsize=(5,5))
plt.plot(circle_x, circle_y) 

# N回の試行にかかる時間を計測します
start_time = time.clock() 

# N回の試行を行っています
for i in range(0, N):
    # 0から1の間で一様乱数を発生させ、変数score_xに格納してください
    score_x = np.random.rand()
    # 0から1の間で一様乱数を発生させ、変数score_yに格納してください
    score_y = np.random.rand()
    if  score_y -score_x * score_x  < 0:
        # 円内に入ったものは黒で表示させ、外れたものは青で表示させてください
        plt.scatter(score_x, score_y, marker='o', color='k')
        # 円内に入ったならば、上で定義した変数 X に 1 ポイント加算してください
        X1 = X1 + 1
    else:
        plt.scatter(score_x, score_y, marker='o', color='b')
        X2 = X2 + 1

# piの近似値をここで計算してください
pi = X1/(X1+X2)

# モンテカルロ法の実行時間を計算しています
end_time = time.clock() 
time = end_time - start_time

# 円周率の結果を表示してください
print("S:%.6f"% pi)
print("実行時間:%f" % (time))

# 結果を表示します
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()