# from tkinter import *
# from tkinter import messagebox
# from PIL import Image,ImageTk
# from plyer import notification
# import time

# t=Tk()
# t.title("Notifier")
# t.geometry("500x400")
# # img=Image.open("notify_label.png")
# # Tkimg=ImageTk.PhotoImage(img)

# # img_label=Label(t,image=Tkimg).grid()
# #getdetails
# def get_Details():
#     get_title=title.get()
#     get_msg=msg.get()
#     get_time=time1.get()

#     if get_title=="" or get_msg==""or get_time=="":
#         messagebox.showerror("Alert","All feilds are required!")
#     else:
#         int_time=int(float(get_time))
#         min_to_sec=int_time*60
#         messagebox.showinfo("Notifier set","set notification")

#         time.sleep(min_to_sec)
#         notification.notify(title=get_title,
#                             message=get_msg,
#                             app_name="notifier",
#                             )
# #label1
# t_label=Label(t,text="Title to notify:",font=("poppins",10))
# t_label.place(x=12,y=12)

# #entry1
# title=Entry(t,width="35",font=("poppins",13))
# title.place(x=120,y=12)

# #label2
# m_label=Label(t,text="Dispaly message:",font=("poppins",10))
# m_label.place(x=12,y=60)

# #entry2
# msg=Entry(t,width="35",font=("poppins",13))
# msg.place(x=125,y=60,height=30)

# #Label 3
# time_label =Label(t,text="Set Time:",font=("poppins",10))
# time_label.place(x=12,y=125)
# #entry3
# time1=Entry(t,width="5",font=("poppins",13))
# time1.place(x=100,y=125)

# #label 4
# time_min_label=Label(t,text="min",font=("poppins",10))
# time_min_label.place(x=160,y=125)

# #button
# but=Button(t,text="SET NOTIFICATION",font=("poppins",18,"bold"),fg="#ffffff",bg="#528DFF",width=15,relief="raised",command=get_Details)
# but.place(x=120,y=230)
# t.resizable(0,0)
# t.mainloop()


from tkinter import *
from PIL import Image, ImageTk
from plyer import notification
from tkinter import messagebox
import time

t = Tk()
t.title('Notifier')
t.geometry("500x300")
img = Image.open('notify_label.png')
tkimage = ImageTk.PhotoImage(img)

# get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    # print(get_title,get_msg, tt)

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="ico.ico",
                            toast=True,
                            timeout=10)

# img_label = Label(t, image=tkimage).grid()

# Label - Title
t_label = Label(t, text="Title to Notify",font=("poppins", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title = Entry(t, width="25",font=("poppins", 13))
title.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123,height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

# ENTRY - Time
time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=123, y=175)

# Label - min
time_min_label = Label(t, text="min", font=("poppins", 10))
time_min_label.place(x=175, y=180)

# Button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()
