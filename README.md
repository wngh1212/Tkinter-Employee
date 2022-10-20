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
check_data함수는 ID/PASS를 확인하고 창을 닫는 함수이다<br>
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
        #root라는 login창을 지움
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
submitbtn에 command = check_data는 버튼을 눌렀을 때에 대해 지정한 (위의)함수를 실행하는 부분이다.
<br>
<img width="614" alt="image" src="https://user-images.githubusercontent.com/88926634/196827558-cdcabef2-06f2-49c8-b05a-10fcddf55638.png"><br>
<img width="518" alt="image" src="https://user-images.githubusercontent.com/88926634/196827853-a1ba2e11-e98f-4f3b-b62b-20b6b3296c4c.png"><br>
<img width="723" alt="image" src="https://user-images.githubusercontent.com/88926634/196827907-8170bdb0-6d97-409b-afff-a7f84b6fe4e5.png"><br>
서버를 실행시키지 않고 클라이언트에서 로그인 후 텍스트를 보낼때<br>
<img width="795" alt="image" src="https://user-images.githubusercontent.com/88926634/196828139-e9a7eea4-55ce-4bae-aedb-6a506f16a8e8.png"><br>
서버를 실행 후에 클라이언트에 메세지를 보냈을때 클라이언트와 서버의 화면<br>
<img width="752" alt="image" src="https://user-images.githubusercontent.com/88926634/196828600-8e4b82a2-7845-495d-841e-6542f86e2eef.png">
<br>
system off를 클릭하면 애플리케이션이 종료가 된다.
<img width="145" alt="image" src="https://user-images.githubusercontent.com/88926634/196828930-7839fe22-da7a-466e-a732-84a2d191d611.png">
<br>
<img width="506" alt="image" src="https://user-images.githubusercontent.com/88926634/196829120-e44abf61-c7a3-4f1e-8275-7188774faa7b.png">






