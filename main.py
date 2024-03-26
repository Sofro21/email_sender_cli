import smtplib

def automatic_email_sender(email_address):
    if type(email_address) is not str:
        raise Exception("Wrong Input")
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'andreisofroniesubscriptions@gmail.com'
    smtp_password = 'zoxmvjqjwodtsjhr'

    from_email = 'andreisofroniesubscriptions@gmail.com'
    to_email = email_address
    subject = 'My first automatic email!'
    body = 'This is a test email.'

    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)

            
email_address = 'randomnesstest2@gmail.com'
automatic_email_sender(email_address)
