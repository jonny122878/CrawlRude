import pandas as pd




def GetHouse():
    prjbrand=[]#房屋品牌
    prjID=[]#次序
    prjName=[]#案名
    prjhref=[]#網址
    prjaddr=[]#地址

    prjprice=[]#價錢
    prjPattern=[]#格局
    prjNop=[]#坪數
    prjStair=[]#樓層
    prjAge=[]#屋齡

    prjType=[]#種類
    prjIndex=[]#索引
    prjStamped=[]#加蓋
    prjParking=[]#車位
    prjImg=[]#外觀

    prjtel=[]#電話
    prjComu=[]#社區
    prjSN=[]#段建號
    prjNol=[]#土地坪數
    prjDir=[]#朝向

    prjMainBui=[]#主建物
    prjAb=[]#附屬建物
    prjCp=[]#共有部分
    houses = trans_df={
            '房屋品牌':prjbrand,
            '次序':prjID,
            '案名':prjName,
            '地址':prjaddr,
            '價錢':prjprice,

            '格局':prjPattern,
            '加蓋':prjStamped,
            '坪數':prjNop,
            '樓層':prjStair,
            '屋齡':prjAge,

            '索引':prjIndex,
            '種類':prjType,
            '外觀':prjImg,
            '車位':prjParking,
            '網址':prjhref,

            '社區':prjComu,
            '段建號':prjSN,
            '土地坪數':prjNol,
            '朝向':prjDir,
            '電話':prjtel,

            '主建物':prjMainBui,
            '附屬建物':prjAb,
            '共有部分':prjCp      
        }    
    return houses
