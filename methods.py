

class Methods:
    def __init__(self, time, time_widget, text_widget):
        self.total_sec = time
        self.time_widget = time_widget
        self.text_widget = text_widget
        self.countdown()

    def countdown(self):
        """ refresh the content of the Timer Entry Widget every second """
        self.total_sec -= 1    # decrease the time
        mins, secs = divmod(self.total_sec, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # display the new time
        self.time_widget.set(timer)
        # request tkinter to call self.refresh after 1s
        if self.total_sec >= 0:
            self.text_widget.after(1000, self.countdown)
        else:
            self.time_widget.set("00:10")
            self.text_widget.delete("1.0", "end")
