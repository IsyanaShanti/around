import tkinter
import tkintermapview
from PIL import Image, ImageTk
import os
from tkinter import ttk
import api


global aqius, lat, long


# GET NEAREST CITY WEATHER AND POLLUTION DATA
api.nearest_city()

aqius = api.near['data']['current']['pollution']['aqius']
lat = api.near['data']['location']['coordinates'][1]
long = api.near['data']['location']['coordinates'][0]
weather = api.near['data']['current']['weather']['ic']
tp = api.near['data']['current']['weather']['tp']
pr = api.near['data']['current']['weather']['pr']
hu = api.near['data']['current']['weather']['hu']
ws = api.near['data']['current']['weather']['ws']



if weather == '01d' :
    weather = 'clear sky (day)'
    fgt = ''
elif weather == '01n' :
    weather = 'clear sky (night)'
elif weather == '02d' :
    weather = 'few clouds (day)'
elif weather == '02n' :
    weather = 'few clouds (night)'
elif weather == '03d' or weather == '03n' :
    weather = 'scattered clouds'
elif weather == '04d' or weather == '04n':
    weather = 'broken clouds'
elif weather == '09d' or weather == '09d':
    weather = 'shower rain'
elif weather == '10d':
    weather = 'rain (day time)'
elif weather == '10n' :
    weather = 'rain (night time)'
elif weather == '11d' or weather == '11n':
    weather = 'thunderstorm'
elif weather == '13d' or weather == '13n':
    weather = 'snow'
elif weather == '50d' or  weather == '50n':
    weather = 'mist'

# CREATE AND SETTING TK WINDOWS
root_tk = tkinter.Tk()
root_tk.title("map_view_example.py")

width= root_tk.winfo_screenwidth()
height= root_tk.winfo_screenheight()

root_tk.geometry("%dx%d+%d+%d" % (width, height, 0, 0))



# MAP WIDGET    
map_widget = tkintermapview.TkinterMapView(root_tk, width=(width - 1200), height=(height - 300), corner_radius=20)
map_widget.place(relx=0.51, rely=0.56, anchor=tkinter.W) # map position

current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
marker = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "assets", "marker.png")).resize((40, 40)))

map_widget.set_position(lat, long)  # get coordinates
map_widget.set_zoom(10)

# Marker
marker = map_widget.set_marker(lat, long, icon=marker) # set coordinates for marker


# FRAME FOR WEATHER AND POLLUTION DATA
data = tkinter.Canvas(root_tk,  width=(width - 1200), height=(height - 300), borderwidth=1, relief="solid")
data.place(relx=0.1, rely=0.56, anchor=tkinter.W)

#air quallity bar

if aqius <= 50:
    bar_color = '#BDDAB1'
    bar_text = 'Good'
    bar_face = os.path.join(current_path, "assets", "good.png")
elif aqius > 50 and aqius <=100:
    bar_color = '#F4F19F'
    bar_text = 'Moderate'
    bar_face = os.path.join(current_path, "assets", "moderate.png")
elif aqius > 100 and aqius <=150:
    bar_color = '#F4D19F'
    bar_text = 'Unhealthy\nfor sensitive groups'
    bar_face = os.path.join(current_path, "assets", "sensitive.png")
elif aqius > 150 and aqius <=200:
    bar_color = '#E1CCCA'
    bar_text = 'Unhealthy'
    bar_face = os.path.join(current_path, "assets", "unhealthy.png")
elif aqius > 200 and aqius <=300:
    bar_color = '#C4BEC0'
    bar_text = 'Very Unhealthy'
    bar_face = os.path.join(current_path, "assets", "very_unhealthy.png")
elif aqius >= 301:
    bar_color = '#B6AAA4'
    bar_text = 'Hazardous'
    bar_face = os.path.join(current_path, "assets", 'hazardous.png')




bar = tkinter.Canvas(data,  width=(width - 1200), height=(height - 900), borderwidth=1, relief='solid', background=bar_color)
bar.place(relx=0, rely=0.12, anchor=tkinter.W)

usaqi_label = tkinter.Label(text = "US AQI", background=bar_color,  fg='#3B3933')
usaqi = tkinter.Label(text = aqius, background=bar_color, font='bold')
usaqi.config(font=('Segoe UI Variable Display Semib', 58))
bar.create_window(55, 35, window=usaqi_label)
bar.create_window(80, 107, window=usaqi)

text = tkinter.Label(text = bar_text, background=bar_color)
text.config(font=('Segoe UI Variable Text Light', 27))
bar.create_window(355,90, window=text)

