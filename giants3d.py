import numpy as np
import matplotlib.pyplot as plt
# 3D�`����s�����߂ɕK�v�ȃ��C�u�����ł�
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('giantsdata.csv')#
shisyo     = np.array
shisyo     = df.values
height=[]
weight=[]
nenpo=[]
for s in shisyo:
    #print(s[3])#���l�p
    height.append(s[4])
    weight.append(s[5])
    nenpo.append(s[6])
"""
print(height)
print(weight)
print(nenpo)
"""
# Figure�I�u�W�F�N�g���쐬���܂�
fig = plt.figure(figsize=(9, 9))
# �T�u�v���b�gax���쐬���܂�
ax  = fig.add_subplot(1, 1, 1, projection="3d")
# X,Y,Z��1�����ɕϊ����܂�
x = np.ravel(height)
y = np.ravel(weight)
z = np.ravel(nenpo)
# 3D�U�z�}���쐬���Ă�������
ax.scatter3D(x, y, z)
