from tkinter import *


def button_click():
    weight = int(weight_text.get())
    height = int(height_text.get())
    height_m = height/100
    Bmi = int(weight/(height_m**2))
    print(weight)
    print(height)
    print(height_m)
    print(Bmi)
    if Bmi < 19:
        Bmi_label.config(text="You are Underweight")
    if Bmi >=19 and Bmi < 25:
        Bmi_label.config(text="You are Normal")
    if Bmi >=25 and Bmi < 40:
        Bmi_label.config(text="You are OverWeight")
    if Bmi > 40:
        Bmi_label.config(text="You are Obese")
    Bmi_label.pack()



window = Tk()
window.title("Bmi calculator")
window.minsize(width=70,height=200)
window.config(padx=20,pady=20)

weight_label = Label(
    text="Enter you Weight(kg)",
    fg="black",
)
weight_label.pack()

weight_text = Entry(width=15)
weight_text.pack()

height_label = Label(
    text="Enter you Weight(cm)",
    fg="black",
)
height_label.pack()

height_text = Entry(width=15)
height_text.pack()



button=Button(text="Calculate",command=button_click)
button.pack()

Bmi_label = Label (fg="black")



window.mainloop()