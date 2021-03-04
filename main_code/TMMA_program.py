from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from pyodbc import ProgrammingError
import os
import datetime
import calendar
import matplotlib.ticker as ticker
from matplotlib import font_manager
import webbrowser
import time

global font,font1,ServerID,user,password,database,docpath

cpath=os.getcwd()
cpath=cpath+'\TMMAinfo.txt'

f= open(cpath)
lines=f.read().splitlines()

newlines=[]

for i in range(len(lines)):
    newlines.append(str(lines[i]))

ServerID=newlines[0].split("=")[1]
user=newlines[1].split("=")[1]
password=newlines[2].split("=")[1]
database=newlines[3].split("=")[1]
fontpath=newlines[5].split("=")[1]
docpath=newlines[6].split("=")[1]



font = FontProperties(fname=fontpath, size=12)
font1 = FontProperties(fname=fontpath, size=9)
my_font = font_manager.FontProperties(fname=fontpath)
#連接SQL
try:
    connect='DRIVER={SQL Server};SERVER='+ServerID+';DATABASET='+database+';UID='+user+';PWD='+password
    cnxn = pyodbc.connect(connect, autocommit=True)
#cnxn = pyodbc.connect(connect)
    global cursor
    cursor = cnxn.cursor()
    work=Tk()
except pyodbc.InterfaceError:
     messagebox.showinfo(title='吃飽睡睡飽吃',message='連線有錯誤,請確認TMMAinfo')







#顯示視窗標題
work.title('TMMA外掛程式 v 1.0.2')
work.geometry('1500x1000+25+25')
lbl1=Label(work,text='建檔執行類 ',height=4, font=('Helvetica 12 bold')).place(x=10,y=1)

lbl2=Label(work,text='報表類',height=4, font=('Helvetica 12 bold'),).place(x=250,y=1)

lbl3=Label(work,text='開始日期',height=4,).place(x=250,y=60)

lbl4=Label(work,text='品號類別三代號',height=4,).place(x=250,y=150)

lbl5=Label(work,text='Excel輸出',height=4,).place(x=550,y=60)

lbl6=Label(work,text='銷售金額',height=4,).place(x=750,y=60)

lbl7=Label(work,text='銷售數量',height=4,).place(x=950,y=60)

lbl8=Label(work,text='銷售利潤',height=4,).place(x=1150,y=60)

lbl9=Label(work,text='銷售成長比率',height=4,).place(x=600,y=260)

lbl10=Label(work,text='銷售比率',height=4,).place(x=800,y=260)

lbl11=Label(work,text='品號類別選擇',height=4,).place(x=300,y=260)

lbl12=Label(work,text='網購需下架商品查詢 ',height=4, font=('Helvetica 12 bold')).place(x=10,y=240)#20200311新增網購查詢類

lbl13=Label(work,text='開始日期',height=4,).place(x=10,y=330)

lbl14=Label(work,text='結束日期',height=4,).place(x=10,y=380)

lbl15=Label(work,text='庫存呆滯查詢',height=4, font=('Helvetica 12 bold')).place(x=10,y=430)#20200316新增網購查詢類

lbl16=Label(work,text='開始日期',height=4,).place(x=10,y=520)

lbl17=Label(work,text='結束日期',height=4,).place(x=10,y=570)

lbl18=Label(work,text='排除庫別選擇',height=4,).place(x=200,y=260)
global date1,date2





e1=Entry(work,width=10,background='yellow',font=('Arial',16))
e1.place(x=250,y=115)


lbl4=Label(work,text='結束日期',height=4,).place(x=390,y=60)

lbl5=Label(work,text='品號輸入',height=4,).place(x=300,y=370)

e2=Entry(work,width=10,background='yellow',font=('Arial',16))
e2.place(x=390,y=115)

e5=Entry(work,width=14,background='yellow',font=('Arial',16))   #20200311新增網購查詢類日期輸入
e5.place(x=10,y=370)

e6=Entry(work,width=14,background='yellow',font=('Arial',16))   #20200311新增網購查詢類日期輸入
e6.place(x=10,y=420)

e7=Entry(work,width=14,background='yellow',font=('Arial',16))   #20200316新增
e7.place(x=10,y=560)

e8=Entry(work,width=14,background='yellow',font=('Arial',16))   #20200316新增
e8.place(x=10,y=610)


code="select MA002, MA003 from TMMA_MAIN.dbo.INVMA where MA001='3';"
cursor.execute(code)
results = cursor.fetchall()
All003=[]
for i in range(len(results)):
    All003.append(results[i][0]+results[i][1])
All003.append("ALL")
e3=ttk.Combobox(work,height=15,width=20,value=All003) #調整為下拉選單 品號分類三
e3.place(x=390,y=173)
e3.current(0)


e4=Entry(work,width=20,background='yellow',font=('Arial',16))
e4.place(x=300,y=410)

e1.focus_set()#取得輸入焦點 日期1
e2.focus_set()#取得輸入焦點 日期2
e3.focus_set()#取得輸入焦點 日期2
e4.focus_set()#取得輸入焦點 品號
e5.focus_set()#20200311新增
e6.focus_set()#20200311新增
e7.focus_set()#20200316新增
e8.focus_set()#20200316新增
global noCount,noCount1,A,B
noCount = "SET NOCOUNT ON;"
noCount1 = "SET NOCOUNT off;"

cateno=['品號類別一','品號類別二','品號類別三','品號類別四']#品號類別動態選擇

cate=ttk.Combobox(work,height=4,width=10,value=cateno)#month
cate.place(x=300,y=305)
cate.current(0)

cate.focus_set()
A=cate.get()

cate.bind_all("<Button-3>", lambda e: focus(e)) 



cate2=['click']
cateee=ttk.Combobox(work,height=15,width=20,value=cate2)#month
cateee.place(x=410,y=305)
cateee.current(0)


#20200624庫別選擇

