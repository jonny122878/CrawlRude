from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import io
import random
import pandas as pd
import openpyxl
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from Crawl.YungRude import *
from IO.excel import *
from IO.YungChorme import *
from Filter.YungFilter import *
from Page.YungPage import *
from YungData import *
from Page.YungPage import *
from Map.MapFloor import *

#要多二個變數.讀取網頁的網址和跑測試頁
ouputFile = 'D:/蔡礎謙/CloudStation/溝通格式Excel樣本/網頁匯整.xlsx'
sheet = '永慶'
#drivers = [YungDriver(),Rent591Driver()]
#houses = [GetHouse(),GetHouse()]

driver = YungDriver()
DriverFilter(driver)
houses = GetHouse()
time.sleep(10)

page = YungPage(driver)
page = 1
houses = YungRude(driver,page,houses)
houseFloors = map(MapSlope,houses['樓層'])
houses['樓層'] = houseFloors
StuffATableToExcel(houses,sheet,ouputFile)

#抽象層次爬蟲型𢛋
#主邏輯:
#將要抓取的網址給Load
    #次邏輯:
        #瀏覽器抽換機率較低、目前chorme
    #js過濾條件
    #獲取頁數    
#主邏輯:
#將每頁的網址所需要的資料轉換成一列
    #次邏輯：
    #模擬資料表做的結構。變動機率也不高。    
    #爬蟲目標的網址標籤，一定會變
#主邏輯：將結果呈現給使用者
    #次邏輯：
    #目前是輸出在excel，未來有可能在Db，網頁