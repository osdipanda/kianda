import tkinter as tk
from . import config


class LineNumbers(tk.Canvas):
    def __init__(self, master, text_widget, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.text_widget = text_widget
        self.redraw()
    
    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.text_widget.index("@0,0")
        while True :
            dline= self.text_widget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum, fill=config.color['linenumberfg'])
            i = self.text_widget.index("%s+1line" % i)

        # Refreshes the canvas widget 30fps
        self.after(30, self.redraw)
        self.line_number = linenum

    def force_update(self):
        self.redraw()