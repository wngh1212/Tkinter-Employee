import tkinter as tk
import pymysql
from tkinter import messagebox
from tkinter import *


root = tk.Tk()
root.geometry("300x300")
root.title("EBP")
root.configure(bg='#7978FF')
root.resizable(width=False,height=False)



def check_data():
    user = Username.get()
    passw = password.get()
    db = pymysql.connect(host ="localhost",user = 'root',password = '123456', db ="mem_db")
    cur = db.cursor()
    search = "select * from employee where emp_id = %s and emp_pass=%s"
    cur.execute(search,(user,passw))
    r = cur.rowcount

    
    if r == 1:
        messagebox.showinfo(title='welcome',message='welcome' + ' ' + Username.get())
        root.destroy()
        print('succesfully login')
        newsc = tk.Tk()
        newsc.title("MAIN FORM")
        newsc.geometry("1920x1080")
        newsc.configure(bg='#7978FF')
        password1 = tk.Entry(newsc, width = 35)
        password1.place(x = 0, y = 50, width = 400,height=500)
    else:
        messagebox.showinfo(title='none user data',message='please check for PASS/ID')
        print('check for your pass/id please')
        db.close()



lblfrstrow = tk.Label(root, text ="Username -",)
lblfrstrow.place(x = 50, y = 20)


Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)


lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)


password = tk.Entry(root, width = 35,show='*')
password.place(x = 150, y = 50, width = 100)


submitbtn = tk.Button(root, text ="Login",bg ='#4649FF',fg='white',command =check_data)
submitbtn.place(x = 150, y = 135, width = 55)

root.mainloop()
