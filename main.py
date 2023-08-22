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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text= "00.00")
    lable.config(text= "Timer", fg=GREEN)
    check_marks.config(text= "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #if 8th reps
    if reps == 8:
        count_down(long_break_sec)
        lable.config(text="Long Break", fg=GREEN)
        window.lift()
    #if 2nd/4th/6th rep
    elif reps % 2 == 0:
        count_down(short_break_sec)
        lable.config(text= "Short Break", fg=PINK)
        window.lift()
    else:
        # if 1st/3rd/5th/7th rep
        count_down(work_sec)
        lable.config(text="Work", fg=RED)
        window.lift()



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
         count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,count_down, count -1)
    else:
        start_timer()
        mark = ""
        # for every 2 reps completed you complete a wrok session - add a check mark
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        check_marks.config(text= mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Study Session")
window.config(padx=100, pady=50, bg= YELLOW)

canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


lable = Label(text="Timer", fg= GREEN, font=(FONT_NAME, 45, "bold"), bg= YELLOW)
lable.grid(column=2, row=1)

start_button = Button(text= "start",command= start_timer , highlightthickness=0)
start_button.grid(column=1, row=3)

reset_button = Button(text= "reset",command=reset_timer, highlightthickness=0)
reset_button.grid(column=3, row=3)

check_marks = Label(fg= GREEN, bg= YELLOW)
check_marks.grid(column=2, row=3)





window.mainloop()