def callback1(eventObject):
    global ware,w
    # you can also get the value off the eventObject
    #print(eventObject.widget.get())
    w.insert(END,eventObject.widget.get()+',')
    # to see other information also available on the eventObject
    #print(dir(eventObject))

code="select MC001, MC002 from TMMA_MAIN.dbo.CMSMC where MC004='1';"
cursor.execute(code)
result2 = cursor.fetchall()
cate3=[]
for i in range(len(result2)):
    cate3.append(result2[i][0].replace("       ", ",")+result2[i][1])
cate0624=ttk.Combobox(work,height=15,width=10,value=cate3)#month
cate0624.place(x=200,y=305)
cate0624.current(0)
cate0624.bind("<<ComboboxSelected>>", callback1)

w = Text ( work,height=10, width=10 )
w.place(x=200,y=350)

yearamount=[]
monthamount=[]
for i in range(2019,2051):
    yearamount.append(i)
for i in range(1,13):
    monthamount.append(i)

year=ttk.Combobox(work,height=4,width=10,value=yearamount)#年
year.place(x=300,y=355)
year.current(1)

year.focus_set()

yearn=year.get()

month=ttk.Combobox(work,height=12,width=10,value=monthamount)#月
month.place(x=410,y=355)
month.current(0)

month.focus_set



def focus(event):
    global cate2,test,cateee
    A=cate.get()
    if A == '品號類別一':
        code="select MA002, MA003 from "+database+".dbo.INVMA where MA001='1';"
    elif A == '品號類別二':
        code="select MA002, MA003 from "+database+".dbo.INVMA where MA001='2';"
    elif A == '品號類別三':
        code="select MA002, MA003 from "+database+".dbo.INVMA where MA001='3';"
    elif A == '品號類別四':
        code="select MA002, MA003 from "+database+".dbo.INVMA where MA001='4';"
    cursor.execute(code)
    results = cursor.fetchall()
    cate2=[]
    for i in range(len(results)):
        cate2.append(results[i][0]+results[i][1])
    cateee=ttk.Combobox(work,height=15,width=20,value=cate2)#month
    cateee.place(x=410,y=305)
    cateee.current(0)
    cateee.focus_set()





def comma_format(x, p): 
    return format(x, "6,.0f").replace(",", ",") 


def buyonegetontfreepos():
    global code
    path=os.getcwd()
    path="\""+path+"\posall.sql"+"\""
    code="SQLCMD -S "+ServerID +" -U "+user+" -P "+password+" -d "+ database +" -i " + path
    os.system(code)
    messagebox.showinfo(title='吃飽睡睡飽吃',message='執行完成拉')
  

    
    
def buyonegetonefreeinternet():
    path=os.getcwd()
    path="\""+path+"\Buyonegetonefree.sql"+"\""
    code="SQLCMD -S "+ServerID +" -U "+user+" -P "+password+" -d "+ database +" -i " + path
    os.system(code)
    messagebox.showinfo(title='吃飽睡睡飽吃',message='執行完成拉')


def POSERPSalereport():
    date1=e1.get()
    date2=e2.get()
    global code,results,b
    code= "use "+database+"; Declare @out nvarchar(max); exec @out = Ray_POS_Sales @date1='"+date1+"', @date2 = '"+date2+"' ;  "
    cursor.execute(code)
    try:
        while cursor.nextset():   # NB: This always skips the first resultset
            try:
                results = cursor.fetchall()
                break
            except pyodbc.ProgrammingError:
                continue
    except  pyodbc.ProgrammingError:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='日期格式不正確喔 請確認是否為YYYYMMDD')
    col= len(results[0])
    row = len(results)
    i=0
    j=0
    a=[]
    b=[]
    b=pd.DataFrame(b)

    for i in range(col):
        for j in range(row):
            a.append(results[j][i])
        b[i]=a
        a=[]
    b = b.rename(columns={0 : "品號", 1:"品名",2:"規格",3:"品號類別一",4:"分類名稱一",5:"品號類別二",6:"分類名稱二",7:"品號類別三",8:"分類名稱三",9:"品號類別四",10:"分類名稱四",11:"銷貨數量",12:"銷貨單未稅金額",13:"銷貨單稅額",14:"原幣銷退金額",15:"原幣銷退稅額",16:"銷退數量",17:"銷貨淨額",18:"銷貨單成本",19:"銷貨毛利",20:"POS 未稅金額",21:"POS 稅額",22:"POS總金額",23:"POS銷貨成本",24:"POS毛利",25:"POS 銷售總數量",26:"商品銷貨總數量",27:"商品銷售總金額",28:"商品銷貨總成本",29:"商品銷貨總毛利",30:"商品銷貨毛利率"})
    b["品號"]=b["品號"].apply('="{}"'.format)
    b["品號類別一"]=b["品號類別一"].apply('="{}"'.format)
    b["品號類別二"]=b["品號類別二"].apply('="{}"'.format)
    b["品號類別三"]=b["品號類別三"].apply('="{}"'.format)
    b["品號類別四"]=b["品號類別四"].apply('="{}"'.format)
    b.to_csv(docpath+"\output.csv",encoding='utf_8_sig')
    messagebox.showinfo(title='吃飽睡睡飽吃',message='資料輸出完成拉 路徑在 \n '+docpath+"\output.csv")
    
    

