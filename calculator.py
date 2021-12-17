from tkinter import*
window=Tk()
window.title("simple calculator")
e=Entry(window,width=35,borderwidth=5 )
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    return
def button_delete():
    e.delete(0,END)
def button_add():
    first_number=e.get()
    global f_num
    f_num = int(first_number)
    global math
    math="addition"
    e.delete(0,END)
def button_sub():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "subtraction"
    e.delete(0, END)
    return
def button_mul():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "multiply"
    e.delete(0, END)
    return
def button_div():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "divide"
    e.delete(0, END)
    return
def button_rem():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "remainder"
    e.delete(0, END)
    return
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,int(second_number)+f_num)
    if math=="subtraction":
        e.insert(0,f_num-int(second_number))
    if math=="multiply":
        e.insert(0,int(second_number)*f_num)
    if math == "divide":
        e.insert(0, f_num / int(second_number))
    if math == "remainder":
        e.insert(0, f_num % int(second_number))
    return
button1=Button(window,text="1",padx=30,pady=10,command=lambda:button_click(1))
button2=Button(window,text="2",padx=30,pady=10,command=lambda:button_click(2))
button3=Button(window,text="3",padx=30,pady=10,command=lambda:button_click(3))
button4=Button(window,text="4",padx=30,pady=10,command=lambda:button_click(4))
button5=Button(window,text="5",padx=30,pady=10,command=lambda:button_click(5))
button6=Button(window,text="6",padx=30,pady=10,command=lambda:button_click(6))
button7=Button(window,text="7",padx=30,pady=10,command=lambda:button_click(7))
button8=Button(window,text="8",padx=30,pady=10,command=lambda:button_click(8))
button9=Button(window,text="9",padx=30,pady=10,command=lambda:button_click(9))
button0=Button(window,text="0",padx=30,pady=10,command=lambda:button_click(0))
buttonrem=Button(window,text="%",padx=30,pady=10,command=button_rem)
buttonadd=Button(window,text="+",padx=20,pady=35,command=button_add)
buttonsub=Button(window,text="-",padx=20,pady=10,command=button_sub)
buttonmul=Button(window,text="*",padx=30,pady=10,command=button_mul)
buttondiv=Button(window,text="/",padx=30,pady=10,command=button_div)
buttonclr=Button(window,text="clear",padx=59,pady=10,command=button_delete)
buttoneq=Button(window,text="=",padx=20,pady=35,command=button_equal)
button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
button0.grid(row=5,column=0)
buttonrem.grid(row=1,column=0)
buttonadd.grid(row=2,column=3,rowspan=2)
buttonsub.grid(row=1,column=3)
buttonmul.grid(row=1,column=2)
buttondiv.grid(row=1,column=1)
buttonclr.grid(row=5,column=1,columnspan=2)
buttoneq.grid(row=4,column=3,rowspan=2)
window.mainloop()
