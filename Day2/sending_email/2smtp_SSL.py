
import smtplib
from email.message import EmailMessage

EMAIL_ADD = ''                                 #senders email            
EMAIL_PASS = ''                                 #app generated password

msg = EmailMessage()
msg['Subject'] = 'grab dinner'
msg['From'] = EMAIL_ADD
msg['To'] = ''                              #receivers email
msg.set_content('whats cooking?')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADD ,EMAIL_PASS)
    smtp.send_message(msg)