def topfivesales():
    global code,results,b,a1,a,colors,date1,date2
    date1=e1.get()
    date2=e2.get()
    condition=e3.get()#20200310 更改為取前四位
    name=condition[6:]
    condition=condition[0:6]
    condition=condition.rstrip()
    code= "use "+database+"; Declare @out nvarchar(max); exec @out = Ray_POS_Sales @date1='"+date1+"', @date2 = '"+date2+"' ;  "
    cursor.execute(code)
    try:
        while cursor.nextset():   # NB: This always skips the first resultset
            try:
                results = cursor.fetchall()
                break
            except pyodbc.ProgrammingError:
                continue
    except ProgrammingError:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='日期格式不正確喔 請確認是否為YYYYMMDD')
    col= len(results[0])
    row = len(results)
    i=0
    j=0
    a=[]
    b=[]
    b=pd.DataFrame(b)
    for i in range(col):
        for j in range(row):
            a.append(results[j][i])
        b[i]=a
        a=[]
    b = b.rename(columns={0 : "品號", 1:"品名",2:"規格",3:"品號類別一",4:"分類名稱一",5:"品號類別二",6:"分類名稱二",7:"品號類別三",8:"分類名稱三",9:"品號類別四",10:"分類名稱四",11:"銷貨數量",12:"銷貨單未稅金額",13:"銷貨單稅額",14:"原幣銷退金額",15:"原幣銷退稅額",16:"銷退數量",17:"銷貨淨額",18:"銷貨單成本",19:"銷貨毛利",20:"POS 未稅金額",21:"POS 稅額",22:"POS總金額",23:"POS銷貨成本",24:"POS毛利",25:"POS 銷售總數量",26:"商品銷貨總數量",27:"商品銷售總金額",28:"商品銷貨總成本",29:"商品銷貨總毛利",30:"商品銷貨毛利率"})
    if condition == '' or condition =='ALL':
        print('no condition')
        messagebox.showinfo(title='吃飽睡睡飽吃',message='會全部都出來喔')
        name='品號'
    else:
        fliter = (b['品號類別三']==condition)
        b=b[fliter]
    a1=b.sort_values("商品銷售總金額",ascending=False).head(10)#20200309改為顯示10
    a1['商品銷售總金額']=pd.to_numeric(a1['商品銷售總金額'], errors='coerce')
    a=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')
    colors=['black', 'red', 'green', 'blue', 'cyan','pink','magenta','brown','olive','gray','orange','skyblue','palegreen','peru','lightgreen','cadetblue','fuchsia','seagreen','burlywood','royalblue']
    a2=np.arange(len(a1))
    a1.index=a2
    i=0
    j=-0.25
    ax = plt.subplot(111)
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(comma_format)) #20200309更改Y軸數字為三位一撇 
    while i < (len(a1)):
        plt.bar(a[i],a1.loc[i,'商品銷售總金額'],color=colors[i],label=a1.loc[i,'品名']+' @'+str(int(a1.loc[i,"商品銷貨總數量"])),width=0.5)#20200309更改寬度
        plt.text(i-0.35, a1.loc[i,'商品銷售總金額'], int(round(a1.loc[i,'商品銷售總金額'],0)), color='blue',position=(j,a1.loc[i,'商品銷售總金額']),fontsize='9',weight='bold')#20200309 text 位置改用position
        i=i+1
        j=j+1
    plt.xlabel('銷售排名',fontproperties=font)
    plt.ylabel('金額',fontproperties=font)
    plt.title( date1+'~'+date2+' '+condition+'「'+name+'」'+'商品總銷售金額排名',fontproperties=font) #20200309刪除類別三 
    plt.legend(prop = font1,loc=0)
    plt.show()
    
    
def top20salesV():
    global code,results,b,a1,a,colors,date1,date2
    date1=e1.get()
    date2=e2.get()
    condition=e3.get()#20200310 更改為取前四位
    name=condition[6:]
    condition=condition[0:6]
    condition=condition.rstrip()
    code= "use "+database+"; Declare @out nvarchar(max); exec @out = Ray_POS_Sales @date1='"+date1+"', @date2 = '"+date2+"' ;  "
    cursor.execute(code)
    try:
        while cursor.nextset():   # NB: This always skips the first resultset
            try:
                results = cursor.fetchall()
                break
            except pyodbc.ProgrammingError:
                continue
    except  pyodbc.ProgrammingError:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='日期格式不正確喔 請確認是否為YYYYMMDD')
    col= len(results[0])
    row = len(results)
    i=0
    j=0
    a=[]
    b=[]
    b=pd.DataFrame(b)
    for i in range(col):
        for j in range(row):
            a.append(results[j][i])
        b[i]=a
        a=[]
    b = b.rename(columns={0 : "品號", 1:"品名",2:"規格",3:"品號類別一",4:"分類名稱一",5:"品號類別二",6:"分類名稱二",7:"品號類別三",8:"分類名稱三",9:"品號類別四",10:"分類名稱四",11:"銷貨數量",12:"銷貨單未稅金額",13:"銷貨單稅額",14:"原幣銷退金額",15:"原幣銷退稅額",16:"銷退數量",17:"銷貨淨額",18:"銷貨單成本",19:"銷貨毛利",20:"POS 未稅金額",21:"POS 稅額",22:"POS總金額",23:"POS銷貨成本",24:"POS毛利",25:"POS 銷售總數量",26:"商品銷貨總數量",27:"商品銷售總金額",28:"商品銷貨總成本",29:"商品銷貨總毛利",30:"商品銷貨毛利率"})
    if condition == '' or condition =='ALL':
        print('no condition')
        messagebox.showinfo(title='吃飽睡睡飽吃',message='沒下條件會全部都出來喔')
        name='品號'
    else:
        fliter = (b['品號類別三']==condition)
        b=b[fliter]
    a1=b.sort_values("商品銷貨總數量",ascending=False).head(10)#20200309改為顯示10
    a1['商品銷貨總數量']=pd.to_numeric(a1['商品銷貨總數量'], errors='coerce')
    a=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')
    colors=['black', 'red', 'green', 'blue', 'cyan','pink','magenta','brown','olive','gray','orange','skyblue','palegreen','peru','lightgreen','cadetblue','fuchsia','seagreen','burlywood','royalblue']
    a2=np.arange(len(a1))
    a1.index=a2
    i=0
    j=-0.05
    ax = plt.subplot(111)
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(comma_format)) #20200309更改Y軸數字為三位一撇 
    while i < (len(a1)):
        plt.bar(a[i],a1.loc[i,'商品銷貨總數量'],color=colors[i],label=a1.loc[i,'品名']+' $'+str(int(a1.loc[i,"商品銷售總金額"])),width=0.5)#20200309更改寬度)
        plt.text(i-0.35, a1.loc[i,'商品銷貨總數量'], int(round(a1.loc[i,'商品銷貨總數量'],0)), color='blue',position=(j,a1.loc[i,'商品銷貨總數量']),fontsize='9',weight='bold')#20200309 text 位置改用position
        i=i+1
        j=j+1
    plt.xlabel('數量排名',fontproperties=font)
    plt.ylabel('數量',fontproperties=font)
    plt.title( date1+'~'+date2+' '+condition+'「'+name+'」'+'商品總銷售數量排名',fontproperties=font)#20200309刪除類別三  更改內容
    plt.legend(prop = font1,loc=0)
    plt.show()

