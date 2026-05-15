import smtplib,ssl
host = "smtp.gmail.com"
port = 465
user = "piyassrabony2014@gmail.com"
password = "iilqknwfqttuxgvw"
receiver = "piyassaha0@gmail.com"
message = """\
Subject: Test Mail
Dear Piyas,
How are you?
"""
my_context = ssl.create_default_context()
with smtplib.SMTP_SSL(host,port,context=my_context) as server:
    server.login(user, password)
    server.sendmail(user,receiver,message)

