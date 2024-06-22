from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import font, colorchooser, filedialog, messagebox
import os
from spellchecker import SpellChecker
import string

spell = SpellChecker()

def newFile(event=None):
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile(event=None):
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None

    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close


def saveFile(event=None):
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[
                                 ("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def saveasFile(event=None):
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[
                                 ("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp(event=NONE):
    # root.destroy()
    global text_change, file
    try:
        if text_change:
            mbox = messagebox.askyesnocancel(
                "Warning", "Do You want to save this File ")
            if mbox is True:
                if file:
                    content = TextArea.get(1.0, END)
                    with open(file, "w", encoding="utf-8") as for_read:
                        for_read.write(content)
                        root.destroy()
                else:
                    content2 = TextArea.get(1.0, END)
                    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[
                                                    ("All Files", "*.*"), ("Text Documents", "*.txt")])
                    file.write(content2)
                    file.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return


def cut():
    TextArea.event_generate("<<Cut>>")


def copy():
    TextArea.event_generate("<<Copy>>")


def Paste():
    TextArea.event_generate("<<Paste>>")


def find(event=None):

    def find_fun():
        word = find_input.get()
        TextArea.tag_remove("match", "1.0", END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = TextArea.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                TextArea.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                TextArea.tag_config(
                    'match', foreground="red", background='#FFFF66')

    def replace_fun():
        word = find_input.get()
        replace_text = replace_input.get()
        content = TextArea.get(1.0, END)
        new_content = content.replace(word, replace_text)
        TextArea.delete(1.0, END)
        TextArea.insert(1.0, new_content)

    find_popup = Toplevel()
    find_popup.geometry("350x200")
    find_popup.title("Find Word")
    find_popup.wm_iconbitmap("icons/find.ico")
    find_popup.resizable(0, 0)

    find_frame = ttk.LabelFrame(find_popup, text="Find and Replace Word")
    find_frame.pack(pady=35)

    text_find = ttk.Label(find_frame, text="Find")
    text_replace = ttk.Label(find_frame, text="Replace")

    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    find_button = ttk.Button(find_frame, text="Find", command=find_fun)
    replace_button = ttk.Button(
        find_frame, text="Replace", command=replace_fun)

    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)

    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)


def clear(event=None):
    TextArea.delete(1.0, END)


def change_word(event=None):
    global text_change
    if TextArea.edit_modified():
        text_change = True
        word = len(TextArea.get(1.0, "end-1c").split())
        character = len(TextArea.get(1.0, "end-1c").replace(" ", ""))
        status_bars.config(text=f"Character : {character}  Word : {word}")
    TextArea.edit_modified(FALSE)


def toolbar():
    global show_tool_bar
    if show_tool_bar is False:

        TextArea.pack_forget()
        status_bars.pack_forget()
        tool_bars_label.pack(side=TOP, fill=X)
        TextArea.pack(fill=BOTH, expand=True)
        status_bars.pack(side=BOTTOM)
        show_tool_bar = True

    else:

        tool_bars_label.pack_forget()
        show_tool_bar = False


def statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False

    else:
        status_bars.pack(side=BOTTOM)
        show_status_bar = True


def change_font(root):
    global font_default
    font_default = font_family.get()
    TextArea.configure(font=(font_default, font_size_default))


def change_font_size(root):
    global font_size_default
    font_size_default = size_var.get()
    TextArea.configure(font=(font_default, font_size_default))


def bold_fun():
    text_get = font.Font(font=TextArea["font"])
    if text_get.actual()["weight"] == 'normal':
        TextArea.configure(font=(font_default, font_size_default, "bold"))
    if text_get.actual()["weight"] == 'bold':
        TextArea.configure(font=(font_default, font_size_default, "normal"))


def italic_fun():
    text_get = font.Font(font=TextArea["font"])
    if text_get.actual()["slant"] == 'roman':
        TextArea.configure(font=(font_default, font_size_default, "italic"))
    if text_get.actual()["slant"] == 'italic':
        TextArea.configure(font=(font_default, font_size_default, "roman"))


def underline_fun():
    text_get = font.Font(font=TextArea["font"])
    if text_get.actual()["underline"] == 0:
        TextArea.configure(font=(font_default, font_size_default, "underline"))
    if text_get.actual()["underline"] == 1:
        TextArea.configure(font=(font_default, font_size_default, "normal"))


def color_choose():
    color_var = colorchooser.askcolor()
    TextArea.configure(fg=color_var[1])


def left_align_fun():
    text_get_all = TextArea.get(1.0, "end")
    TextArea.tag_config("left", justify=LEFT)
    TextArea.delete(1.0, END)
    TextArea.insert(INSERT, text_get_all, "left")


def center_align_fun():
    text_get_all = TextArea.get(1.0, "end")
    TextArea.tag_config("center", justify=CENTER)
    TextArea.delete(1.0, END)
    TextArea.insert(INSERT, text_get_all, "center")


def right_align_fun():
    text_get_all = TextArea.get(1.0, "end")
    TextArea.tag_config("right", justify=RIGHT)
    TextArea.delete(1.0, END)
    TextArea.insert(INSERT, text_get_all, "right")


# Function to detect if Windows is in dark mode
def is_windows_dark_mode():
    try:
        # Access registry to check if dark mode is enabled
        import winreg
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        reg_key = winreg.OpenKey(
            registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        dark_mode, _ = winreg.QueryValueEx(reg_key, "AppsUseLightTheme")
        winreg.CloseKey(reg_key)
        return dark_mode == 0  # 0 means dark mode, 1 means light mode
    except:
        return False


# Function to set the light theme
def light():
    apply_theme("Light")


# Function to set the dark theme
def dark():
    apply_theme("Dark")


# Function to set the system theme dynamically
def system():
    if is_windows_dark_mode():
        apply_theme("SystemDark")
    else:
        apply_theme("SystemLight")


# Helper function to apply the theme to all relevant widgets
def apply_theme(theme_name):
    color_tuple = color_dict.get(theme_name)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    TextArea.config(background=bg_color, fg=fg_color)


def delete_word(event):
    text_index = TextArea.index(INSERT)
    if text_index:
        TextArea.delete("insert-2c wordstart", "insert")
    return "break"

def undo(event=None):
    TextArea.edit_undo()

def redo(event=None):
    TextArea.edit_redo()


def spell_check(event=None):
    text_content = TextArea.get(1.0, END)
    words = text_content.split()
    misspelled = []

    # Remove punctuation from each word and check spelling
    for word in words:
        clean_word = word.strip(string.punctuation)
        if clean_word and clean_word not in spell:
            misspelled.append(word)

    # Remove previous misspelled tags
    for tag in TextArea.tag_names():
        if tag.startswith("misspelled"):
            TextArea.tag_delete(tag)

    # Add new misspelled tags
    for word in misspelled:
        start_idx = '1.0'
        while True:
            start_idx = TextArea.search(word, start_idx, nocase=True, stopindex=END)
            if not start_idx:
                break
            end_idx = f"{start_idx}+{len(word)}c"
            TextArea.tag_add(f"misspelled-{word}", start_idx, end_idx)
            start_idx = end_idx

    # Apply styling to misspelled tags
    for tag in TextArea.tag_names():
        if tag.startswith("misspelled"):
            TextArea.tag_configure(tag, foreground="red", underline=1)
            TextArea.tag_bind(tag, "<Button-3>", show_suggestions)

# Function to show spelling suggestions in a context menu
def show_suggestions(event):
    menu = Menu(root, tearoff=0)
    word_start = TextArea.index(f"@{event.x},{event.y} wordstart")
    word_end = TextArea.index(f"@{event.x},{event.y} wordend")
    word = TextArea.get(word_start, word_end)
    clean_word = word.strip(string.punctuation)
    suggestions = spell.candidates(clean_word)

    if not suggestions:
        menu.add_command(label="No Suggestions", state="disabled")
    else:
        for suggestion in suggestions:
            menu.add_command(label=suggestion, command=lambda suggestion=suggestion: replace_word(word_start, word_end, suggestion))

    menu.post(event.x_root, event.y_root)


# Function to replace the misspelled word with the selected suggestion
def replace_word(start, end, suggestion):
    TextArea.delete(start, end)
    TextArea.insert(start, suggestion)
    spell_check()



# Driver Code
if __name__ == "__main__":
    root = Tk()
    root.title("Untitled Notepad")
    root.wm_iconbitmap("icons/2.ico")
    root.geometry("800x600")

    # MenuBar
    MenuBar = Menu(root, cursor="arrow")

    FileMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    # icon
    new_icon = PhotoImage(file="icons/file.png")
    open_icon = PhotoImage(file="icons/open.png")
    save_icon = PhotoImage(file="icons/save.png")
    save_as_icon = PhotoImage(file="icons/save_as.png")
    exit_icon = PhotoImage(file="icons/exit.png")
    cut_icon = PhotoImage(file="icons/cut.png")
    copy_icon = PhotoImage(file="icons/copy.png")
    paste_icon = PhotoImage(file="icons/paste.png")
    find_icon = PhotoImage(file="icons/find.png")
    clear_icon = PhotoImage(file="icons/clear.png")
    tool_icon = PhotoImage(file="icons/tool.png")
    status_icon = PhotoImage(file="icons/status.png")
    dark_icon = PhotoImage(file="icons/dark.png")
    light_icon = PhotoImage(file="icons/light.png")
    system_icon = PhotoImage(file="icons/system.png")
    bold_icon = PhotoImage(file="icons/bold.png")
    italic_icon = PhotoImage(file="icons/italic.png")
    underline_icon = PhotoImage(file="icons/underline.png")
    align_center_icon = PhotoImage(file="icons/align_center.png")
    align_left_icon = PhotoImage(file="icons/align_left.png")
    align_right_icon = PhotoImage(file="icons/align_right.png")
    color_wheel_icon = PhotoImage(file="icons/color_wheel.png")

    color_dict = {
        'Light': ("#000000", "#ffffff"),   # (font_color, bg_color)
        'Dark': ("#FFFFFF", "#202020"),
        "SystemLight": ("#000000", "#ffffff"),
        "SystemDark": ("#FFFFFF", "#202020")
    }

    # Font family
    font_default = "Arial"
    font_size_default = 16

    # Open New File
    FileMenu.add_command(label="New", image=new_icon,
                         compound=LEFT, accelerator="Ctrl + N", command=newFile)
    # Open Exiting File
    FileMenu.add_command(label="Open", image=open_icon,
                         compound=LEFT, accelerator="Ctrl + O", command=openFile)
    FileMenu.add_separator()
    # Save File
    FileMenu.add_command(label="Save", image=save_icon,
                         compound=LEFT, accelerator="Ctrl + S", command=saveFile)
    # Save as File
    FileMenu.add_command(label="Save As..", image=save_as_icon,
                         compound=LEFT, accelerator="Ctrl + Shift + S", command=saveasFile)
    FileMenu.add_separator()
    # Exit Application
    FileMenu.add_command(label="Exit", image=exit_icon,
                         compound=LEFT, command=quitApp, accelerator="Ctrl + Q")

    EditMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    EditMenu.add_command(label="Cut", image=cut_icon,
                         compound=LEFT, accelerator="Ctrl + X", command=cut)
    EditMenu.add_separator()
    EditMenu.add_command(label="copy", image=copy_icon,
                         compound=LEFT, accelerator="Ctrl + C", command=copy)
    EditMenu.add_command(label="Paste", image=paste_icon,
                         compound=LEFT, accelerator="Ctrl + V", command=Paste)
    EditMenu.add_separator()
    EditMenu.add_command(label="Find", image=find_icon,
                         compound=LEFT, accelerator="Ctrl + F", command=find)
    EditMenu.add_command(label="Clear", image=clear_icon,
                         compound=LEFT, accelerator=" Alt + X", command=clear)

    root.bind_all("<Control-n>", newFile)
    root.bind_all("<Control-o>", openFile)
    root.bind_all("<Control-f>", find)
    root.bind_all("<Control-s>", saveFile)
    root.bind_all("<Control-Shift-KeyPress-S>", saveasFile)
    root.bind_all("<Control-q>", quitApp)
    root.bind_all("<Alt-x>", clear)
    root.bind_all("<Control-z>", undo)
    root.bind_all("<Control-y>", redo)

    # Tool Bar Label
    tool_bars_label = Label(root)
    tool_bars_label.pack(side=TOP, fill=X)

    # Font box
    get_fonts = font.families()
    font_family = StringVar()
    font_box = ttk.Combobox(tool_bars_label, width=30,
                            textvariable=font_family, state="readonly", justify=CENTER)
    font_box["values"] = get_fonts
    font_box.current(get_fonts.index("Arial"))
    font_box.grid(row=0, column=0, padx=5, pady=1)
    font_box.bind("<<ComboboxSelected>>", change_font)

    # Size Box
    size_var = IntVar()
    size_box = ttk.Combobox(tool_bars_label, width=20,
                            textvariable=size_var, state="readonly", justify=CENTER)
    size_box["values"] = tuple(range(8, 72, 2))
    size_box.current(4)
    size_box.grid(row=0, column=1, padx=5, pady=1)
    size_box.bind("<<ComboboxSelected>>", change_font_size)

    # Bold
    bold_btn = ttk.Button(tool_bars_label, image=bold_icon, command=bold_fun)
    bold_btn.grid(row=0, column=2, padx=2)

    # Italic
    italic_btn = ttk.Button(tool_bars_label, image=italic_icon)
    italic_btn.grid(row=0, column=3, padx=2)
    italic_btn.configure(command=italic_fun)

    # underline
    underline_btn = ttk.Button(tool_bars_label, image=underline_icon)
    underline_btn.grid(row=0, column=4, padx=2)
    underline_btn.configure(command=underline_fun)

    # color_wheel
    color_wheel_btn = ttk.Button(tool_bars_label, image=color_wheel_icon)
    color_wheel_btn.grid(row=0, column=5, padx=8)
    color_wheel_btn.configure(command=color_choose)

    # right_align
    align_right_btn = ttk.Button(tool_bars_label, image=align_right_icon)
    align_right_btn.grid(row=0, column=8, padx=3)
    align_right_btn.configure(command=right_align_fun)

    # left_align
    align_left_btn = ttk.Button(tool_bars_label, image=align_left_icon)
    align_left_btn.grid(row=0, column=6, padx=3)
    align_left_btn.configure(command=left_align_fun)

    # center_align
    align_center_btn = ttk.Button(tool_bars_label, image=align_center_icon)
    align_center_btn.grid(row=0, column=7, padx=3)
    align_center_btn.configure(command=center_align_fun)

    show_status_bar = BooleanVar()
    show_status_bar.set(False)

    show_tool_bar = BooleanVar()
    show_tool_bar.set(True)

    viewMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="View", menu=viewMenu)

    viewMenu.add_checkbutton(label="Tool Bar Hide", onvalue=True,
                             offvalue=0, image=tool_icon, compound=LEFT, command=toolbar)
    viewMenu.add_checkbutton(
        label="Status Bar Hide", image=status_icon, compound=LEFT, command=statusbar)

    themeMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="Theme", menu=themeMenu)

    themeMenu.add_radiobutton(
        label="Light", image=light_icon, compound=LEFT, command=light)
    themeMenu.add_radiobutton(
        label="Dark", image=dark_icon, compound=LEFT, command=dark)
    themeMenu.add_radiobutton(
        label="System", image=system_icon, compound=LEFT, command=system)

    root.config(menu=MenuBar)

    # status Bar
    status_bars = ttk.Label(root, text=" Lines", cursor="arrow")
    status_bars.pack(side=BOTTOM, fill=X)
    text_change = False

    # Text Area
    TextArea = Text(root, font=("Arial", 16))
    file = None
    TextArea.config(wrap="word", relief=SUNKEN)

    Scroll = Scrollbar(root)
    TextArea.focus_set()
    Scroll.pack(side=RIGHT, fill=Y)
    TextArea.pack(fill=BOTH, expand=True)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    TextArea.bind("<<Modified>>", change_word)

    TextArea.bind("<Control-BackSpace>", delete_word)

    TextArea.bind('<KeyRelease>', spell_check)

root.mainloop()
