import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 讀入 csv 文字檔 UTF-8
print('****107年大專院校系別查詢****')
csv_file='http://stats.moe.gov.tw/files/detail/107/107_sdata.csv'
school= pd.read_csv(csv_file)
a=input('輸入科系名稱(如:資訊,電子):')
b=input('輸入日間進修別:D,N(D:日,N:進修):')
c=input('輸入體系別:1,2,3(1:一般,2:技職,3:師範):')
students=int(input('輸入學生人數(以上):'))
df1=school[(school['科系名稱'].str.contains(a))&(school['日間∕進修別'].str.contains(b))&(school['體系別'].str.contains(c))&(school['學生數'].astype(int)>=students)]
df1=df1.sort_values(by=['縣市名稱','學生數'],ascending=[True,False]) 
print(df1)

df2=df1.groupby('縣市名稱', as_index=False)['學校名稱'].count()
df2=df2.sort_values(by=['學校名稱'],ascending=[True]) 
#print(df2)
plt.figure(figsize=(9,12))    # 顯示圖框架大小
labels =df2['縣市名稱'] # 製作圓餅圖的類別標籤
size =df2['學校名稱']      # 製作圓餅圖的數值來源
plt.pie(size,                           # 數值
        labels = labels,                # 標籤
        autopct = '%1.1f%%',            # 將數值百分比並留到小數點一位
        #explode = separeted,            # 設定分隔的區塊位置
        pctdistance = 0.6,              # 數字距圓心的距離
        textprops = {'fontsize' : 12} # 文字大小
        #shadow=True  # 設定陰影
       )                    
plt.axis('equal')
plt.title('107年'+a+"相關科系各縣市分佈比例圖", {'fontsize' : 18})  # 設定標題及其文字大小
#plt.legend(loc = "best")   
plt.show()
