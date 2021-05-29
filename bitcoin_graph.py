
# https://matplotlib.org/2.0.2/examples/user_interfaces/embedding_in_tk_canvas.html

import tkinter
import tkinter as tk
from tkinter import Tk,Label
from PIL import Image,ImageTk
from PIL import *
import requests
import matplotlib.pyplot as plt
import tkinter.font as font
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame

#root window
root = tkinter.Tk()
root.title('Bitcoin')
root.configure(width = 800,height = 460)

#canvas
canvas = tk.Canvas(root)
canvas.configure(bg ='black')
canvas.place(relwidth =1,relheight=1)

#image
imag = ImageTk.PhotoImage(file ='bitcoin.png')
image_label = Label(canvas,image = imag)
image_label.place(relwidth=1,relheight=1)

# for graph
x_values = []
y_values = []

#format function
def format(response):
    try:
        btc = response['BTC']
        x_values.append(btc)
    except:
        final_str = 'There was an error'
    final_str = 'BTC: %s'%(btc)
    return(final_str)
def Nepal(response):
    us = response['USD']
    nep = (117.22)*us
    final = 'NRs: %s'%nep
    return(final)


#tracker function
def tracker():
    global canvas
    global x_values
    global y_values
    url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR'
    response = requests.get(url).json()
    frame2 = Label(canvas,text = format(response),font=('arial',15,'bold'),bg ='#A64D79')
    frame2.place(relx=0.07, rely=0.34, relheight=0.09, relwidth=0.2)
    frame3 =Label(canvas,text = Nepal(response),font=('arial',15,'bold'),anchor = 'w',bg ='#A64D79')
    frame3.place(relx=0.07, rely=0.53, relheight=0.09, relwidth=0.25)
    time = datetime.now().strftime('%H:%M:%S')
    y_values.append(time)
    frame4 = Label(canvas, text='Updated at: %s' % (time), font=('arial', 15, 'bold'),bg ='#A64D79')
    frame4.place(relx=0.07, rely=0.73, relheight=0.09, relwidth=0.30)
    frame5 = tk.Frame(canvas)
    frame5.place(relx=0.38, rely=0.1, relheight=0.8, relwidth=0.55)

    figure = plt.Figure(figsize=(7.4,6.2), dpi=60)
    figure.patch.set_facecolor('xkcd:mint green')
    ax = figure.add_subplot(111)
    ax.set_facecolor('#A64D79')
    ax.plot(x_values,color = 'xkcd:mint green',linewidth=3,marker = '.',markersize = 20,markeredgecolor = 'black',linestyle='--')
    chart_type = FigureCanvasTkAgg(figure,frame5)
    chart_type.get_tk_widget().pack()

    canvas.after(1000, tracker)

    # graph = plt.plot(time,response['BTC'])
    # graph.place(frame5)

    #label1 = Label(canvas,text = format(response),font = ('Arial',15,'bold'))
    # label1.place(relx = 0.05,rely=0.3,relheight=0.2,relwidth=0.2)

#frame1
frame1 = tk.Frame(canvas)
frame1.place(relx = 0.07,rely=0.16,relheight=0.09,relwidth=0.2)
btn = tk.Button(frame1,text ='Start',font =('Arial',20,'bold'),bd = 5,command = tracker,bg ='#A64D79')
btn.place(relheight=1,relwidth=1)



root.mainloop()
