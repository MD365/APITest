import requests
import xlrd
import json

def request(self, rqtype, rqurl, paramete, headers):
    if rqtype == "get":
        apiresult = requests.get(url=rqurl, params=paramete, headers=headers)  # 发送请求
        return apiresult
    if rqtype == "post":
        apiresult = requests.post(url=rqurl, data=paramete, headers=headers)
        return apiresult
    else:
        print("请求参数错误，请求类型只支持get+post，请求地址支持string，参数支持dict")
def xlsee(self, xlsFile):
    sheetlist = []  # 用来保存表格所有数据
    rqapi = xlrd.open_workbook(xlsFile)   # 获得文件对象
    sheet_name = rqapi.sheet_names()[0]  # 获取第一个sheet名称
    sheet = rqapi.sheet_by_name(sheet_name)  # 获取第一个sheet对象
    nrow = sheet.nrows   # 获取行总数
    for i in range(1,nrow):
        sheetlist.append(sheet.row_values(i))
    return sheetlist

xlsFile = "/Users/mada/APITest/apicase.xls"
workbook = xlrd.open_workbook(xlsFile)
sheet1 = workbook.sheet_by_name('Sheet1')
rows = sheet1.row_values(2)
print (rows)
url = rows[2]+rows[3]
print (url)
postData = rows[5]
response = requests.post(url,data=postData)

b= requests.get(url='http://www.rainsmoon.com/')

url = 'http://and.cbchot.com/api/server_config/'
headers={'content-type':'application/x-www-form-urlencoded','sessionid':'ff3fdcc2ed6647c2afdf12c82fff6328','X-Client':'sdk=4.4.4;screenSize=1080*1920;type=MI+3W;imei=865002028154896;imsi=460010910615030;cell_id=;version=1.1.00.17.15;mac=14:f6:5a:b6:20:c9;rootPath=%2Fstorage%2Femulated%2F0;rn=0567375437;'}
payload={"password": "ff86bb0684b4fe3b22e678eadb4af719","account":"118688"}
a=requests.post(url,headers=headers)
print (a.text)

