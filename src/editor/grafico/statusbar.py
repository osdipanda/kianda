import tkinter as tk
from . import config


class StatusBar(tk.Canvas):
    def __init__(self, master, bg, *args, **kwargs):
        super().__init__(master, highlightthickness=0, *args, **kwargs)
        self.master = master
        self.bg = bg
        self.label  = tk.Label(self,
        font=(config.font['statusbar']['family'], 
        config.font['statusbar']['size']),
        background=config.color['statusbarbg'],
        foreground=config.color['foreground'])
        self.label.pack(fill="x")

    def set(self, format, *args):
        self.label.config(text = format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()