aqii = tkinter.Label(text = "AQI Index", background=bar_color,  fg='#3B3933')
bar.create_window(650, 35, window=aqii)

face_img = ImageTk.PhotoImage(Image.open(bar_face).resize((100, 100)))
face = tkinter.Label(image = face_img, background=bar_color)
bar.create_window(650, 110, window=face)


#weather data
ystart = 350
weather_label_w = tkinter.Label(text = "Weather", fg='#3B3933', justify='left')
weather_label_w.config(font=('Segoe UI Variable Text Light', 15))
weather_data_w = tkinter.Label(text = weather, fg='#3B3933', font='bold')
weather_data_w.config(font=('Segoe UI Variable Display Semib', 15))
data.create_window(120, ystart, window=weather_label_w, anchor='w')
data.create_window(572, ystart, window=weather_data_w, anchor='e')
data.create_line(120, ystart+20, 570, ystart+20)
ystart = ystart + 50

weather_label_tp = tkinter.Label(text = "Temperature", fg='#3B3933',bd=1, justify='right')
weather_label_tp.config(font=('Segoe UI Variable Text Light', 15))
weather_data_tp = tkinter.Label(text = str(tp) + '°C', fg='#3B3933', font='bold')
weather_data_tp.config(font=('Segoe UI Variable Display Semib', 15))
data.create_window(120, ystart, window=weather_label_tp, anchor='w')
data.create_window(572, ystart, window=weather_data_tp, anchor='e')
data.create_line(120, ystart+20, 570, ystart+20)

ystart = ystart + 50

weather_label_pr = tkinter.Label(text = "Pressure", fg='#3B3933')
weather_label_pr.config(font=('Segoe UI Variable Text Light', 15))
weather_data_pr = tkinter.Label(text = str(pr) + ' mbar', fg='#3B3933', font='bold')
weather_data_pr.config(font=('Segoe UI Variable Display Semib', 15))
data.create_window(120, ystart, window=weather_label_pr, anchor='w')
data.create_window(572, ystart, window=weather_data_pr, anchor='e')
data.create_line(120, ystart+20, 570, ystart+20)

ystart = ystart + 50

weather_label_hu = tkinter.Label(text = "Humidity", fg='#3B3933')
weather_label_hu.config(font=('Segoe UI Variable Text Light', 15))
weather_data_hu = tkinter.Label(text = str(hu) + ' %', fg='#3B3933', font='bold')
weather_data_hu.config(font=('Segoe UI Variable Display Semib', 15))
data.create_window(120, ystart, window=weather_label_hu, anchor='w')
data.create_window(572, ystart, window=weather_data_hu, anchor='e')
data.create_line(120, ystart+20, 570, ystart+20)

ystart = ystart + 50

weather_label_ws = tkinter.Label(text = "Wind", fg='#3B3933')
weather_label_ws.config(font=('Segoe UI Variable Text Light', 15))
weather_data_ws = tkinter.Label(text = str(ws) + ' km/h', fg='#3B3933', font='bold')
weather_data_ws.config(font=('Segoe UI Variable Display Semib', 15))
data.create_window(120, ystart, window=weather_label_ws, anchor='w')
data.create_window(572, ystart, window=weather_data_ws, anchor='e')
data.create_line(120, ystart+20, 570, ystart+20)


# FRAME FOR INPUT COUNTRY, STATE AND CITY
class CustomEntry(tkinter.Entry):
    def __init__(self, *args, **kwargs):
        kwargs["borderwidth"] = 0
        kwargs["background"] = '#EAE3CB'
        kwargs["width"] = 10
        super().__init__(*args, **kwargs)
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self, x=0, rely=1.0, height=2, relwidth=1.0)

canvas1 = tkinter.Canvas(root_tk,  width=(width - 1200), height=(height - 850), background='#EAE3CB')
canvas1.place(relx=0, rely=0, anchor=tkinter.W)

  


country_label = tkinter.Label(text = "Country", background='#EAE3CB', fg='#3B3933').place(x = 35, y = 22) 
country = CustomEntry(root_tk)
country.config(font=('helvetica', 13))
canvas1.create_window(100, 185, window=country)
canvas1.create_window(0, 0, window=country_label)

state_label = tkinter.Label(text = "State", background='#EAE3CB', fg='#3B3933').place(x = 194, y = 22) 
state = CustomEntry(root_tk)
state.config(font=('helvetica', 13))
canvas1.create_window(260, 185, window=state)
canvas1.create_window(0, 0, window=state_label)

