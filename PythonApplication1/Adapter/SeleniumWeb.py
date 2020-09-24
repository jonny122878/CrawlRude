from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from YungData import *


class Selenium_591 :
	 
	def __init__(self):		
		chrome_options = Options()
		chrome_options.add_argument('--incognito')
		chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0')
		global browser
		browser = webdriver.Chrome(chrome_options=chrome_options)		
		browser.get("https://www.591.com.tw/")
		time.sleep(5)
	



	def GetWebBrowser(self):
		return browser

	
	def getPage_num(self):
		page_num = browser.find_element_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[7]').text
		return page_num
	
	def StringProcess(self,data):
		return data.split('|')
	
	def page_down(self,n):
		if n > 6 :
			next = browser.find_element_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[14]')
			next.click()
		else :
			next = browser.find_element_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[' + str(8+n) + ']')
			next.click()
	
	def Header(self,i):
		global house
		house = GetHouse()
		#爬取外觀資訊
		title = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']').find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/h3/a').text
		data = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/p[1]').text
		house_data = self.StringProcess(data)
		addr = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/p[2]/em').text
		price = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/div/i').text
		#house_master = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/p[3]/em[1]').text
		link = browser.find_element_by_xpath('//*[@id="content"]/ul[' + str(i) + ']/li[2]/h3/a').get_attribute('href')
		
		house['房屋品牌'].append('519')
		house['案名'].append(title)
		house['網址'].append(link)
		house['地址'].append(addr)
		house['價錢'].append(price)
		house['種類'].append(house_data[0])
		
		
		if len(house_data) >= 4:
			house['格局'].append(house_data[1])
			house['坪數'].append(house_data[2])
			house['樓層'].append(house_data[3].replace('樓層：',''))
		else:
			house['坪數'].append(house_data[1])
			house['樓層'].append(house_data[2].replace('樓層：',''))
		

	def content(self,i):
		Detail = {}
		#進入詳細頁面
		DetailButton = browser.find_element_by_xpath('//*[@id="content"]/ul['+  str(i) +']/li[2]/h3/a')
		DetailButton.click()
		handles = browser.window_handles
		browser.switch_to_window(handles[1])
		time.sleep(5)

		#爬取詳細頁資料
		for m in range(1,15):
			try :
				dt_name = browser.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/div[1]/ul[1]/li['+  str(m) +']/div[1]').text
				dt = browser.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/div[1]/ul[1]/li['+ str(m) +']/div[2]/em').text
				try:
					house[dt_name].append(dt)
				except:
					pass
			except:
				break
		
		for a in house.keys():
			if len(house[a]) == 0 :
				house[a].append(" ")
			
		browser.close()
		browser.switch_to_window(handles[0])
		time.sleep(5)

	def dataBack(self):
		return house
		
	def Exit(self):
		time.sleep(3)
		browser.quit()

	#過濾的動作
	def Filter(self):
		return