def top20salesPOS():
    global code,results,b,a1,a,colors,date1,date2
    date1=e1.get()
    date2=e2.get()
    condition=e3.get()#20200310 更改CONDITION處理方式
    name=condition[6:]
    condition=condition[0:6]
    condition=condition.rstrip()
    code= "use "+database+"; Declare @out nvarchar(max); exec @out = Ray_POS_Sales @date1='"+date1+"', @date2 = '"+date2+"' ;  "
    cursor.execute(code)
    try:
        while cursor.nextset():   # NB: This always skips the first resultset
            try:
                results = cursor.fetchall()
                break
            except pyodbc.ProgrammingError:
                continue
    except  pyodbc.ProgrammingError:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='日期格式不正確喔 請確認是否為YYYYMMDD')
    col= len(results[0])
    row = len(results)
    i=0
    j=0
    a=[]
    b=[]
    b=pd.DataFrame(b)
    for i in range(col):
        for j in range(row):
            a.append(results[j][i])
        b[i]=a
        a=[]
    b = b.rename(columns={0 : "品號", 1:"品名",2:"規格",3:"品號類別一",4:"分類名稱一",5:"品號類別二",6:"分類名稱二",7:"品號類別三",8:"分類名稱三",9:"品號類別四",10:"分類名稱四",11:"銷貨數量",12:"銷貨單未稅金額",13:"銷貨單稅額",14:"原幣銷退金額",15:"原幣銷退稅額",16:"銷退數量",17:"銷貨淨額",18:"銷貨單成本",19:"銷貨毛利",20:"POS 未稅金額",21:"POS 稅額",22:"POS總金額",23:"POS銷貨成本",24:"POS毛利",25:"POS 銷售總數量",26:"商品銷貨總數量",27:"商品銷售總金額",28:"商品銷貨總成本",29:"商品銷貨總毛利",30:"商品銷貨毛利率"})
    if condition == '' or condition =='ALL':
        print('no condition')
        messagebox.showinfo(title='吃飽睡睡飽吃',message='沒下條件會全部都出來喔')
        name='品號'
    else:
        fliter = (b['品號類別三']==condition)
        b=b[fliter]
    a1=b.sort_values("POS總金額",ascending=False).head(10)#20200309改為顯示10
    a1["POS總金額"]=pd.to_numeric(a1["POS總金額"], errors='coerce')
    a=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')
    colors=['black', 'red', 'green', 'blue', 'cyan','pink','magenta','brown','olive','gray','orange','skyblue','palegreen','peru','lightgreen','cadetblue','fuchsia','seagreen','burlywood','royalblue']
    a2=np.arange(len(a1))
    a1.index=a2
    i=0
    j=-0.25
    ax = plt.subplot(111)
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(comma_format)) #20200309更改Y軸數字為三位一撇 
    while i < (len(a1)):
        plt.bar(a[i],a1.loc[i,"POS總金額"],color=colors[i],label=a1.loc[i,'品名']+' @POS數量'+str(int(a1.loc[i,"POS 銷售總數量"])),width=0.5)#20200309更改寬度
        plt.text(i-0.35, a1.loc[i,"POS總金額"], int(round(a1.loc[i,"POS總金額"],0)),color='blue',position=(j,a1.loc[i,"POS總金額"]),fontsize='9',weight='bold')#20200309 text 位置改用position
        i=i+1
        j=j+1
    plt.xlabel('金額排名',fontproperties=font)
    plt.ylabel('金額',fontproperties=font)
    plt.title( date1+'~'+date2+' '+condition+'「'+name+'」'+'POS銷售金額TOP10',fontproperties=font) #20200310更改顯示內容 
    plt.legend(prop = font1,loc=0)
    plt.show()

