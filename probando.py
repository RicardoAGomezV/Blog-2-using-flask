from email.message import EmailMessage
import smtplib

from parameters import MY_EMAIL, MY_PASSWORD

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(MY_EMAIL, MY_PASSWORD)

msg = EmailMessage()
msg['Subject'] = 'subject prueba'
msg['From'] = MY_EMAIL
msg['To'] = MY_EMAIL
content="probando"
msg.set_content(content)

# sending the mail
s.send_message(msg)

# terminating the session
s.quit()