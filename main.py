import sys
import smtplib
import secrets

from_addr = secrets.sender
to_addrs = secrets.sender
msg = """Essa mensagem foi enviada por um script em python.
Utilizando a biblioteca smtplib.
"""

try:
    s = smtplib.SMTP(secrets.smtp_host,587)
    s.login(secrets.sender, secrets.sender_password)
    s.sendmail(from_addr, to_addrs, msg)
    s.quit()
    print('E-mail enviado.')
except smtplib.SMTPException:
    print ("Erro:", sys.exc_info()[0])