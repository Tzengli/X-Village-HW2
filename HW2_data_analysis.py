#以2010~2015年高雄市各月份登革熱染病人數進行氣候與登革熱感染人數關係之研究
#total_j之j代表月份
#y2010~y2015為各年份登革熱每月感染人數List

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import json

url = 'https://od.cdc.gov.tw/eic/Age_County_Gender_061.json'
r = requests.get(url)
r.encoding = 'utf-8'
data=json.loads(r.text)
# data2=json.dumps(data, ensure_ascii=False, indent=4)
y2010 = []
y2011 = []
y2012 = []
y2013 = []
y2014 = []
y2015 = []

print('2010年1~12月各月份登革熱感染人數統計:')
for j in range(1,13):
    total = 0
    for i in range(len(data)):
        if data[i]["縣市"]== "高雄市" and int(data[i]["發病年份"]) == 2010 and int(data[i]["發病月份"]) == j:
            #print(data[i]['確定病例數'])
            total = total + int(data[i]["確定病例數"])    
    y2010.append(total)
    print("total_",j,' = ',total,sep = '',end = ',')
print()
print('='*50)    

print('2011年1~12月各月份登革熱感染人數統計:')
for j in range(1,13):
    total = 0
    for i in range(len(data)):
        if data[i]["縣市"]== "高雄市" and int(data[i]["發病年份"]) == 2011 and int(data[i]["發病月份"]) == j:
            #print(data[i]['確定病例數'])
            total = total + int(data[i]["確定病例數"])   
    y2011.append(total)         
    print("total_",j,' = ',total,sep = '',end = ',')    
print()
print('='*50)    

print('2012年1~12月各月份登革熱感染人數統計:')
for j in range(1,13):
    total = 0
    for i in range(len(data)):
        if data[i]["縣市"]== "高雄市" and int(data[i]["發病年份"]) == 2012 and int(data[i]["發病月份"]) == j:
            #print(data[i]['確定病例數'])
            total = total + int(data[i]["確定病例數"]) 
    y2012.append(total)           
    print("total_",j,' = ',total,sep = '',end = ',') 

print()
print('='*50)    

print('2013年1~12月各月份登革熱感染人數統計:')
for j in range(1,13):
    total = 0
    for i in range(len(data)):
        if data[i]["縣市"]== "高雄市" and int(data[i]["發病年份"]) == 2013 and int(data[i]["發病月份"]) == j:
            #print(data[i]['確定病例數'])
            total = total + int(data[i]["確定病例數"]) 
    y2013.append(total)           
    print("total_",j,' = ',total,sep = '',end = ',') 

print()
print('='*50)    

print('2014年1~12月各月份登革熱感染人數統計:')
for j in range(1,13):
    total = 0
    for i in range(len(data)):
        if data[i]["縣市"]== "高雄市" and int(data[i]["發病年份"]) == 2014 and int(data[i]["發病月份"]) == j:
            #print(data[i]['確定病例數'])
            total = total + int(data[i]["確定病例數"])  
    y2014.append(total)          
    print("total_",j,' = ',total,sep = '',end = ',') 

print()
print('='*50)    

print('2015年1~12月各月份登革熱感染人數統計:')
for j in range(1,13):
    total = 0
    for i in range(len(data)):
        if data[i]["縣市"]== "高雄市" and int(data[i]["發病年份"]) == 2015 and int(data[i]["發病月份"]) == j:
            #print(data[i]['確定病例數'])
            total = total + int(data[i]["確定病例數"])    
    y2015.append(total)        
    print("total_",j,' = ',total,sep = '',end = ',')    

print()
print('='*50)     

def display(year):
    for i in range(len(year)):
        print("%6d"%year[i],end='')
    print('')

# display(y2010)
# display(y2011)
# display(y2012)
# display(y2013)
# display(y2014)
# display(y2015)


###畫出2010~2015年高雄市各月份登革熱感染人數表格

dict = {'2010': y2010,'2011':y2011,'2012':y2012,'2013':y2013,'2014':y2014,'2015':y2015}
monthindex1 = [1,2,3,4,5,6,7,8,9,10,11,12]
frame_1 =  pd.DataFrame(dict,index = monthindex1)
print(frame_1)


