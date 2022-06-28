from tkinter import Tk, Frame, Label, Entry, DISABLED, Text, StringVar, OptionMenu, Scrollbar, RIGHT, BOTH, END
from tkinter.colorchooser import askcolor
from tkmacosx import Button
from PIL import Image, ImageTk


class App(Tk):
    def __init__(self):
        super().__init__()
        self.width, self.height = 900, 400
        self.create_gui()
        # Countdown Settings
        self.max_time = 10
        self.countdown()

    def create_gui(self):
        # --- GUI --- #
        self.geometry('{}x{}'.format(self.width, self.height))
        # self.resizable(False, False)
        self.title('Vash, the Text!')

        # Background Image
        bg_img = ImageTk.PhotoImage(Image.open("./aldebaran.png").resize((self.width, self.height),
                                                                         Image.Resampling.LANCZOS))
        lbl = Label(self, image=bg_img)
        lbl.img = bg_img  # Keep a reference in case this code put is in a function.
        lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.

        # -- Frame Information -- #
        # frame_info
        frame_info = Frame(self, highlightthickness=0)
        frame_info.pack()
        # frame_write_section
        frame_write_sect = Frame(self, width=870, height=350, highlightthickness=0)
        frame_write_sect.pack_propagate(False)

        # frame Write Words -> Text Widget
        self.text_write_section = Text(frame_write_sect, width=1, height=1, bg="white", fg="black",
                                       highlightthickness=0, insertbackground="black")
        self.text_write_section.pack(fill="both", expand=True, padx=0, pady=0)
        self.text_write_section.focus()
        self.text_write_section.configure(font=('Arial', 22, 'normal'))
        self.text_write_section.bind("<KeyRelease>", lambda event: self.update_sec())
        frame_write_sect.pack()

        sb = Scrollbar(self.text_write_section)
        self.text_write_section.config(yscrollcommand=sb.set)
        sb.configure(command=self.text_write_section.yview)
        sb.pack(side=RIGHT, fill=BOTH)

        #  frame_info -> Time Left
        label_time = Label(frame_info, text="Time left:")
        label_time.grid(row=0, column=4, pady=3)

        self.time_text = StringVar()
        self.time_text.set("00:10")
        self.entry_time = Entry(frame_info, width=5, bg="white", fg="red", textvariable=self.time_text)
        self.entry_time.grid(row=0, column=5)
        self.entry_time["state"] = DISABLED

        # frame_info -> Background Color & Text Color
        self.btn_bg_color = Button(frame_info, text='Background Color', command=self.change_bg_color)
        self.btn_bg_color.grid(row=0, column=6, pady=3)

        self.btn_text_color = Button(frame_info, text='Text Color', command=self.change_text_color)
        self.btn_text_color.grid(row=0, column=7, pady=3)

        # frame_info -> Text Size
        label_size = Label(frame_info, text="Size:")
        label_size.grid(row=0, column=8, pady=3)

        size_range_int = range(1, 101)
        size_range_str = [str(x) for x in size_range_int]
        self.option_var = StringVar()
        self.option_var.set(size_range_str[21])

        option_menu = OptionMenu(frame_info, self.option_var, *size_range_str, command=self.change_text_size)
        option_menu.grid(row=0, column=9, pady=3)

    def change_bg_color(self):
        colors = askcolor(title="Tkinter Color Chooser")
        self.text_write_section.configure(bg=colors[1])
        self.btn_bg_color["bg"] = colors[1]

    def change_text_color(self):
        colors = askcolor(title="Tkinter Color Chooser")
        self.text_write_section.configure(fg=colors[1])
        self.btn_text_color["fg"] = colors[1]

    def change_text_size(self, option):
        self.text_write_section.configure(font=('Arial', int(self.option_var.get()), 'normal'))

    def update_sec(self):
        self.max_time = 10
        self.time_text.set(f"00:{self.max_time}")

    def countdown(self):
        self.max_time -= 1
        mins, secs = divmod(self.max_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # display the new time
        self.time_text.set(f"{timer}")
        # request tkinter to call self.refresh after 1s
        if self.max_time >= 0:
            self.entry_time.after(1000, self.countdown)
        else:
            self.text_write_section.delete("1.0", "end")
            self.max_time = 10
            self.time_text.set(f"00:{self.max_time}")
            self.countdown()

        if len(self.text_write_section.get("1.0", END)) == 1:
            self.max_time = 10




