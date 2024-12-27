import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

def save_note():
    date = cal.get_date()
    note = note_entry.get()
    if date in notes:
        notes[date].append(note)
    else:
        notes[date] = [note]
    note_entry.delete(0, 'end')

def show_notes():
    date = cal.get_date()
    if date in notes:
        messagebox.showinfo('Заметки', '\n'.join(notes[date]))
    else:
        messagebox.showinfo('Заметки', 'Нет заметок для этой даты')

notes = {}

root = tk.Tk()
root.title("календарь")

cal = Calendar(root, selectmode='day', year=2023, month=12, day=22)
cal.pack(pady=20)

note_label = tk.Label(root, text="Введите заметку:")
note_label.pack()

note_entry = tk.Entry(root)
note_entry.pack()

save_button = tk.Button(root, text="Сохранить заметку", command=save_note)
save_button.pack(pady=5)

show_button = tk.Button(root, text="Показать заметки", command=show_notes)
show_button.pack(pady=5)

root.mainloop()