#!/usr/bin/env python2.7
import smtplib
import sys
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("humblecryptohacker@gmail.com", "hacker@123")
msg=sys.argv[1]
#Send the mail
#msg = "Hello!" # The /n separates the message from the headers
server.sendmail("humblecryptohacker@gmail.com", "vnt.darda@gmail.com", msg)
server.sendmail("humblecryptohacker@gmail.com", "animesh920@gmail.com", msg)
