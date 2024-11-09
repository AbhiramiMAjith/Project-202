import socket
from threading import Thread
from tkinter import *

#nickname = input("Enter your nickname ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 8000
client.connect((ip,port))

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)

        self.ask = Label(self.login,text="Please Login to continue",justify='center',font=('Calibri'))
        self.ask.place(relheight = 0.15,relx = 0.2,rely = 0.07)

        self.name_label = Label(self.login,text="Name",font=("Calibri"))
        self.name_label.place(relheight = 0.2,relx = 0.1,rely = 0.2)

        self.name = Entry(self.login)
        self.name.place(relwidth = 0.4,relheight = 0.12, relx= 0.1,rely = 0.2)

        self.continue_button = Button(self.login,text="Continue",font=("Calibri"),command=lambda:self.go_ahead(self.name.get()))
        self.continue_button.place(relx=0.4,rely=0.55)

        self.window.mainloop()

    def go_ahead(self,name):
        self.login.destroy()
        self.name = name
        recieve_thread = Thread(target=self.recieve)
        recieve_thread.start()

    def recieve(self):
        while True:
            try:
                message = client.recv(2048).decode("utf-8")
                if message == 'NICKNAME':
                    client.send(self.name.encode("utf-8"))
                else:
                    pass
            except Exception as error:
                print("An error occured",error)
                client.close()
                break
gui = GUI()