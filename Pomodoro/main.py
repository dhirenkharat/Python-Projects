from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
tim=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(tim)
    lable1.config(text="Timer")
    lable2.config(text="")
    canvas.itemconfig(textop,text="00:00")
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec=WORK_MIN*60
    short_break_min=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)
        lable1.config(text="Break", bg=YELLOW)
    elif reps%2==1:
        count_down(work_sec)
        lable1.config(text="Work" ,bg=YELLOW)
    else:
        count_down(short_break_min)
        lable1.config(text="Short Break" ,bg=YELLOW)
        temp=""
        for i in range(math.floor(reps/2)):
            temp+="✔"
            lable2.config(text=temp)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec in range(0,10):
        count_sec="0"+str(count_sec)
    canvas.itemconfig(textop,text=f"{count_min}:{count_sec}")
    if count>0:
        global tim
        tim=window.after(1000,count_down,count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)

textop=canvas.create_text(100,130,text="00.00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

lable1=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
lable1.grid(column=1,row=0)

button=Button(text="Start",command=start_timer)
button.grid(column=0,row=2)

button2=Button(text="reset",command=reset_timer)
button2.grid(column=2,row=2)

lable2=Label(font=(FONT_NAME,20,"bold"),fg=GREEN)
lable2.grid(column=1,row=3)







window.mainloop()

