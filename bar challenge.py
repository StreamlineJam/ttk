import ttkbootstrap as tb
from helpers.K import *

class SearchBarComp(tb.Frame):
    def __init__(self, master, y_spacing=PM):
        super().__init__(master)
        self.pack(pady=y_spacing, padx=PL, fill=X)

        self.entry = tb.Entry(self)
        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS, command=self.submit_action)

        self.entry.pack(side=LEFT, expand=TRUE, fill=X)
        self.submit_button.pack(side=LEFT, padx=(PM, 0))



class ButtonGroupComp(tb.Frame):
    def __init__(self, master, y_spacing=PL):
        super().__init__(master)
        self.pack(pady=y_spacing, padx=PL, fill=X)

        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
        self.clear_button = tb.Button(self, text="Clear", bootstyle=WARNING)

        self.submit_button.pack(side=RIGHT, padx=(PS, 0))
        self.clear_button.pack(side=RIGHT)


class App(tb.Window):
    def __init__(self, theme):
        super().__init__(themename=theme)

        self.title("Frames")
        self.geometry("1280x720")

        self.results_text = tb.StringVar(value="No Results")

        self.title_label = tb.Label(self, text="SMIC Records", font=DISPLAY3, bootstyle=PRIMARY)
        self.subtitle_label = tb.Label(
            self,
            text="get smic students records",
            font=H5,
            bootstyle=SECONDARY)
        self.results = tb.Label(self, textvariable=self.results_text, font=BODY, bootstyle=INFO)

        self.title_label.pack(pady=(PL, 0), padx=PL, fill=X)
        self.subtitle_label.pack(pady=(0, PM), padx=PL, fill=X)
        self.search_bar = SearchBarComp(self)
        self.results.pack(pady=PM, padx=PL, expand=TRUE)
        # self.button_group = ButtonGroupComp(self)


if __name__ == '__main__':
    app = App(theme="sandstone")
    app.place_window_center()
    app.mainloop()