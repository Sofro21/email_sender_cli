import smtplib
from tkinter.simpledialog import askstring
from tkinter import *

def automatic_email_sender(email_address, message1, user_input):
    email = email_address.get()
    ui = user_input.get()
    message2 = message1.get("1.0", "end-1c")
    message2 = message2.replace("{DEMIR}", user_input.get())


    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'andreisofroniesubscriptions@gmail.com'
    smtp_password = 'zoxmvjqjwodtsjhr'

    from_email = 'andreisofroniesubscriptions@gmail.com'
    to_email = email
    subject = 'My first automatic email!'
    body = message2

    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)


top = Tk()
top.geometry("1000x1000")

email_label = Label(top, text="E-mail Address:")
email_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

email_entry = Entry(top, width=40)
email_entry.grid(row=0, column=1, padx=5, pady=5)

random_user_input_label = Label(top, text="Random user input:")
random_user_input_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

random_user_input = Entry(top, width=40)
random_user_input.grid(row=2, column=1, padx=5, pady=5)

message_label = Label(top, text="Message:")
message_label.grid(row=1, column=0, padx=5, pady=5, sticky="nw")

message_text = Text(top, width=40, height=10)
message_text.grid(row=1, column=1, padx=5, pady=5, sticky="nw")

send_button = Button(top, text="Send Email", command=lambda: automatic_email_sender(email_entry,message_text,random_user_input))
send_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")


top.mainloop()