from tkinter import*
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลังของโปรแกรม
GUI.title('MANUSCRIPT WRITING PLAN')# นี่คือชื่อโปรแกรม
GUI.geometry('500x400')#นี่คือขนาดโปรแกรม


L1 = Label(GUI,text='ONE MONTH MANUSCRIPT WRITING PLAN',font=('Time new roman',15),fg='red')
L1.place(x=45,y=0)           
###############

#####################
def Button1():
            text = 'Materials and Methods'
            messagebox.showinfo('First week',text)

FB1 = LabelFrame(GUI)#คล้ายกระดาน
FB1.place(x=200,y=50)# button position
B1 = ttk.Button(FB1,text='First Week',command=Button1)
B1.pack(ipadx=21,ipady=20)
###################################
def Button2():
            text = 'Results and Discussion'
            messagebox.showinfo('Second week',text)



FB2 = LabelFrame(GUI)#คล้ายกระดาน
FB2.place(x=200,y=120)# button position
B2 = ttk.Button(FB2,text='Second week',command=Button2)
B2.pack(ipadx=20,ipady=20)

#################################
def Button3():
            text = 'Discussion and Introduction'
            messagebox.showinfo('Thrid week',text)



FB3 = LabelFrame(GUI)#คล้ายกระดาน
FB3.place(x=200,y=190)# button position
B3 = ttk.Button(FB2,text='Thrid week',command=Button3)
B3.pack(ipadx=20,ipady=20)

########################################
def Button4():
            text = 'Introduction and Conclusion'
            messagebox.showinfo('Fourth week',text)



FB4 = LabelFrame(GUI)#คล้ายกระดาน
FB4.place(x=200,y=250)# button position
B4 = ttk.Button(FB2,text='Fourth week',command=Button4)
B4.pack(ipadx=20,ipady=20)











GUI.mainloop()
