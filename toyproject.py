import tkinter as tk
import pymysql
from tkinter import messagebox
from tkinter import *
#import server
#import client

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

#-----------delete loginform...after------------
root.mainloop()
newsc = tk.Tk()
newsc.title("MAIN FORM")
newsc.geometry("600x600")
newsc.configure(bg='#7978FF')
def open_ser():
    import server #interesting module error but...is not errors!!!....temporary Solution! Beacause....module is one calling!!
    server
def system_of():
    newsc.destroy()

def open_cli():
    import client
server_op = Button(newsc,text="open server",command=open_ser)
server_op.pack()

client_op = Button(newsc,text="open chat client",command=open_cli)
client_op.pack()

system_off = Button(newsc,text="system off",command=system_of).pack()
newsc.mainloop()