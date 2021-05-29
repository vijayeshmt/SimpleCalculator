"""
Code written by Vijayesh M T
Python code written using tkinter'
date: 28/05/21
Cons:Cannot calculate many value at a time
     cannot work with float values
Simple calculator which computes only integer
icon =https://iconarchive.com/tag/calculator
"""
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("250x400+300+300")

#To avoid resizing uncomment the below comment
# root.resizable(0, 0)
root.title("Calculator")
root.wm_iconbitmap("Calc.ico")
A = 0
val = ""
operator = ""


#functions

def btn_1_isclicked():
	global val
	val = val + "1"
	data.set(val)


def btn_2_isclicked():
	global val
	val = val + "2"
	data.set(val)


def btn_3_isclicked():
	global val
	val = val + "3"
	data.set(val)


def btn_4_isclicked():
	global val
	val = val + "4"
	data.set(val)


def btn_5_isclicked():
	global val
	val = val + "5"
	data.set(val)


def btn_6_isclicked():
	global val
	val = val + "6"
	data.set(val)


def btn_plus_clicked():
	global A
	global val
	global operator
	A = int(val)
	operator = "+"
	val = val + "+"
	data.set(val)


def btn_minus_clicked():
	global A
	global val
	global operator
	A = int(val)
	operator = "-"
	val = val + "-"
	data.set(val)


def btn_mul_clicked():
	global A
	global val
	global operator
	A = int(val)
	operator = "x"
	val = val + "x"
	data.set(val)


def btn_div_clicked():
	global A
	global val
	global operator
	A = int(val)
	operator = "/"
	val = val + "/"
	data.set(val)


def btn_7_isclicked():
	global val
	val = val + "7"
	data.set(val)


def btn_8_isclicked():
	global val
	val = val + "8"
	data.set(val)


def btn_9_isclicked():
	global val
	val = val + "9"
	data.set(val)


def btn_0_isclicked():
	global val
	val = val + "0"
	data.set(val)


def c_pressed():
	global A
	global val
	global operator
	val = ""
	A = 0
	operator = ""
	data.set(val)


def result():
	global A
	global val
	global operator
	val2 = val
	if operator == "+":
		x = int((val2.split("+")[1]))
		c = A + x
		data.set(c)
		val = str(c)
	elif operator == "-":
		x = int((val2.split("-")[1]))
		c = A - x
		data.set(c)
		val = str(c)
	elif operator == "x":
		x = int((val2.split("x")[1]))
		c = A * x
		data.set(c)
		val = str(c)
	elif operator == "/":
		x = int((val2.split("/")[1]))
		if x == 0:
			messagebox.showerror("Error", "Division by zero is not possible")
			A = ""
			val = ""
			data.set(val)
		else:
			c = A / x
			d = format(c, ".4f")
			data.set(d)
			val = str(d)


data = StringVar()
lbl = Label(root,
            text="Label",
            anchor=SE,
            border=1,
            relief=SUNKEN,
            padx=5,
            textvariable=data,
            bg="#ffffff",
            fg="#000000",
            font=("Verdana", 22, "bold")
            )
lbl.pack(expand=True, fill="both",
         padx=5)

# Frame
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill="both", )

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill=BOTH)

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill=BOTH)

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill=BOTH)

# Buttons
btn7 = Button(btnrow1, text="7", border=0, command=btn_7_isclicked,fg="#ff77a9", relief=GROOVE, font=("Verdana", 22, "bold"))
btn7.pack(side=LEFT, expand=True, fil="both")
btn8 = Button(btnrow1, text="8", border=0, command=btn_8_isclicked,fg="#1a237e", relief=GROOVE, font=("Verdana", 22, "bold"))
btn8.pack(side=LEFT, expand=True, fil="both")
btn9 = Button(btnrow1, text="9", border=0, command=btn_9_isclicked,fg="#ff6f00", relief=GROOVE, font=("Verdana", 22, "bold"))
btn9.pack(side=LEFT, expand=True, fil="both")
btnx = Button(btnrow1, text="x", border=0, relief=GROOVE,fg="#002984", command=btn_mul_clicked, font=("Verdana", 22, "bold"))
btnx.pack(side=LEFT, expand=True, fil="both")

btn4 = Button(btnrow2, text="4", border=0, relief=GROOVE,fg="#7953d2", command=btn_4_isclicked, font=("Verdana", 22, "bold"))
btn4.pack(side=LEFT, expand=True, fil="both")
btn5 = Button(btnrow2, text="5", border=0, command=btn_5_isclicked,fg="#c2185b", relief=GROOVE, font=("Verdana", 22, "bold"))
btn5.pack(side=LEFT, expand=True, fil="both")
btn6 = Button(btnrow2, text="6", border=0, relief=GROOVE,fg="#9e00c5", command=btn_6_isclicked, font=("Verdana", 22, "bold"))
btn6.pack(side=LEFT, expand=True, fil="both")
btnminus = Button(btnrow2, text="-", border=0, relief=GROOVE, fg="#f4511e",command=btn_minus_clicked, font=("Verdana", 22, "bold"))
btnminus.pack(side=LEFT, expand=True, fil="both")

btn1 = Button(btnrow3, text="1", border=0, command=btn_1_isclicked,fg="#d50000",relief=GROOVE, font=("Verdana", 22, "bold"))
btn1.pack(side=LEFT, expand=True, fil="both")
btn2 = Button(btnrow3, text="2", border=0, relief=GROOVE,fg="#29b6f6", command=btn_2_isclicked, font=("Verdana", 22, "bold"))
btn2.pack(side=LEFT, expand=True, fil="both")
btn3 = Button(btnrow3, text="3", border=0, relief=GROOVE, fg="#880e4f",command=btn_3_isclicked, font=("Verdana", 22, "bold"))
btn3.pack(side=LEFT, expand=True, fil="both")
btnplus = Button(btnrow3, text="+", border=0, relief=GROOVE,fg="#fbc02d", command=btn_plus_clicked, font=("Verdana", 22, "bold"))
btnplus.pack(side=LEFT, expand=True, fil="both")

btnzero = Button(btnrow4, text="0", border=0, command=btn_0_isclicked,fg="#ffc400", relief=GROOVE, font=("Verdana", 22, "bold"))
btnzero.pack(side=LEFT, expand=True, fil="both")
btn2 = Button(btnrow4, text="C", border=0, relief=GROOVE,fg="#ff6d00", command=c_pressed, font=("Verdana", 22, "bold"))
btn2.pack(side=LEFT, expand=True, fil="both")
btn3 = Button(btnrow4, text="=", border=0, relief=GROOVE,fg="#455a64", command=result, font=("Verdana", 22, "bold"))
btn3.pack(side=LEFT, expand=True, fil="both")
btn4 = Button(btnrow4, text="/", border=0, relief=GROOVE,fg="#00e5ff", command=btn_div_clicked, font=("Verdana", 22, "bold"))
btn4.pack(side=LEFT, expand=True, fil="both")

root.mainloop()
