import requests
from bs4 import BeautifulSoup
from datetime import datetime
 
url = "http://www.cbr.ru/scripts/XML_daily.asp?"
 
today = datetime.today()
today = today.strftime("%d/%m/%Y")
 
payload = {"date_req" : today}
responce = requests.get(url, params=payload)
 
xml = BeautifulSoup(responce.content, "lxml")
 
def getCourse (id):
    return xml.find("valute",  {'id': id}).value.text
 
 
def getCourseNew(id):
    _ex = {"value":0, "name":"", "nominal":0, "charCode":""}
    _node = xml.find("valute",  {'id': id})
    _ex["value"]=float(_node.value.text.replace(",","."))
    # _ex["name"]=_node.name.text
    _ex["nominal"]=int(_node.nominal.text)
    _ex["charCode"]=_node.charcode.text
    # node.children - итератор по дочерним узлам 
    return _ex
 
 
def Courses (xml):
    res = xml.findAll("valute")
    for ex in res:
        print(ex.numcode.text)
    return res
 
# print(getCourse("R01235"), "рублей за 1 доллар")
# print(getCourse("R01239"), "рублей за 1 евро")
# print(getCourse("R01375"), "рублей за 1 юань")
 
 
_t = getCourseNew("R01235")
print("{} р. за {} {}".format(_t["value"], _t["nominal"], _t["charCode"]))
 
_t = getCourseNew("R01370")
print("{} р. за {} {}".format(_t["value"], _t["nominal"], _t["charCode"]))
 
_t = getCourseNew("R01530")
print("{} р. за {} {}".format(_t["value"], _t["nominal"], _t["charCode"]))

_t = getCourseNew("R01239")
print("{} р. за {} {}".format(_t["value"], _t["nominal"], _t["charCode"]))

_t = getCourseNew("R01820")
print("{} р. за {} {}".format(_t["value"], _t["nominal"], _t["charCode"]))


valute_from = "EUR" 
valute_to = "USD" 
amount = int(input("Кол-во конвертируемой валюты(из EUR в USD): ")) 

xu = getCourse("R01235")
xe = getCourse("R01239")

def course(valute_from, valute_to, amount): 
    curs = { 
        "RUR": 1.0,
        "EUR": float(xe.replace(',', '.')),
        "USD": float(xu.replace(',', '.'))  
    } 
    if valute_from == "RUR": 
        return amount/curs[valute_to] 
    else: 
        return amount/curs[valute_to]*curs[valute_from] 
print(course(valute_from, valute_to, amount))