def top20profit():
    global code,results,b,a1,a,colors,date1,date2
    date1=e1.get()
    date2=e2.get()
    condition=e3.get()#20200310 更改CONDITION處理方式
    name=condition[6:]
    condition=condition[0:6]
    condition=condition.rstrip()
    code= "use "+database+"; Declare @out nvarchar(max); exec @out = Ray_POS_Sales @date1='"+date1+"', @date2 = '"+date2+"' ;  "
    cursor.execute(code)
    try:
        while cursor.nextset():   # NB: This always skips the first resultset
            try:
                results = cursor.fetchall()
                break
            except pyodbc.ProgrammingError:
                continue
    except  pyodbc.ProgrammingError:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='日期格式不正確喔 請確認是否為YYYYMMDD')
    col= len(results[0])
    row = len(results)
    i=0
    j=0
    a=[]
    b=[]
    b=pd.DataFrame(b)
    for i in range(col):
        for j in range(row):
            a.append(results[j][i])
        b[i]=a
        a=[]
    b = b.rename(columns={0 : "品號", 1:"品名",2:"規格",3:"品號類別一",4:"分類名稱一",5:"品號類別二",6:"分類名稱二",7:"品號類別三",8:"分類名稱三",9:"品號類別四",10:"分類名稱四",11:"銷貨數量",12:"銷貨單未稅金額",13:"銷貨單稅額",14:"原幣銷退金額",15:"原幣銷退稅額",16:"銷退數量",17:"銷貨淨額",18:"銷貨單成本",19:"銷貨毛利",20:"POS 未稅金額",21:"POS 稅額",22:"POS總金額",23:"POS銷貨成本",24:"POS毛利",25:"POS 銷售總數量",26:"商品銷貨總數量",27:"商品銷售總金額",28:"商品銷貨總成本",29:"商品銷貨總毛利",30:"商品銷貨毛利率"})
    if condition == '' or condition =='ALL' : #20200311 更改增加ALL 條件
        print('no condition')
        messagebox.showinfo(title='吃飽睡睡飽吃',message='沒下條件會全部都出來喔')
        name='品號'
    else:
        fliter = (b['品號類別三']==condition)
        b=b[fliter]
    a1=b.sort_values("商品銷貨總毛利",ascending=False).head(10)#20200309改為顯示10
    a1["商品銷貨總毛利"]=pd.to_numeric(a1["商品銷貨總毛利"], errors='coerce')
    a=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')
    colors=['black', 'red', 'green', 'blue', 'cyan','pink','magenta','brown','olive','gray','orange','skyblue','palegreen','peru','lightgreen','cadetblue','fuchsia','seagreen','burlywood','royalblue']
    a2=np.arange(len(a1))
    a1.index=a2
    i=0
    j=-0.25
    ax = plt.subplot(111)
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(comma_format)) #20200309更改Y軸數字為三位一撇 
    while i < (len(a1)):
        plt.bar(a[i],a1.loc[i,"商品銷貨總毛利"],color=colors[i],label=a1.loc[i,'品名']+' @毛利率'+str(int(a1.loc[i,"商品銷貨毛利率"]))+'%',width=0.5)#20200309更改寬度)
        plt.text(i-0.35, a1.loc[i,"商品銷貨總毛利"], int(round(a1.loc[i,"商品銷貨總毛利"],0)),color='blue',position=(j,a1.loc[i,"商品銷貨總毛利"]),fontsize='9',weight='bold')#20200309 text 位置改用position
        i=i+1
        j=j+1
    plt.xlabel('毛利排名',fontproperties=font)
    plt.ylabel('金額',fontproperties=font)
    plt.title( date1+'~'+date2+' '+condition+'「'+name+'」'+'商品毛利POS+ERP排名',fontproperties=font) #20200310更改顯示內容 
    plt.legend(prop = font1,loc=0)
    plt.show()

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def splitdatetofive(Y,M):
    global Adate
    Adate = datetime.date(Y, M,1)
    alldaterange=[]
    for i in range(1,6):
        alldaterange.append(datetime.datetime.strptime(str(add_months(Adate,1)- datetime.timedelta(days = 1)), '%Y-%m-%d').strftime('%Y%m%d'))
        alldaterange.append(datetime.datetime.strptime(str(Adate), '%Y-%m-%d').strftime('%Y%m%d'))
        Adate=add_months(Adate,-1)
    return alldaterange

def splitdatetoone(Y,M):
    global Adate
    Adate = datetime.date(Y, M,1)
    alldaterange=[]
    alldaterange.append(datetime.datetime.strptime(str(add_months(Adate,1)- datetime.timedelta(days = 1)), '%Y-%m-%d').strftime('%Y%m%d'))
    alldaterange.append(datetime.datetime.strptime(str(Adate), '%Y-%m-%d').strftime('%Y%m%d'))
    Adate=add_months(Adate,-1)
    return alldaterange
    
    
    

def categorysales():
    global amount,b,condition,months
    A=cate.get()
    yearn=int(year.get())
    monthn=int(month.get())
    alldaterange=splitdatetofive(yearn,monthn)
    saleposamount=[]
    salemamount=[]
    saleERP=[]
    
    condition=cateee.get()
    condition1=condition
    condition=condition[0:6]
    condition=condition.rstrip()
    z=0

    if condition == 'click':
            print('no condition')
            messagebox.showinfo(title='吃飽睡睡飽吃',message='請點選滑鼠右鍵才會有類別出現')
    else:
        for x in range(0,int(len(alldaterange)/2)):
            date1=alldaterange[z+1]
            date2=alldaterange[z]
            code= "use "+database+"; Declare @out nvarchar(max); exec @out = Ray_POS_Sales @date1='"+date1+"', @date2 = '"+date2+"' ;  "
            cursor.execute(code)
            try:
                while cursor.nextset():   # NB: This always skips the first resultset
                    try:
                        results = cursor.fetchall()
                        break
                    except pyodbc.ProgrammingError:
                        continue
            except  pyodbc.ProgrammingError:
                messagebox.showinfo(title='吃飽睡睡飽吃',message='沒有資料喔 請確認是不是有日期錯了')
            col= len(results[0])
            row = len(results)
            i=0
            j=0
            a=[]
            b=[]
            b=pd.DataFrame(b)
            for i in range(col):
                for j in range(row):
                    a.append(results[j][i])
                b[i]=a
                a=[]
            b = b.rename(columns={0 : "品號", 1:"品名",2:"規格",3:"品號類別一",4:"分類名稱一",5:"品號類別二",6:"分類名稱二",7:"品號類別三",8:"分類名稱三",9:"品號類別四",10:"分類名稱四",11:"銷貨數量",12:"銷貨單未稅金額",13:"銷貨單稅額",14:"原幣銷退金額",15:"原幣銷退稅額",16:"銷退數量",17:"銷貨淨額",18:"銷貨單成本",19:"銷貨毛利",20:"POS 未稅金額",21:"POS 稅額",22:"POS總金額",23:"POS銷貨成本",24:"POS毛利",25:"POS 銷售總數量",26:"商品銷貨總數量",27:"商品銷售總金額",28:"商品銷貨總成本",29:"商品銷貨總毛利",30:"商品銷貨毛利率"})
            if A == '品號類別一':
                fliter = (b['品號類別一']==condition)
                b=b[fliter]
            elif A == '品號類別二':
                fliter = (b['品號類別二']==condition)
                b=b[fliter]
            elif A == '品號類別三':
                fliter = (b['品號類別三']==condition)
                b=b[fliter]
            elif A == '品號類別四':
                fliter = (b['品號類別四']==condition)
                b=b[fliter]
            b["POS總金額"]=pd.to_numeric(b["POS總金額"])
            b["商品銷售總金額"]=pd.to_numeric(b["商品銷售總金額"])
            b["銷貨淨額"]=pd.to_numeric(b["銷貨淨額"])
            saleposamount.append(sum(b["POS總金額"]))
            salemamount.append(sum(b["商品銷售總金額"]))
            saleERP.append(sum(b["銷貨淨額"]))
            z=z+2
        z=0
        months=[]
        for x in range(0,int(len(alldaterange)/2)):
            a=alldaterange[z]
            months.append(a[0:6])
            z=z+2
        saleposamount.reverse()
        salemamount.reverse()
        saleERP.reverse()
        months.reverse()
        plt.plot(months, saleposamount, color='red',label="POS總金額"+'@'+str(saleposamount))
        plt.plot(months, salemamount, color='blue',label='商品銷售總金額'+'@'+str(salemamount))
        plt.plot(months, saleERP, color='purple',label='ERP後台銷售'+'@'+str(saleERP))
        plt.title(A+condition1+'五個月成長狀況',fontproperties=font)
        plt.legend(prop = font1,loc=0)
        plt.gcf().set_facecolor("gray")
        plt.show()

