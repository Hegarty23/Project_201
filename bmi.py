from tkinter import *
window=Tk()
window.title("BMI calculator")
window.geometry("400x400")
window.configure(bg="lightcyan")
def calculate_bmi():
    w=int(weight.get())
    h=int(height.get())/100
    bmi=w/(h*h)
    bmi=round(bmi, 1)
    name=username.get()
    resultLabel.destroy()
    message=""
    if bmi<18.5:
        message="You are underweight"
    elif bmi>18.25 and bmi<=24.9:
        message="You are in normal range"
    elif bmi>25 and bmi<=29.9:
        message="You are overweight"
    elif bmi>30:
        message="You are obese"
    else:
        message="Something went wrong"
    output=Label(resultFrame, text=name + " Your bmi is " + str(bmi) + " and " + message, bg="lightcyan", font=("Calibri", 12), width=42)
    output.place(x=20, y=40)
    output.pack()

appLabel=Label(window, text="BMI calculator", bg="lightcyan", fg="black", font=("Calibri", 20), bd=5)
appLabel.place(x=50, y=20)

nameLabel=Label(window, text="Your name", bg="lightcyan", fg="black", font=("Calibri", 12), bd=1)
nameLabel.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

heightLabel=Label(window, text="Enter height", bg="lightcyan", fg="black", font=("Calibri", 12), bd=1)
heightLabel.place(x=20, y=140)

height=Entry(window, text="", bd=2, width=15)
height.place(x=150, y=142)

weightLabel=Label(window, text="Enter weight", bg="lightcyan", fg="black", font=("Calibri", 12), bd=1)
weightLabel.place(x=20, y=185)

weight=Entry(window, text="", bd=2, width=15)
weight.place(x=150, y=187)

calculateButton=Button(window, text="calculate", bg="lightcyan", fg="black", font=("Calibri", 12), bd=4, command=calculate_bmi)
calculateButton.place(x=20, y=250)

resultFrame=LabelFrame(window, text="result", bg="lightcyan", font=("Calibri", 12))
resultFrame.pack(padx=20, pady=20)
resultFrame.place(x=20, y=300)

resultLabel=LabelFrame(window, text="", bg="lightcyan", font=("Calibri", 12), width=33)
resultLabel.place(x=20, y=20)
resultLabel.pack()

window.mainloop()