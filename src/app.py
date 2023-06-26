import tkinter as tk
from tkinter import ttk
from appController import responseGen
from speechrecognition import takeCommand
from threading import Thread

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("500x500")
        self.pack()
        
        # Menu pane title
        self.menu = ttk.Frame(self, height=100, width=500)
        self.menu.pack()
        ttk.Label(self.menu, text="Vaider.ai").pack()
        
        # Content pan
        self.contentPan = ttk.Frame(self, height=300, width=500)
        self.contentPan.pack()
        ttk.Label(self.contentPan, text="Content")
        
        # Footer (mic)
        self.footer = ttk.Frame(self, height=100, width=500).pack()
        ttk.Button(self.footer, text="Listen", command=self.listen).pack()
    
    def listenThread(self):
        query = takeCommand()
        ttk.Label(self.contentPan, text="User: " + query).pack()
        response = responseGen(query)
        ttk.Label(self.contentPan, text="Vaider: " + response).pack()
    
    def listen(self):
        # log the in and out
        thread = Thread(target=self.listenThread)
        thread.start()
        thread.join()

app = App()
app.mainloop()