city_label = tkinter.Label(text = "City", background='#EAE3CB', fg='#3B3933').place(x = 353, y = 22) 
city = CustomEntry(root_tk)
city.config(font=('helvetica', 13))
canvas1.create_window(420, 185, window=city)
canvas1.create_window(0, 0, window=city_label)

# For Image
good = ImageTk.PhotoImage(Image.open('./assets/good.png').resize((100, 100)))
moderate = ImageTk.PhotoImage(Image.open('./assets/moderate.png').resize((100, 100)))
sensitive = ImageTk.PhotoImage(Image.open('./assets/sensitive.png').resize((100, 100)))
unhealthy = ImageTk.PhotoImage(Image.open('./assets/unhealthy.png').resize((100, 100)))
very_unhealthy = ImageTk.PhotoImage(Image.open('./assets/very_unhealthy.png').resize((100, 100)))
hazardous = ImageTk.PhotoImage(Image.open('./assets/hazardous.png').resize((100, 100)))


#Submit Button command
def submit():

    Country = country.get()
    State = state.get()
    City = city.get()
    api.iqair(Country, State, City)   

    aqius = api.data['data']['current']['pollution']['aqius']
    lat = api.data['data']['location']['coordinates'][1]
    long = api.data['data']['location']['coordinates'][0]

    #Map Settings
    map_widget.set_position(lat, long)  #get coordinates
    map_widget.set_zoom(10)
    marker.set_position(lat, long) # set coordinates for marker

    #Air quallity bar settings

    if aqius <= 50:
        bar_color = '#BDDAB1'
        bar_text = 'Good'
        face.configure(image=good)
    elif aqius > 50 and aqius <=100:
        bar_color = '#F4F19F'
        bar_text = 'Moderate'
        face.configure(image=moderate)
    elif aqius > 100 and aqius <=150:
        bar_color = '#F4D19F'
        bar_text = 'Unhealthy\nfor sensitive groups'
        face.configure(image=sensitive)
    elif aqius > 150 and aqius <=200:
        bar_color = '#E1CCCA'
        bar_text = 'Unhealthy'
        face.configure(image=unhealthy)
    elif aqius > 200 and aqius <=300:
        bar_color = '#C4BEC0'
        bar_text = 'Very Unhealthy'
        face.configure(image=very_unhealthy)
    elif aqius >= 301:
        bar_color = '#B6AAA4'
        bar_text = 'Hazardous'
        face.configure(image=hazardous)
    
    bar.config(background=bar_color)
    usaqi.config(text = aqius, background=bar_color)
    usaqi_label.config(background=bar_color)
    text.config(background=bar_color, text = bar_text)
    aqii.config(background=bar_color)
    face.config(background=bar_color)


    weather = api.data['data']['current']['weather']['ic']
    tp = api.data['data']['current']['weather']['tp']
    pr = api.data['data']['current']['weather']['pr']
    hu = api.data['data']['current']['weather']['hu']
    ws = api.data['data']['current']['weather']['ws']

    if weather == '01d' :
        weather = 'clear sky (day)'
    elif weather == '01n' :
        weather = 'clear sky (night)'
    elif weather == '02d' :
        weather = 'few clouds (day)'
    elif weather == '02n' :
        weather = 'few clouds (night)'
    elif weather == '03d' or weather == '03n' :
        weather = 'scattered clouds'
    elif weather == '04d' or weather == '04n':
        weather = 'broken clouds'
    elif weather == '09d' or weather == '09d':
        weather = 'shower rain'
    elif weather == '10d':
        weather = 'rain (day time)'
    elif weather == '10n' :
        weather = 'rain (night time)'
    elif weather == '11d' or weather == '11n':
        weather = 'thunderstorm'
    elif weather == '13d' or weather == '13n':
        weather = 'snow'
    elif weather == '50d' or  weather == '50n':
        weather = 'mist'



    weather_data_w.config(text= weather)
    weather_data_tp.config(text= str(tp) + '°C')
    weather_data_hu.config(text= str(hu) + ' %')
    weather_data_ws.config(text= str(ws) + ' km/h')
    weather_data_pr.config(text= str(pr) + ' mbar')

    

    


# Submit data
login_btn = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "assets", "submit.png")).resize((135, 50)))
img = tkinter.Button(image = login_btn, borderwidth = 0, background='#EAE3CB', activebackground='#EAE3CB', command=submit).place(x = 530, y = 32.5) 
canvas1.create_window(0, 0, window=img)


root_tk.mainloop()