def my_autopct(pct):
    return ('%.2f' % pct) if pct > 5 else ''

def c_sort(A,B,C):
    total=sum(B)
    A=pd.DataFrame(A)
    B=pd.DataFrame(B)
    C=pd.DataFrame(C)
    test3 = pd.concat([A, B,C], axis=1)
    test3.columns = ['allcate','pieamount','Name']

    test3=test3.sort_values('pieamount',ascending=False)
    test3.index=np.arange(0,len(test3))
    return test3

def c_label(A):
    total=sum(A['pieamount'])
    lists=[]
    for i in range(0,len(A)):
        percent=round((A.loc[i,'pieamount']/total)*100,3)
        temp=A.loc[i,'allcate'] +' '+A.loc[i,'Name']+'  '+str(percent)+'%'+' $'+str(A.loc[i,'pieamount'])
        lists.append(temp)
    return lists

def p_label(A): #20200310新增 pie chart 上 label 少於5% 不顯示
    B=A
    for i in range(len(A)):
        if (A.loc[i,'pieamount']*100/np.sum(A['pieamount'])) < 5:
            B.loc[i,'Name']=''
    return B

        

def piechart():
    global code,results,b,pieamount,allcate,temp,lists,label,time,NM,my_font,templab
    A=cate.get()
    yearn=int(year.get())
    monthn=int(month.get())
    time=splitdatetoone(yearn,monthn)
    code= "use "+database+"; Declare @out nvarchar(max); exec @out = Ray_POS_Sales @date1='"+time[1]+"', @date2 = '"+time[0]+"' ;  "
    cursor.execute(code)
    try:
        while cursor.nextset():   # NB: This always skips the first resultset
            try:
                results = cursor.fetchall()
                break
            except pyodbc.ProgrammingError:
                continue
    except  pyodbc.ProgrammingError:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='日期格式不正確喔 請確認是否為YYYYMMDD')
    col= len(results[0])
    row = len(results)
    i=0
    j=0
    a=[]
    b=[]
    b=pd.DataFrame(b)
    allcate=[]
    code="; select MA007,MA008,MA009,MA010  from "+database+".dbo.CMSMA; "
    cursor.execute(code)
    cate223 = cursor.fetchall()
    pieamount=[]
    for i in range(col):
        for j in range(row):
            a.append(results[j][i])
        b[i]=a
        a=[]
        NM=[]
    b = b.rename(columns={0 : "品號", 1:"品名",2:"規格",3:"品號類別一",4:"分類名稱一",5:"品號類別二",6:"分類名稱二",7:"品號類別三",8:"分類名稱三",9:"品號類別四",10:"分類名稱四",11:"銷貨數量",12:"銷貨單未稅金額",13:"銷貨單稅額",14:"原幣銷退金額",15:"原幣銷退稅額",16:"銷退數量",17:"銷貨淨額",18:"銷貨單成本",19:"銷貨毛利",20:"POS 未稅金額",21:"POS 稅額",22:"POS總金額",23:"POS銷貨成本",24:"POS毛利",25:"POS 銷售總數量",26:"商品銷貨總數量",27:"商品銷售總金額",28:"商品銷貨總成本",29:"商品銷貨總毛利",30:"商品銷貨毛利率"})
    b ['商品銷售總金額']=pd.to_numeric(b['商品銷售總金額'], errors='coerce')
    if A == '品號類別一':
        allcate=b['品號類別一'].unique()
        catename=cate223[0][0]
        for i in range(0,len(allcate)):
            fliter = (b['品號類別一']==allcate[i])
            temp=b[fliter]
            NM.append(temp["分類名稱一"].unique())#20200310新增 類別名稱抓取
            pieamount.append(round(sum(temp['商品銷售總金額'])))
    elif A == '品號類別二':
        allcate=b['品號類別二'].unique()
        catename=cate223[0][1]
        for i in range(0,len(allcate)):
            fliter = (b['品號類別二']==allcate[i])
            temp=b[fliter]
            NM.append(temp["分類名稱二"].unique())#20200310新增 類別名稱抓取
            pieamount.append(round(sum(temp['商品銷售總金額'])))
    elif A == '品號類別三':
        allcate=b['品號類別三'].unique()
        catename=cate223[0][2]
        for i in range(0,len(allcate)):
            fliter = (b['品號類別三']==allcate[i])
            temp=b[fliter]
            NM.append(temp["分類名稱三"].unique())#20200310新增 類別名稱抓取
            pieamount.append(round(sum(temp['商品銷售總金額'])))
    elif A == '品號類別四':
        allcate=b['品號類別四'].unique()
        catename=cate223[0][3]
        for i in range(0,len(allcate)):
            fliter = (b['品號類別四']==allcate[i])
            temp=b[fliter]
            NM.append(temp["分類名稱四"].unique())#20200310新增 類別名稱抓取
            pieamount.append(round(sum(temp['商品銷售總金額'])))
    lists=c_sort(allcate,pieamount,NM)
    label=c_label(lists)
    templab=p_label(lists)
    
    patches,l_text,p_text =plt.pie(lists['pieamount'],labels=templab['Name'], autopct = my_autopct,pctdistance = 0.6,startangle=90,textprops = {'fontsize' : 10},shadow=True)
    for t in l_text:
        t.set_fontproperties(my_font)
    plt.axis('equal')
    plt.title(str(yearn)+str(monthn)+' 「'+catename+'」'+"單月銷售類別占比",fontproperties=font)
    plt.legend(prop = font1,labels=label,loc = 0)
    plt.tight_layout()
    plt.show()

