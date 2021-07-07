from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys


rt = Tk() 
rt.title("Calculator")
bn_lt = [
"bin", "CC","+/-", "%" ,
"9", "8", "7", "-",
"6", "5", "4", "+", 
"3", "2", "1", "*",
"0", ".", "=",  "/",
"(", ")",   
"cos", "sin", "tan" ,
"log" , "ln","ctg", ]
r = 1
c = 0
for i in bn_lt:
    rel = ""
    cmd=lambda x=i: cc(x)
    ttk.Button(rt, text=i, command = cmd, width = 10 ).grid(row=r, column = c)
    c += 1
    if c > 3:
        c = 0
        r += 1


cc_w = Entry(rt, width = 30)
cc_w.grid(row=0, column=0, columnspan=4)
def cc(key):
    global memory
    if key == "=":

        str1 = "-+0123456789.*/)(" 
        if cc_w.get()[0] not in str1:
            cc_w.insert(END, "Перший символ - це не число!")
            messagebox.showerror("Помилка!", "Не число!")

        try:
            result = eval(cc_w.get())
            cc_w.insert(END, "=" + str(result))
        except:
            cc_w.insert(END, "Помилка!")
            messagebox.showerror("Помилка!", "Перевірте правил. даних")

    elif key == "CC":
        cc_w.delete(0, END)
    elif key == "±":
        if "=" in cc_w.get():
            cc_w.delete(0, END)
        try:
            if cc_w.get()[0] == "-":
                cc_w.delete(0)
            else:
                cc_w.insert(0, "-")
        except IndexError:


            pass
    elif key == "sin":
        cc_w.insert(END, "=" + str(math.sin(int(cc_w.get()))))
    elif key == "cos":
        cc_w.insert(END, "=" + str(math.cos(int(cc_w.get()))))
    elif key == "tan":
        cc_w.insert(END, "=" + str(math.tan(int(cc_w.get()))))
    elif key == "ctg":
        cc_w.insert(END, "=" + str((math.cos(int(cc_w.get()))/(math.sin(int(cc_w.get()))))))
    elif key == "(":
        cc_w.insert(END, "(")
    elif key == ")":
        cc_w.insert(END, ")")
    elif key == "log":
        cc_w.insert(END, "=" + str(math.log(int(cc_w.get()))))
    elif key == "ln":
        cc_w.insert(END, "=" + str(math.log10(int(cc_w.get()))))
    elif key == "%":
        cc_w.insert(END, "=" + str(int(cc_w.get())*(int(cc_w.get())/100)))
    elif key == "bin":
        cc_w.insert(END, "=" + bin(int(cc_w.get())))
    else:


        if "=" in cc_w.get():
            cc_w.delete(0, END)
        cc_w.insert(END, key)
        rt.mainloop()