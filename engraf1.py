import matplotlib.pyplot as plt

"""
select count(*) from player where 体重<70;　22人
select count(*) from player where 体重>=70 and 体重<=79; 206人
select count(*) from player where 体重>=80 and 体重<=89;　４００人
select count(*) from player where 体重>=90 and 体重<=99;　１８３人
select count(*) from player where 体重>=100;　５８人
"""


values = [22, 206, 400, 183, 58] # グラフ要素の値
labels = [                         # グラフ要素のラベル
    '70kg', '70-79kg', '80-89kg', '90-99kg', '100kg'
]
plt.pie(x=values,                  # グラフ要素の値を設定
        labels=labels,             # グラフ要素のラベルを設定
        autopct='%.2f%%')          # 構成割合として小数点以下2桁までをプロット
plt.axis('equal')                  # グラフを
plt.show()
