import tkinter as tk
import subprocess
import queue
import os
from threading import Thread

class Terminal:
    def __init__(self, master, text_widget):
        self.master = master
        self.text_widget = text_widget

        # get the path to the console.py file assuming it is in the same folder
        consolePath = os.path.join(os.path.dirname(__file__),"interactiveConsole.py")
        # open the interactiveConsole.py file (replace the path to python with the 
        # correct one for your system)
        self.proc = subprocess.Popen(["python3",consolePath],
                                      stdout=subprocess.PIPE,
                                       stdin=subprocess.PIPE,
                                      stderr=subprocess.PIPE)

        # make queues for keeping stdout and stderr whilst it is transferred between threads
        self.outQueue = queue.Queue()
        self.errQueue = queue.Queue()

        # keep track of where any line that is submitted starts
        self.line_start = 0

        # a daemon to keep track of the threads so they can stop running
        self.alive = True

        # start the functions that get stdout and stderr in separate threads
        Thread(target=self.readFromProccessOut).start()
        Thread(target=self.readFromProccessErr).start()

    def destroy(self):
        "This is the function that is automatically called when the widget is destroyed."
        # write exit() to the console in order to stop it running
        self.proc.stdin.write("exit()\n".encode())
        self.proc.stdin.flush()
        self.master.destroy()

    def enter(self,event=None):
        "The <Return> key press handler"
        string = self.text_widget.get(1.0, tk.END)[self.line_start:]
        self.line_start+=len(string)
        self.proc.stdin.write(string.encode())
        self.proc.stdin.flush()

    def readFromProccessOut(self):
        "To be executed in a separate thread to make read non-blocking"
        while self.alive:
            data = self.proc.stdout.raw.read(1024).decode()
            self.outQueue.put(data)

    def readFromProccessErr(self):
        "To be executed in a separate thread to make read non-blocking"
        while self.alive:
            data = self.proc.stderr.raw.read(1024).decode()
            self.errQueue.put(data)

    def writeLoop(self):
        "Used to write data from stdout and stderr to the Text widget"
        # if there is anything to write from stdout or stderr, then write it
        if not self.errQueue.empty():
            self.write(self.errQueue.get())
        if not self.outQueue.empty():
            self.write(self.outQueue.get())

        # run this method again after 10ms
        if self.alive:
            self.text_widget.after(10,self.writeLoop)

    def write(self,string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)
        self.line_start+=len(string)
