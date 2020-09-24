from bs4 import BeautifulSoup
def YungPage(driver):
    
    soup=BeautifulSoup(driver.page_source,'html.parser')     
    finalPage= soup.find('a',attrs={'ga_label':'buy_page_last'})
    if finalPage.get('href')!="":
       page=int(finalPage.get('href').split("pg=",1)[1])#總頁數
    return page