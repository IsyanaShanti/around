import tkinter
import tkintermapview
from PIL import Image, ImageTk
import os
from tkinter import ttk



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

map_widget.set_position(-6.28862, 106.71789)  # get coordinates
map_widget.set_zoom(10)

# Marker
marker_2 = map_widget.set_marker(-6.28862, 106.71789, icon=marker) # set coordinates for marker



# FRAME FOR WEATHER AND POLLUTION DATA
data = tkinter.Frame(root_tk, width=(width - 1200), height=(height - 300), borderwidth=1, relief="solid")
data.place(relx=0.1, rely=0.56, anchor=tkinter.W)
# frame.pack()


# FRAME FOR INPUT COUNTRY, STATE AND CITY
# input = tkinter.Frame(root_tk, width=(width - 1200), height=(height - 850), background='#EAE3CB')
# input.place(relx=0, rely=0, anchor=tkinter.W)

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

country = CustomEntry(root_tk)
country.config(font=('helvetica', 13))
canvas1.create_window(100, 177, window=country)

state = CustomEntry(root_tk)
state.config(font=('helvetica', 13))
canvas1.create_window(260, 177, window=state)

city = CustomEntry(root_tk)
city.config(font=('helvetica', 13))
canvas1.create_window(420, 177, window=city)


# style = ttk.Style()
# # print(style.layout("TEntry"))
# # print(style.layout("TSeparator"))


# label = tkinter.Label(input, text='First')
# # entry = CustomEntry(canvas1, width=20, highlightthickness=0)
# label.grid(row=1, column=0,)
# # entry.grid(row=row, column=1,)

root_tk.mainloop()