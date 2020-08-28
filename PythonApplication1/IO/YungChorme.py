from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
def YungDriver():    
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    #chrome_options.add_argument('user-agent='+ua.random)
    driver = webdriver.Chrome('D:/PythonApplication1/PythonApplication1/python粗抓/PythonApplication1/PythonApplication1/chromedriver.exe',options=chrome_options)
    
    driver.get('https://buy.yungching.com.tw/region')
    return driver

def TinyYungDriver(url):    
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    #chrome_options.add_argument('user-agent='+ua.random)
    driver = webdriver.Chrome('D:/PythonApplication1/PythonApplication1/python粗抓/PythonApplication1/PythonApplication1/chromedriver.exe',options=chrome_options)    
    driver.get(url)
    return driver