def Productsales():
    global amount,b,months,saleposamount,product,b,alldaterange
    A=cate.get()
    yearn=int(year.get())
    monthn=int(month.get())
    product=e4.get()
    alldaterange=splitdatetofive(yearn,monthn)
    saleposamount=[]
    salemamount=[]
    saleERP=[]
    z=0

    code="select MB001 from "+database+".dbo.INVMB where MB001='"+product+"';"
    cursor.execute(code)
    test=cursor.fetchall()
    if []==test:
        messagebox.showerror(title='吃飽睡睡飽吃',message='找不到此品號 請行行好重新確認')
    else:
        for x in range(0,int(len(alldaterange)/2)):
            date1=alldaterange[z+1]
            date2=alldaterange[z]
            code= "use TMMA_MAIN; Declare @out nvarchar(max); exec @out = Ray_POS_Sales @date1='"+date1+"', @date2 = '"+date2+"' ;  "
            cursor.execute(code)
            try:
                while cursor.nextset():   # NB: This always skips the first resultset
                    try:
                        results = cursor.fetchall()
                        break
                    except pyodbc.ProgrammingError:
                        continue
            except  pyodbc.ProgrammingError:
                messagebox.showinfo(title='吃飽睡睡飽吃',message='沒有資料喔 請確認是不是有日期錯了')
            col= len(results[0])
            row = len(results)
            i=0
            j=0
            a=[]
            b=[]
            b=pd.DataFrame(b)
            for i in range(col):
                for j in range(row):
                    a.append(results[j][i])
                b[i]=a
                a=[]
            b = b.rename(columns={0 : "品號", 1:"品名",2:"規格",3:"品號類別一",4:"分類名稱一",5:"品號類別二",6:"分類名稱二",7:"品號類別三",8:"分類名稱三",9:"品號類別四",10:"分類名稱四",11:"銷貨數量",12:"銷貨單未稅金額",13:"銷貨單稅額",14:"原幣銷退金額",15:"原幣銷退稅額",16:"銷退數量",17:"銷貨淨額",18:"銷貨單成本",19:"銷貨毛利",20:"POS 未稅金額",21:"POS 稅額",22:"POS總金額",23:"POS銷貨成本",24:"POS毛利",25:"POS 銷售總數量",26:"商品銷貨總數量",27:"商品銷售總金額",28:"商品銷貨總成本",29:"商品銷貨總毛利",30:"商品銷貨毛利率"})
            b['品號']=b['品號'].str.rstrip()
            fliter = (b["品號"]==product)
            b=b[fliter]
            b["POS總金額"]=pd.to_numeric(b["POS總金額"])
            b["商品銷售總金額"]=pd.to_numeric(b["商品銷售總金額"])
            b["銷貨淨額"]=pd.to_numeric(b["銷貨淨額"])
            saleposamount.append(sum(b["POS總金額"]))
            salemamount.append(sum(b["商品銷售總金額"]))
            saleERP.append(sum(b["銷貨淨額"]))
            z=z+2
        z=0
        months=[]
        for x in range(0,int(len(alldaterange)/2)):
            a=alldaterange[z]
            months.append(a[0:6])
            z=z+2
        saleposamount.reverse()
        salemamount.reverse()
        saleERP.reverse()
        months.reverse()
        plt.plot(months, saleposamount, color='red',label="POS總金額"+'@'+str(saleposamount))
        plt.plot(months, salemamount, color='blue',label='商品銷售總金額'+'@'+str(salemamount))
        plt.plot(months, saleERP, color='purple',label='ERP後台銷售'+'@'+str(saleERP))
        plt.title(A+product+'五個月成長狀況',fontproperties=font)
        plt.legend(prop = font1,loc=0)
        plt.gcf().set_facecolor("gray")
        plt.show()

def autoupdate():
    path=os.getcwd()
    path="\""+path+"\Adjustmain.sql"+"\""
    code="SQLCMD -S "+ServerID +" -U "+user+" -P "+password+" -d "+ database +" -i " + path
    os.system(code)
    messagebox.showinfo(title='吃飽睡睡飽吃',message='執行完成拉')


