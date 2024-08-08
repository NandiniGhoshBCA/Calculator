from tkinter import*
win=Tk()
win.geometry("300x300")
win.title("Calculator")
#img=photoImage(file='dowmload.png)
#win.iconphoto(0,img)
win.resizable(0,0)
f=Frame(win,height=200,width=240)
f.place(x=40,y=60)

expression=""
var=StringVar()
def btn_click(num):
    global expression
    expression=expression+str(num)
    var.set(expression)
   
def bt_clear():
    global expression
    var.set('')
    expression=""
   
def equals():
    global expression
    total=str(eval(expression))
    var.set(total)
    expression=total
   
#input field
input_text=Entry(win,textvariable=var,font="Normal")
input_text.place(x=50,y=15,width=190,height=40)

#row 1 buttons
b1=Button(f,text="1",font="Normal",padx=5,pady=5,command=lambda:btn_click('1'))
b1.grid(row=0,column=0,ipadx=5,ipady=5)
b2=Button(f,text="2",font="Normal",padx=5,pady=5,command=lambda:btn_click('2'))
b2.grid(row=0,column=1,ipadx=5,ipady=5)
b3=Button(f,text="3",font="Normal",padx=5,command=lambda:btn_click('3'))
b3.grid(row=0,column=2,ipadx=5,ipady=5)
bsum=Button(f,text='+',font="Normal",padx=5,pady=5,command=lambda:btn_click('+'))
bsum.grid(row=0,column=3,ipadx=5,ipady=5)

#row 2 buttons
b4=Button(f,text="4",font="Normal",padx=5,pady=5,command=lambda:btn_click('4'))
b4.grid(row=1,column=0,ipadx=5,ipady=5)
b5=Button(f,text="5",font="Normal",padx=5,pady=5,command=lambda:btn_click('5'))
b5.grid(row=1,column=1,ipadx=5,ipady=5)
b6=Button(f,text="6",font="Normal",padx=5,command=lambda:btn_click('6'))
b6.grid(row=1,column=2,ipadx=5,ipady=5)
bsub=Button(f,text='-',font="Normal",padx=5,pady=5,command=lambda:btn_click('-'))
bsub.grid(row=1,column=3,ipadx=5,ipady=5)

#button row 3
b7=Button(f,text="7",font="Normal",padx=5,pady=5,command=lambda:btn_click('7'))
b7.grid(row=2,column=0,ipadx=5,ipady=5)
b8=Button(f,text="8",font="Normal",padx=5,pady=5,command=lambda:btn_click('8'))
b8.grid(row=2,column=1,ipadx=5,ipady=5)
b9=Button(f,text="9",font="Normal",padx=5,command=lambda:btn_click('9'))
b9.grid(row=2,column=2,ipadx=5,ipady=5)
bmul=Button(f,text='*',font="Normal",padx=5,pady=5,command=lambda:btn_click('*'))
bmul.grid(row=2,column=3,ipadx=5,ipady=5)

#button of row 4
b_ce=Button(f,text="CE",font="Normal",padx=5,pady=5,command=bt_clear)
b_ce.grid(row=3,column=0,ipadx=5,ipady=5)
b_0=Button(f,text="0",font="Normal",padx=5,pady=5,command=lambda:btn_click('0'))
b_0.grid(row=3,column=1,ipadx=5,ipady=5)
b_eq=Button(f,text="=",font="Normal",padx=5,command=equals)
b_eq.grid(row=3,column=2,ipadx=5,ipady=5)
bdiv=Button(f,text='/',font="Normal",padx=5,pady=5,command=lambda:btn_click('/'))
bdiv.grid(row=3,column=3,ipadx=5,ipady=5)

win.mainloop() 