##繪製2013年登革熱疫情各月份分佈圓餅圖
##因為前6個月人數較少故將之加總作比較

labels = ('First 6 months','July','August','September','October','November','December')
m6t_2013 = (y2013[0]+y2013[1]+y2013[2]+y2013[3]+y2013[4]+y2013[5]) 
y13 = (m6t_2013,y2013[6],y2013[7],y2013[8],y2013[9],y2013[10],y2013[11])
plt.pie(y13 , labels = labels,autopct='%1.1f%%')
plt.legend(["Year2013"], loc=2)
plt.title('Dengue pie chart')
plt.show()

##繪製2014年登革熱疫情各月份分佈圓餅圖
##因為前6個月人數較少故將之加總作比較

m6t_2014 = (y2014[0]+y2014[1]+y2014[2]+y2014[3]+y2014[4]+y2014[5]) 
y14 = (m6t_2014,y2014[6],y2014[7],y2014[8],y2014[9],y2014[10],y2014[11])
plt.pie(y14 , labels = labels,autopct='%1.1f%%')
plt.legend(["Year2014"], loc=2)
plt.title('Dengue pie chart')
plt.show()

##繪製2015年登革熱疫情各月份分佈圓餅圖
##因為前6個月人數較少故將之加總作比較

m7t_2015 = (y2015[0]+y2015[1]+y2015[2]+y2015[3]+y2015[4]+y2015[5]) 
y15 = (m7t_2015,y2015[6],y2015[7],y2015[8],y2015[9],y2015[10],y2015[11])
plt.pie(y15 , labels = labels,autopct='%1.1f%%')
plt.legend(["Year2015"], loc=2)
plt.title('Dengue pie chart')
plt.show()


##繪製2013~2015年各月份登革熱疫情折線圖

plt.figure(figsize=(10, 2)) # 圖片尺寸 10*2
# 這一行能畫折線圖， linestyle是點的
plt.plot(monthindex1, y2013, color='blue', linewidth=2.0, linestyle=':')
plt.xlabel('Month')
plt.ylabel('Number of people infected')
plt.legend(["Year2013"], loc=2) # loc指的是legend要放的位置，loc=2是放在第二象限
plt.title('Dengue epidemic line chart')
plt.show() # 要把圖片顯示出來記得加這一行


plt.figure(figsize=(10, 2)) # 圖片尺寸 10*6
# 這一行能畫折線圖， linestyle是點的
plt.plot(monthindex1, y2014, color='blue', linewidth=2.0, linestyle=':')
plt.xlabel('Month')
plt.ylabel('Number of people infected')
plt.legend(["Year2014"], loc=2) # loc指的是legend要放的位置，loc=2是放在第二象限
plt.title('Dengue epidemic line chart')
plt.show() # 要把圖片顯示出來記得加這一行


plt.figure(figsize=(10, 2)) # 圖片尺寸 10*6
# 這一行能畫折線圖， linestyle是點的
plt.plot(monthindex1, y2015, color='blue', linewidth=2.0, linestyle=':')
plt.xlabel('Month')
plt.ylabel('Number of people infected')
plt.legend(["Year2015"], loc=2) # loc指的是legend要放的位置，loc=2是放在第二象限
plt.title('Dengue epidemic line chart')
plt.show() # 要把圖片顯示出來記得加這一行


##繪製2013~2015年各月份登革熱疫情直方圖

year2013
plt.style.use('ggplot')
plt.bar(monthindex1,y2013,align = 'center')
plt.xlabel('Month')
plt.ylabel('Number of people infected')
plt.legend(['Year2013'], loc = 2)
plt.title('Dengue histogram chart')
plt.show()

# year2014
plt.style.use('ggplot')
plt.bar(monthindex1,y2014,align = 'center')
plt.xlabel('Month')
plt.ylabel('Number of people infected')
plt.legend(['Year2014'], loc = 2)
plt.title('Dengue histogram chart')
plt.show()

# year2015
plt.style.use('ggplot')
plt.bar(monthindex1,y2015,align = 'center')
plt.xlabel('Month')
plt.ylabel('Number of people infected')
plt.legend(['Year2015'], loc = 2)
plt.title('Dengue histogram chart')
plt.show()

  