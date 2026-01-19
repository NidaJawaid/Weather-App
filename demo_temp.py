from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=667f605489a2a70672adc2446da2012a").json()
    w_label1.config(text=data["weather"][0]["main"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pressure_label1.config(text=data["main"]["pressure"])






win=Tk()
win.title("weather app")
win.config(bg="blue")
win.geometry("500x500")

name_label=Label(win,text="weather app",
                 font=("times new roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
city_name=StringVar()

list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

#combo box
com=ttk.Combobox(win,text="weather app",values=list_name,
                 font=("times new roman",30,"bold"),textvariable=city_name)
com.place(x=25,y=150,height=50,width=450)


w_label=Label(win,text="weather",
                 font=("times new roman",15))
w_label.place(x=25,y=300,height=30,width=100)

w_label1=Label(win,text="",
                 font=("times new roman",15))
w_label1.place(x=250,y=300,height=30,width=100)

temp_label=Label(win,text="temperature",
                 font=("times new roman",15))
temp_label.place(x=25,y=340,height=30,width=100)

temp_label1=Label(win,text="",
                 font=("times new roman",15))
temp_label1.place(x=250,y=340,height=30,width=100)


pressure_label=Label(win,text="pressure",
                 font=("times new roman",15))
pressure_label.place(x=25,y=380,height=30,width=100)

pressure_label1=Label(win,text="",
                 font=("times new roman",15))
pressure_label1.place(x=250,y=380,height=30,width=100)



#button banayenge jisko dabane ke baad state choose kiya rahega uska weather batayega
#button bnane ko button naam ka function hai
done_button=Button(win,text="done",
                 font=("times new roman",30,"bold"),command=data_get)
done_button.place(x=205,y=230,height=50,width=100)

#ab kya kya dikhana hai about weather of that place






win.mainloop() 