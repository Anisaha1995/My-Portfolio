import smtplib,ssl
import os

def send_email(message_1):
    host = "smtp.gmail.com"
    port = 465
    user = "piyassrabony2014@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "piyassaha0@gmail.com"

    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(user, password)
        server.sendmail(user, receiver, message_1)



