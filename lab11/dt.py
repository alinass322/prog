from tkinter import *
import calendar
import datetime
import tkinter.simpledialog as simpledialog
from tkinter import scrolledtext

def back():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()

def next():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()

def add_note_to_date(date):
    note = simpledialog.askstring(f"Note for {calendar.month_name[month]} {date}, {year}", f"Enter a note for {calendar.month_name[month]} {date}:")
    if note:
        if (year, month, date) in notes:
            notes[(year, month, date)].append(note)
        else:
            notes[(year, month, date)] = [note]
        first_day, month_days = calendar.monthrange(year, month)
        day_index = (first_day + date - 1) % 7 + 7 * ((first_day + date - 1) // 7)
        days[day_index].destroy()  
        day_label = Label(root, text=date, width=4, height=2, font='Arial 18 bold', fg='red')
        day_label.grid(row=2 + (date + first_day) // 7, column=(date + first_day - 1) % 7, sticky=NSEW)
        day_label.bind("<Button-1>", lambda event, day=date: add_note_to_date(day)) 

def fill():
    info_label['text'] = calendar.month_name[month] + ', ' + str(year)
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        back_month_days = calendar.monthrange(year - 1, 12)[1]
    else:
        back_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]

    for n in range(month_days):
        days[n + week_day]['text'] = n + 1
        days[n + week_day]['fg'] = 'black'
        if year == now.year and month == now.month and n == now.day:
            days[n + week_day - 1]['bg'] = 'green'
            days[n + week_day]['bg'] = 'grey'
        else:
            days[n + week_day]['bg'] = '#b3b3b3'

    for n in range(week_day):
        days[week_day - n - 1]['text'] = back_month_days - n
        days[week_day - n - 1]['fg'] = '#c4c4c4'
        days[week_day - n - 1]['bg'] = '#f3f3f3'
    for n in range(6 * 7 - month_days - week_day):
        days[week_day + month_days + n]['text'] = n + 1
        days[week_day + month_days + n]['fg'] = '#c4c4c4'
        days[week_day + month_days + n]['bg'] = '#f3f3f3'
    for n in range(month_days):
        if year == now.year and month == now.month and n + 1 == now.day:
            day_number = n + 1
            day_label = Label(root, text=day_number, width=4, height=2, font='Arial 18 bold', bg='blue', fg='white')
            day_label.grid(row=2 + (n + week_day) // 7, column=(n + week_day) % 7, sticky=NSEW)
            day_label.bind("<Button-1>", lambda event, day=day_number: add_note_to_date(day))
        else:
            day_number = n + 1
            day_label = Label(root, text=day_number, width=4, height=2, font='Arial 18 bold')
            day_label.grid(row=2 + (n + week_day) // 7, column=(n + week_day) % 7, sticky=NSEW)
            day_label.bind("<Button-1>", lambda event, day=day_number: add_note_to_date(day))

        days.append(day_label)


root = Tk()
root.title('календарь')
days = []
now = datetime.datetime.now()
year = now.year
month = now.month
back_button = Button(root, text='<', command=back)
back_button.grid(row=0, column=0, sticky=NSEW)
next_button = Button(root, text='>', command=next)
next_button.grid(row=0, column=6, sticky=NSEW)
info_label = Label(root, text='0', width=1, height=1, font='Arial 18 bold', fg='purple')
info_label.grid(row=0, column=1, columnspan=5, sticky=NSEW)

for n in range(7):
    lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1, font='Arial 10 bold', fg='purple')
    lbl.grid(row=1, column=n, sticky=NSEW)

for row in range(6):
    for col in range(7):
        lbl = Label(root, text='0', width=4, height=2, font='Arial 18 bold')
        lbl.grid(row=row+2, column=col, sticky=NSEW)
        days.append(lbl)

        
notes = {}

fill ()
root.mainloop()