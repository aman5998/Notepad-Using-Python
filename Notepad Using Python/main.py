import tkinter as tk
from tkinter import ttk, font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("Notepad")
main_application.iconbitmap('icons/notepad.ico')

# Main Menu
main_menu = tk.Menu()

# File menu
file = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file)

# Icons for File menu
new_icon = tk.PhotoImage(file="icons/new.png")
open_icon = tk.PhotoImage(file="icons/open.png")
save_icon = tk.PhotoImage(file="icons/save.png")
save_as_icon = tk.PhotoImage(file="icons/save_as.png")
exit_icon = tk.PhotoImage(file="icons/exit.png")

# New Button Function
text_url = ""

def new_file(event=None):
    global text_url
    text_url = ""
    text_editor.delete(1.0, tk.END)

file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N", command=new_file)

# Open File Button Function
def open_file(event=None):
    global text_url
    text_url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                          filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
    try:
        with open(text_url, "r") as for_read:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(text_url))

file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O", command=open_file)

# Save Button Function
def save_file(event=None):
    global text_url
    try:
        if text_url:
            content = str(text_editor.get(1.0, tk.END))
            with open(text_url, "w", encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
            if text_url:
                with open(text_url, "w", encoding="utf-8") as for_read:
                    content2 = text_editor.get(1.0, tk.END)
                    for_read.write(content2)
    except:
        return

file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S", command=save_file)

# Save as Button Function
def save_as_file(event=None):
    global text_url
    try:
        content = text_editor.get(1.0, tk.END)
        text_url = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
        if text_url:
            with open(text_url, "w", encoding="utf-8") as file:
                file.write(content)
    except:
        return

file.add_command(label="Save as", image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Shift+S", command=save_as_file)
file.add_separator()

# Exit Function
def exit_fun(event=None):
    global text_url, text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel("Warning", "Do you want to save this file?")
            if mbox is True:
                if text_url:
                    content = text_editor.get(1.0, tk.END)
                    with open(text_url, "w", encoding="utf-8") as for_read:
                        for_read.write(content)
                    main_application.destroy()
                else:
                    text_url = filedialog.asksaveasfilename(defaultextension=".txt",
                                                            filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
                    if text_url:
                        with open(text_url, "w", encoding="utf-8") as for_read:
                            content2 = text_editor.get(1.0, tk.END)
                            for_read.write(content2)
                        main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, command=exit_fun)

# Edit menu
edit = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Edit", menu=edit)

# Icons for Edit menu
copy_icon = tk.PhotoImage(file="icons/copy.png")
paste_icon = tk.PhotoImage(file="icons/paste.png")
cut_icon = tk.PhotoImage(file="icons/cut.png")
clear_all_icon = tk.PhotoImage(file="icons/clear_all.png")
find_icon = tk.PhotoImage(file="icons/find.png")

edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C",
                 command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V",
                 command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X",
                 command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear all", image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+X",
                 command=lambda: text_editor.delete(1.0, tk.END))
edit.add_separator()

# Find section for find button ui
def find_fun():
    find_popup = tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("Find")
    find_popup.iconbitmap('icons/find.ico')
    find_popup.resizable(0, 0)

    # frame for find
    find_frame = ttk.LabelFrame(find_popup, text="Find/Replace")
    find_frame.pack(pady=20)
    #label
    text_find = ttk.Label(find_frame, text="Find")
    text_replace = ttk.Label(find_frame, text="Replace")
    # entry box
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)
    # button
    find_button = ttk.Button(find_frame, text="Find")
    replace_button = ttk.Button(find_frame, text="Replace")
    # text label grid
    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)
    # Entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    # button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F", command=find_fun)

# View menu
view = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="View", menu=view)
view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=0)
view.add_checkbutton(label="Status Bar", onvalue=True, offvalue=0)

# Theme menu
theme = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Theme", menu=theme)
theme.add_radiobutton(label="Light")
theme.add_radiobutton(label="Dark")
theme.add_radiobutton(label="System")

main_application.config(menu=main_menu)