def interent3():
    global b,code,results,inputValue,main
    date1=e5.get()
    date2=e6.get()
    inputValue=w.get("1.0","end-1c")
    

    if(inputValue==''):
        code = '''use '''+ database+'''
        ;
        select LA001 as '品號', sum(iif(LA005=1,LA011,0)) as '昨日入庫數量',
        sum(iif(LA005=-1,LA011,0)) as '昨日出庫數量', 
        sum(iif(LA005=1,LA011,0))-sum(iif(LA005=-1,LA011,0)) as '昨日餘額',
        INVMB.MB064 as '現有庫存數量'
        from INVLA 
        left join INVMB on INVLA.LA001=INVMB.MB001
        where (LA004<='''+date2 +''') and LA004>= ('''+date1 + ''') and INVMB.MB064='0'  
        group by LA001,INVMB.MB064
        Having sum(iif(LA005=1,LA011,0))-sum(iif(LA005=-1,LA011,0))<=0;'''
    else:
        t=pd.DataFrame([x.split(',') for x in inputValue.split('\n')])
        part=""
        main=""
        nn=len(t.columns)
        for i in range(0,nn):
            part=""
            if(i==0):
                part="LA009 != "+"\'"+t[i]+"\'"
            elif(i%2==1):
                pass
            elif(i==nn-1):
                pass
            else:
                part="or LA009 != "+"\'"+t[i]+"\'"
            main=main+part
        main='('+main+')'
        code = '''use '''+database+''';
        select LA001 as '品號', sum(iif(LA005=1,LA011,0)) as '昨日入庫數量',
        sum(iif(LA005=-1,LA011,0)) as '昨日出庫數量', 
        sum(iif(LA005=1,LA011,0))-sum(iif(LA005=-1,LA011,0)) as '昨日餘額',
        INVMB.MB064 as '現有庫存數量'
        from INVLA 
        left join INVMB on INVLA.LA001=INVMB.MB001
        where (LA004<='''+date2+''') and LA004>= ('''+date1+") and INVMB.MB064='0' and "
        code=code+main[0]+" group by LA001,INVMB.MB064 Having sum(iif(LA005=1,LA011,0))-sum(iif(LA005=-1,LA011,0))<=0;"
    
        
    cursor.execute(code)
    try:
        while cursor.nextset():   # NB: This always skips the first resultset
            try:
                results = cursor.fetchall()
                break
            except pyodbc.ProgrammingError:
                continue
    except  pyodbc.ProgrammingError:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='日期格式不正確喔 請確認是否為YYYYMMDD')

    try:
        col= len(results[0])
        row = len(results)
        i=0
        j=0
        a=[]
        b=[]
        b=pd.DataFrame(b)
        for i in range(col):
            for j in range(row):
                a.append(results[j][i])
            b[i]=a
            a=[]
        b = b.rename(columns={0:"品號",1:"昨日入庫數量",2:'昨日出庫數量',3:'昨日餘額',4:'現有庫存數量'})
        ht=pd.DataFrame.to_html(b)
        url=docpath+'\\'+date1+'-'+date2+'.html'
        text_file=open(url,'w')
        text_file.write(ht)
        text_file.close()
        webbrowser.open(url,new=2)
    except IndexError:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='沒有資料喔 請行行好看是不是格式打錯了')
    

def transaction():
    global b,code,results
    date1=e7.get()
    date2=e8.get()
    code ="use "+database+"; exec  Three_months_no_transaction @date1='"+date1+"', @date2 = '"+date2+"';"  
        
    cursor.execute(code)
    try:
        while cursor.nextset():   # NB: This always skips the first resultset
            try:
                results = cursor.fetchall()
                break
            except pyodbc.ProgrammingError:
                continue
    except  pyodbc.ProgrammingError:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='日期格式不正確喔 請確認是否為YYYYMMDD')

    try:
        col= len(results[0])
        row = len(results)
        i=0
        j=0
        a=[]
        b=[]
        b=pd.DataFrame(b)
        for i in range(col):
            for j in range(row):
                a.append(results[j][i])
            b[i]=a
            a=[]
        b = b.rename(columns={0:"品名",1:"品號",2:'品號類別一',3:'品號類別一名稱',4:'品號類別二',5:'品號類別二名稱',6:'品號類別三',7:'品號類別三名稱',8:'品號類別四',9:'品號類別四名稱',10:'最近銷售日期',11:'備註',12:'單別',13:'單號'})
        ht=pd.DataFrame.to_html(b)
        url=docpath+'\\'+date1+'-'+date2+'transaction.html'
        text_file=open(url,'w')
        text_file.write(ht)
        text_file.close()
        webbrowser.open(url,new=2)
    except IndexError:
        messagebox.showinfo(title='吃飽睡睡飽吃',message='沒有資料喔 請行行好看是不是格式打錯了')

#建檔類BTN
btn=Button(work,text='POS組合促銷品自動新增',height=2,width=20,command=buyonegetontfreepos)
btn.place(x=10,y=60)

btn1=Button(work,text='銷貨促銷買一送一自動新增',height=2,width=20,command=buyonegetonefreeinternet)
btn1.place(x=10,y=120)

btn22=Button(work,text='POS組合促銷價格自動更新',height=2,width=20,command=autoupdate)
btn22.place(x=10,y=180)


#報表類BTN

btn2=Button(work,text='POS+ERP銷售總報表',height=2,width=20,command=POSERPSalereport)
btn2.place(x=550,y=100)

btn3=Button(work,text='總銷售金額最好10項商品',height=2,width=20,command=topfivesales)#20200310更改為顯示10
btn3.place(x=750,y=100)

btn4=Button(work,text='總銷售數量最好10項商品',height=2,width=20,command=top20salesV)#20200310更改為顯示10
btn4.place(x=950,y=100)

btn5=Button(work,text='POS銷售金額TOP10',height=2,width=20,command=top20salesPOS)#20200310更改為顯示10
btn5.place(x=750,y=150)

btn6=Button(work,text='利潤最好10項商品',height=2,width=20,command=top20profit)
btn6.place(x=1150,y=100)

btn6=Button(work,text='類別銷售近五個月成長線',height=2,width=20,command=categorysales)
btn6.place(x=600,y=300)

btn7=Button(work,text='品號近五個月成長線',height=2,width=20,command=Productsales)
btn7.place(x=600,y=400)

btn8=Button(work,text='類別銷售比率圓餅圖',height=2,width=20,command=piechart)#20200310增加於LEGEND 顯示類別中文名稱
btn8.place(x=800,y=300)



#網購查詢類
btn9=Button(work,text='期間有銷貨 目前無庫存',height=2,width=20,command=interent3)#20200311新增網路扣庫存查詢按鈕  查前一日
btn9.place(x=10,y=300)

#庫存呆滯查詢類
btn10=Button(work,text='庫存呆滯不分館查詢',height=2,width=20,command=transaction)#20200316新增庫存呆滯查詢
btn10.place(x=10,y=490)

work.mainloop()


