import numpy as np
import japanize_matplotlib 
import matplotlib.pyplot as plt

kokugo=[4,7,18,28,36,27,10,7]
syakai=[0,17,13,12,17,17,22,39]
sugaku=[8,19,17,23,16,18,17,19]


left = np.arange(len(kokugo))  # numpyで横軸を設定
label_x = ['100-90','89-80', '79-70','69-60', '59-50','49-40', '39-30','29-0'] 
width = 0.2
 
plt.bar(left, kokugo, color='r', width=width,label='国語', align='center')
plt.bar(left+width, syakai, color='b', width=width, label='社会',align='center')
plt.bar(left+width*2, sugaku, color='y', width=width, label='数学',align='center')
 
plt.xticks(left + width/3, label_x)
plt.legend(loc=2)
plt.show()