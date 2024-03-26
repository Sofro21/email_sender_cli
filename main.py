import smtplib
from tkinter.simpledialog import askstring
from tkinter import *

def automatic_email_sender(email_address, message1):
    if type(email_address) is not str:
        raise Exception("Wrong Input")
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'andreisofroniesubscriptions@gmail.com'
    smtp_password = 'zoxmvjqjwodtsjhr'

    from_email = 'andreisofroniesubscriptions@gmail.com'
    to_email = email_address
    subject = 'My first automatic email!'
    body = message1

    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)


top = Tk()

top.geometry("1000x1000")
def show():
   message = askstring("Input", "Enter the message you want to send")
   automatic_email_sender('andreisofronie25@gmail.com', message)
   
B = Button(top, text ="Click", command = show)
B.place(x=500,y=500)

top.mainloop()