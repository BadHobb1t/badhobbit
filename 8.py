from tkinter import * 
from bs4 import BeautifulSoup
import requests
from datetime import datetime
window = Tk() 
window.geometry("400x400") 
window.title("Курс юаня") 
window.resizable(False, False)
window["bg"] = "blue" 

today = datetime.today()
today = today.strftime("%d/%m/%Y")

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

payload = {"date_req": today}

response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, "lxml")

def getCourse(id):
    return xml.find("valute", {'id':id}).value.text

course_info = Label(window, text="Курс на: " + today.replace('/','.'), font="Arial 28")
course_info.place(y=100, x=40)

course = Label(window, text="¥ " + getCourse("R01375"), font="Arial 36")
course.place(y=150, x=40)

label = Label(window, text="Курс юаня", bg="blue", fg="white", font="Arial 50").pack()
window.mainloop()