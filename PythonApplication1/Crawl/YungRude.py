from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import io
import random
import pandas as pd
import openpyxl


def YungRude(driver,page,houses):
    for i in range(0,page):
        temp1=[]
        temp2=[]
        temp3=[]
        temp4=[]
    
        time.sleep(random.uniform(20,30))
        soup=BeautifulSoup(driver.page_source,'html.parser')
        time.sleep(5)
        a_tags = soup.find_all('a',class_="item-title ga_click_trace")

    
        for url in a_tags:
            #'房屋品牌'       
            houses['房屋品牌'].append('永慶')
            #houses['次序'].append('=ROW()-1')
            
            houses['網址'].append("https://buy.yungching.com.tw"+url.get('href'))
        
        #處理地址&案名
        for addr in a_tags:
            addr=addr.get('title').split(" ",1)
            houses['案名'].append(addr[0])
            houses['地址'].append(addr[1])

        price=soup.find_all('span',class_="price-num")
        #處理價錢
        for pri in price:
            houses['價錢'].append(pri.string.replace(',',''))

        pattern=soup.find_all('ul',class_="item-info-detail")
        #處理格局
        #ind=0
    
        for pa in pattern:
            for child in pa.children:
            
                #if (ind+1)%2==0 :     
                if  child.string!=None:        
                    deal=child.string.replace(' ','').replace('\n','')           
                    temp1.append(deal)
                else:
                    temp1.append("")
                #ind=ind+1
        #ind=0
            
        for j in range(int(len(temp1))):
        
            if  (j+1)%19!=0:
                temp2.append(temp1[j].replace(' ','').replace('\n',''))
    
        for j in range(int(len(temp2))):
        
            if j%2!=0:
                temp3.append(temp2[j].replace(' ','').replace('\n',''))
  
        for index in range(len(temp3)):
            if (index+3)%9==0:
                houses['格局'].append(temp3[index])
        #處理坪數
        for index in range(len(temp3)):
            if (index+4)%9==0:
                houses['坪數'].append(temp3[index].strip('建物坪'))
        #處理樓層
        for index in range(len(temp3)):
            if (index+7)%9==0:
                houses['樓層'].append(temp3[index].strip('樓'))
        #處理屋齡
        for index in range(len(temp3)):
            if (index+8)%9==0:
                houses['屋齡'].append(temp3[index].strip('年'))
        #處理種類
        for index in range(len(temp3)):
            if (index+9)%9==0:
                houses['種類'].append(temp3[index])
        #處理索引
        div_tags=soup.find_all('div',class_="item-description")
        for index in div_tags:
            temp4=index.string.split(" ",1)
            houses['索引'].append(temp4[0])
        #處理加蓋
        for index in range(len(temp3)):
            if (index+2)%9==0:
                houses['加蓋'].append(temp3[index])
                houses['次序'].append("")
                houses['外觀'].append("")
                houses['社區'].append("")
                houses['土地坪數'].append("")
                houses['朝向'].append("")
                houses['電話'].append("")
                houses['主建物'].append("")
                houses['附屬建物'].append("")
                houses['共有部分'].append("")
                houses['段建號'].append('')
        #處理車位
        for index in range(len(temp3)):
            if (index+1)%9==0:
                if temp3[index].find("含車位")!=-1:#找尋含車位
                    houses['車位'].append("有")
                else:
                    houses['車位'].append("沒有")
      
        driver.delete_all_cookies()
        driver.find_element_by_xpath('//a[@ga_label="buy_page_next"]').click()#換頁


    return houses


#prjbrand=[]#房屋品牌
#    prjID=[]#次序
#    prjName=[]#案名
#    prjhref=[]#網址
#    prjaddr=[]#地址
#    prjprice=[]#價錢
#    prjPattern=[]#格局
#    prjNop=[]#坪數
#    prjStair=[]#樓層
#    prjAge=[]#屋齡
#    prjType=[]#種類
#    prjIndex=[]#索引
#    prjStamped=[]#加蓋
#    prjParking=[]#車位
#    prjImg=[]#外觀
#    prjtel=[]#電話
#    prjComu=[]#社區
#    prjSN=[]#段建號
#    prjNol=[]#土地坪數
#    prjDir=[]#朝向
#    prjMainBui=[]#主建物
#    prjAb=[]#附屬建物
#    prjCp=[]#共有部分