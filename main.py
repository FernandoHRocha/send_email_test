import sys
import smtplib

from_addr = 'sender@example.com'
to_addrs = ['recipient@example.com']
msg = """From: Sender
To: Recipient
Subject: This is the message subject

This is the message body.
"""

try:
    s = smtplib.SMTP('localhost')
    s.login('sender@example.com', 'password')
    s.sendmail(from_addr, to_addrs, msg)
    s.quit()
except smtplib.SMTPException:
    print "Error:", sys.exc_info()[0]