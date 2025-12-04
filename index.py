from tkinter import *
import webbrowser

root = Tk()
root.title("Multi Media Task by Omar Fayed")
root.geometry("600x500")
root.configure(bg="#0f172a")

title_label = Label(
    root,
    text="Browser Link Opener",
    fg="cyan",
    bg="#0f172a",
    font=("Helvetica", 22, "bold")
)
title_label.pack(pady=20)



link_label = Label(
    root,
    text="Enter any link:",
    bg="#0f172a",
    fg="white",
    font=("Helvetica", 12)
)
link_label.pack(pady=5)

link_entry = Entry(root, width=40, font=("Helvetica", 12))
link_entry.pack(pady=5)

def open_custom_link():
    link = link_entry.get()
    if link.strip():
        webbrowser.open(link)

open_link_btn = Button(
    root,
    text="Open Entered Link",
    fg="black",
    bg="lightgray",
    font=("Helvetica", 13),
    padx=20,
    pady=5,
    command=open_custom_link
)
open_link_btn.pack(pady=10)
root.mainloop()
