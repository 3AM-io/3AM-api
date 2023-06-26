import tkinter as tk
from tkinter import ttk
from appController import responseGen
from speechrecognition import takeCommand
from threading import Thread
import asyncio
import event_emitter as events

class App(tk.Frame):    
    def __init__(self, master=None):
        super().__init__(master)
        
        self.em = events.EventEmitter()
        self.em.on("render", self.render)
        self.row = 0
        self.status = False
        self.master.geometry("500x500")
        self.grid()
        
        # Menu pane title
        self.menu = ttk.Frame(self, height=100, width=500)
        self.menu.grid(row=0)
        ttk.Label(self.menu, text="Vaider.ai").grid(row=0, column=0)
        
        # Content pan
        self.contentPan = ttk.Frame(self, height=400, width=500)
        self.contentPan.grid(row=1)
        
        # Footer (mic)
        self.footer = ttk.Frame(self, height=500, width=500).grid(row=2)
        ttk.Button(self.footer, text="Listen", command=self.listen).grid(row=0, column=0)

    async def listenThread(self):
        try:
            self.query = takeCommand()
            self.response = responseGen(self.query)
            self.em.emit("render")
            print(self.response)
        except:
            self.query = ""
            self.response = "Sorry, I didn't get that"
            self.em.emit("render")
            print(self.response)

    def listen(self):
        # log the in and out
        # ttk.Label(self.contentPan, text="User: " + query).pack()
        # ttk.Label(self.contentPan, text="Vaider: " + response).pack()
        thread = Thread(target=asyncio.run, args=(self.listenThread(),))
        thread.start()
        
    def render(self):
        ttk.Label(self.contentPan, text="User: " + self.query).grid(row=self.row, column=0)
        ttk.Label(self.contentPan, text="Vaider: " + self.response).grid(row=self.row+1, column=0)
        self.row += 2

app = App()
app.mainloop()