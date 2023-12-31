import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
my_timer = None
timer_running = False


# ---------------------------- TIMER RESET ------------------------------- #

def reset_it():
    global my_timer
    global reps
    global timer_running
    window.after_cancel(my_timer)
    header.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    checks.config(text="")
    reps = 0
    timer_running = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global timer_running
    if timer_running:
        return

    global reps
    reps += 1
    timer_running = True

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        header["text"] = "Long Break!"
        header["fg"] = RED
        reps = 0
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        header["text"] = "Short Break"
        header["fg"] = PINK
    else:
        count_down(WORK_MIN * 60)
        header["text"] = "Working"
        header["fg"] = GREEN


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global my_timer
    global timer_running
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min == 0:
        count_min = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1000, count_down, count - 1)
    else:
        timer_running = False
        start_timer()
        marks = ""
        sessions = math.floor(reps / 2)
        for _ in range(sessions):
            marks += "✅"
        checks["text"] = marks


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Labels

header = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
header.grid(row=0, column=1)

checks = Label(fg=GREEN, bg=YELLOW, font=50)
checks.grid(row=4, column=1)

# buttons
button = Button(text="Start", command=start_timer)
button.grid(row=2, column=0)

button2 = Button(text="Reset", command=reset_it)
button2.grid(row=2, column=3)

window.mainloop()
