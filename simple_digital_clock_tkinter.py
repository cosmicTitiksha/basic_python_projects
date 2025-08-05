import tkinter as tk
import time

root = tk.Tk()
root.title('Simple Digital Clock')
root.geometry('400x200')
root.configure(bg="black")

time_label = tk.Label(root,
                      font = ('Algerian',49),
                      background= 'black',
                      foreground= 'cyan')
time_label.pack(anchor='center')

def update_time():
    current_time = time.strftime('%H:%M:%S')  # e.g. 14:23:45
    time_label.config(text=current_time)  # update label
    root.after(1000, update_time)  # recall this function every 1000ms (1 sec)


update_time()
root.mainloop()