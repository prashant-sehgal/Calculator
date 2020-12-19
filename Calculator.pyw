from tkinter import *

def keyClick(event):
    global textBoxValue
    text= event.widget.cget('text')

    if text == '=':
        if textBoxValue.get().isdigit():
            value = int(textBoxValue.get())
        else:
            value = eval(textbox.get())

        textBoxValue.set(value)
        textbox.update()
           
    elif text == 'Clear Pad':
        textBoxValue.set('')
        textBox.update()

    elif text == '÷':
        textBoxValue.set(textBoxValue.get() + '/')
        textBox.update()
        
    else:
        textBoxValue.set(textBoxValue.get() + text)
        textBox.update()

root = Tk()
root.title('Calculator')
root.wm_iconbitmap('calc.ico')

textBoxValue = StringVar()

textbox = Entry( root, font=('arial', 20, 'bold'), justify="right", bg='cyan',border= 10, textvariable = textBoxValue)
textbox.pack()

frame1 = Frame(root, pady=2)
frame1.pack()
frame2 = Frame(root, pady=2)
frame2.pack()
frame3 = Frame(root, pady=2)
frame3.pack()
frame4 = Frame(root, pady=2)
frame4.pack()
frame5 = Frame(root, pady=2)
frame5.pack()

button1 = Button(frame1, text="7", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button1.pack(side = LEFT)
button1.bind('<Button-1>', keyClick)

button2 = Button(frame1, text="8", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button2.pack(side = LEFT)
button2.bind('<Button-1>', keyClick)

button3 = Button(frame1, text="9", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button3.pack(side = LEFT)
button3.bind('<Button-1>', keyClick)

button4 = Button(frame1, text="+", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button4.pack(side = LEFT)
button4.bind('<Button-1>', keyClick)

button5 = Button(frame2, text="4", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button5.pack(side = LEFT)
button5.bind('<Button-1>', keyClick)

button6 = Button(frame2, text="5", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button6.pack(side = LEFT)
button6.bind('<Button-1>', keyClick)

button7 = Button(frame2, text="6", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button7.pack(side = LEFT)
button7.bind('<Button-1>', keyClick)

button8 = Button(frame2, text="-", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button8.pack(side = LEFT)
button8.bind('<Button-1>', keyClick)

button9 = Button(frame3, text="3", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button9.pack(side = LEFT)
button9.bind('<Button-1>', keyClick)

button10 = Button(frame3, text="2", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button10.pack(side = LEFT)
button10.bind('<Button-1>', keyClick)

button11 = Button(frame3, text="1", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button11.pack(side = LEFT)
button11.bind('<Button-1>', keyClick)

button12 = Button(frame3, text="*", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button12.pack(side = LEFT)
button12.bind('<Button-1>', keyClick)

button13 = Button(frame4, text=".", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button13.pack(side = LEFT)
button13.bind('<Button-1>', keyClick)

button14 = Button(frame4, text="0", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button14.pack(side = LEFT)
button14.bind('<Button-1>', keyClick)

button15 = Button(frame4, text="÷", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, command=keyClick)
button15.pack(side = LEFT)
button15.bind('<Button-1>', keyClick)

button16 = Button(frame4, text="=", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, bg='green', fg="white", command=keyClick)
button16.pack(side = LEFT)
button16.bind('<Button-1>', keyClick)

button16 = Button(frame5, text="Clear Pad", font=('arial', '20', 'bold'), border= 8, padx=15, pady=10, bg='#0026ff',fg="white", command=keyClick)
button16.pack(side = LEFT)
button16.bind('<Button-1>', keyClick)

root.mainloop()