# Tool Bar
tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP, fill=tk.X)

# Font Box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label, width=30, textvariable=font_family, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5, pady=5)

# Size Box
size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label, width=20, textvariable=size_variable, state="readonly")
font_size["values"] = tuple(range(4, 50, 2))
font_size.current(6)
font_size.grid(row=0, column=1, padx=5)

# Bold button
bold_icon = tk.PhotoImage(file="icons/bold.png")
bold_btn = ttk.Button(tool_bar_label, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# Italic button
italic_icon = tk.PhotoImage(file="icons/italic.png")
italic_btn = ttk.Button(tool_bar_label, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# Underline button
underline_icon = tk.PhotoImage(file="icons/underline.png")
underline_btn = ttk.Button(tool_bar_label, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# Color Wheel button
font_color_btn_icon = tk.PhotoImage(file="icons/color_wheel.png")
font_color_btn = ttk.Button(tool_bar_label, image=font_color_btn_icon)
font_color_btn.grid(row=0, column=5, padx=5)

# Left Align button
left_align_icon = tk.PhotoImage(file="icons/left_align.png")
left_align_btn = ttk.Button(tool_bar_label, image=left_align_icon)
left_align_btn.grid(row=0, column=6, padx=5)

# Center Align button
center_align_icon = tk.PhotoImage(file="icons/center_align.png")
center_align_btn = ttk.Button(tool_bar_label, image=center_align_icon)
center_align_btn.grid(row=0, column=7, padx=5)

# Right Align button
right_align_icon = tk.PhotoImage(file="icons/right_align.png")
right_align_btn = ttk.Button(tool_bar_label, image=right_align_icon)
right_align_btn.grid(row=0, column=8, padx=5)

# Text Edit Area
text_editor = tk.Text(main_application)
text_editor.config(wrap="word", relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Status Bar word and character count
status_bars = ttk.Label(main_application, text="Status bar")
status_bars.pack(side=tk.BOTTOM)

text_change = False

def change_word(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        word = len(text_editor.get(1.0, "end-1c").split())
        character = len(text_editor.get(1.0, "end-1c"))
        status_bars.config(text=f"Character: {character} Word: {word}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", change_word)

# Font family and font size function
font_now = "Arial"
font_size_now = 16

def change_font(event=None):
    global font_now
    font_now = font_family.get()
    text_editor.configure(font=(font_now, font_size_now))

def change_size(event=None):
    global font_size_now
    font_size_now = size_variable.get()
    text_editor.configure(font=(font_now, font_size_now))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)

# Bold Function
def bold_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"] == 'normal':
        text_editor.configure(font=(font_now, font_size_now, "bold"))
    if text_get.actual()["weight"] == 'bold':
        text_editor.configure(font=(font_now, font_size_now, "normal"))

bold_btn.configure(command=bold_fun)

# Italic Function
def italic_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"] == 'roman':
        text_editor.configure(font=(font_now, font_size_now, "italic"))
    if text_get.actual()["slant"] == 'italic':
        text_editor.configure(font=(font_now, font_size_now, "roman"))

italic_btn.configure(command=italic_fun)

# Underline Function
def underline_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"] == 0:
        text_editor.configure(font=(font_now, font_size_now, "underline"))
    if text_get.actual()["underline"] == 1:
        text_editor.configure(font=(font_now, font_size_now, "normal"))

underline_btn.configure(command=underline_fun)

# Color button function
def color_choose():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=color_choose)

# Left align button function
def align_left():
    text_get_all = text_editor.get(1.0, "end")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "left")

left_align_btn.configure(command=align_left)

# Center align button function
def align_center():
    text_get_all = text_editor.get(1.0, "end")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "center")

center_align_btn.configure(command=align_center)

# Right align button function
def align_right():
    text_get_all = text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "right")

right_align_btn.configure(command=align_right)

def delete_word(event):
    text_index = text_editor.index(tk.INSERT)
    if text_index:
        text_editor.delete("insert-2c wordstart", "insert")
    return "break"

text_editor.bind("<Control-BackSpace>", delete_word)

main_application.mainloop()
