import socket
from _thread import *
import threading
from tkinter import *
from time import sleep
#import toyproject

def send(socket):
    global go_send
    while True:
        if go_send:
            message = (message_input.get(1.0,"end")).rstrip()
            socket.send(message.encode())
            message_input.delete(1.0, "end")
            go_send = False
        else:
            if go_out:
                socket.close()
                exit()
            sleep(0.1)

def receive(socket):
    first = True
    while True:
        try:
            data = socket.recv(1024)
            chat_log['state'] = 'normal'
            if first:
                chat_log.insert("end",str(data.decode( )))
                first = False
            else:
                chat_log.insert("end",'\n' + str(data.decode()))
                chat_log.see('end')
            chat_log['state'] = 'disabled'
        except ConnectionAbortedError as e:
            chat_log['state'] = 'normal'
            chat_log.insert("end", '\n[System]  desconecting.\n')
            chat_log['state'] = 'disabled'
            exit()

def login():
    
    HOST = ip_entry.get(); PORT = int(port_entry.get())
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    threading.Thread(target=send, args= (client_socket,)).start()
    threading.Thread(target=receive, args= (client_socket,)).start()
    exit()

def try_login():
    global go_out
    start_new_thread(login,())
    login_button['state'] = 'disabled'
    logout_button['state'] = 'active'
    ip_entry['state'] = 'readonly'
    port_entry['state'] = 'readonly'
    go_out = False

def try_logout():
    global go_out
    login_button['state'] = 'active'
    logout_button['state'] = 'disabled'
    ip_entry['state'] = 'normal'
    port_entry['state'] = 'normal'
    go_out = True

def set_go_send(event):
    global go_send
    go_send = True

go_out, go_send = False, False
c_root = Toplevel()
c_root.geometry('500x500')
c_root.title('Client')
c_root.resizable(False, False)

''' Top Menu '''
Label(c_root, text = 'Server IP : ').place(x=20, y=20)
Label(c_root, text = 'Port : ').place(x=250, y=20)
ip_entry = Entry(c_root, width=14); ip_entry.place(x=83, y=21)
ip_entry.insert(0,'127.0.0.1')
port_entry = Entry(c_root, width=5); port_entry.place(x = 290, y=21)
port_entry.insert(0,'8080')
login_button = Button(c_root,text='Log In', command=try_login); login_button.place(x=350, y=18)
logout_button = Button(c_root,text='Log Out',state = 'disabled', command = try_logout); logout_button.place(x=420, y=18)

''' Middle Menu '''
chat_frame = Frame(c_root)
scrollbar = Scrollbar(chat_frame) ; scrollbar.pack(side='right',fill='y')
chat_log = Text(chat_frame, width = 62, height = 24, state = 'disabled', yscrollcommand = scrollbar.set) ; chat_log.pack(side='left')#place(x=20, y=60)
scrollbar['command'] = chat_log.yview
chat_frame.place(x=20, y=60)
message_input = Text(c_root, width = 55, height = 4) ; message_input.place(x=20,y = 390)
send_button = Button(c_root, text = 'Send', command = lambda: set_go_send(None)); send_button.place(x=430, y=405)
message_input.bind("<Return>",set_go_send)

clse_button = Button(c_root,text='Close',command=exit); clse_button.place(x=200, y = 460)

#c_root.mainloop()
