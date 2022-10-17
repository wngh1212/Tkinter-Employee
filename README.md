# tkinter-employee

Fake data for testing<br>
![image](https://user-images.githubusercontent.com/88926634/195977169-cbb55fc9-ddbe-4002-ac11-ad0cd8f88245.png)<br>
<pre><code>import tkinter as tk
import pymysql
from tkinter import messagebox
from tkinter import *
</code></pre>
필요한 모듈과 라이브러리를 import한다.<br>
<pre><code>root = tk.Tk()
root.geometry("300x300")
root.title("EBP")
root.configure(bg='#7978FF')
root.resizable(width=False,height=False)
</code></pre>
가장 기본으로 띄울 창을 만들어준다.<br>
check_data함수에 데이터 베이스를 연결하는 코드이다.<br>
check_data함수는 ID/PASS를 확인하고 MAIN화면을 여는 함수이다.<br>
<pre><code>def check_data():
    user = Username.get()
    passw = password.get()
    db = pymysql.connect(host ="localhost",user = 'root',password = '123456', db ="mem_db")
    cur = db.cursor()
    search = "select * from employee where emp_id = %s and emp_pass=%s"
    cur.execute(search,(user,passw))
    #위의 쿼리문에 get()으로 가져온데이터를 차례로 넣으며 비교
    r = cur.rowcount
     if r == 1:
        messagebox.showinfo(title='welcome',message='welcome' + ' ' + Username.get()) #Username에 입력받은 값을 가져와 출력
        root.destroy()
        #root라는 login창을 지운후 새로운 MAINFORM을 생성
        print('succesfully login')
        newsc = tk.Tk()
        newsc.title("MAIN FORM")
        newsc.geometry("1920x1080")
        newsc.configure(bg='#7978FF')
    else:
        messagebox.showinfo(title='none user data',message='please check for PASS/ID')
        print('check for your pass/id please')
        db.close()
</code></pre>
(root)EBP의 창에 포함된 입력받는 부분이나 버튼을 구현하는 코드들이다.
<code><pre>
lblfrst = tk.Label(root, text ="Username -",)
lblfrst.place(x = 50, y = 20)


Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)


lblsec = tk.Label(root, text ="Password -")
lblsec.place(x = 50, y = 50)


password = tk.Entry(root, width = 35,show='*')
password.place(x = 150, y = 50, width = 100)


submitbtn = tk.Button(root, text ="Login",bg ='#4649FF',fg='white',command =check_data)
submitbtn.place(x = 150, y = 135, width = 55)

root.mainloop()
</code></pre>
submitbtn에 command = check_data는 버튼을 눌렀을 때에 대해 지정한 (위의)함수를 실해하는 부분이다.
