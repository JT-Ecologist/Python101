from tkinter import*
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลังของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')# นี่คือชื่อโปรแกรม
GUI.geometry('500x400')#นี่คือขนาดโปรแกรม


L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='red')
L1.place(x=30,y=20)           
###############
B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)# button position and size
#####################
def Button2():
            text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
            messagebox.showinfo('เงินในบัญชี',text)



FB1 = LabelFrame(GUI)#คล้ายกระดาน
FB1.place(x=100,y=300)# button position
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
###################################
def Button3():
            text = 'Python 101 Math'
            messagebox.showinfo('วิชาที่เรียน 10-20 ก.พ.',text)



FB2 = LabelFrame(GUI)#คล้ายกระดาน
FB2.place(x=100,y=100)# button position
B3 = ttk.Button(FB2,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)






GUI.mainloop()


 

