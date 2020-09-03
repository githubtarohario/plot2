import sqlite3
import matplotlib.pyplot as plt
def kensaku():
    dbname='TestDB.db'
    conn=sqlite3.connect(dbname)
    select_sql = "select seireki,rate from rate"
    print(select_sql)
    c = conn.cursor()
    seireki=[]
    shityou=[]
    for row in c.execute(select_sql):
        print(row[0],"******",row[1])
        s1=row[0]
        s2=row[1]
        seireki.append(s1)
        shityou.append(s2)
    conn.close()
    return seireki,shityou
x1,y1=kensaku()
print(x1)
print(y1)




plt.title('rate %') # グラフのタイトル
plt.xlabel('Year')# X軸のラベル
plt.ylabel('rate %')# Y軸のラベル
marker='o'
line='--'
color='r'  # b:青 g:緑 r:赤 c:シアン m:マゼンダ y:黄 k:黒 w:白
fmt=marker + line + color
plt.plot(x1, y1, fmt, label = 'rate')# グラフデータの設定
plt.legend() # 凡例の表示
plt.show()   # グラフの表示
