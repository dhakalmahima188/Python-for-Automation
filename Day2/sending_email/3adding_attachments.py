
import smtplib
from email.message import EmailMessage

EMAIL_ADD = ' '                         #senders name
EMAIL_PASS = ''                         #app generated password
                
msg = EmailMessage()
msg['Subject'] = 'check out my village'
msg['From'] = EMAIL_ADD
msg['To'] = ' '                         #receivers email
msg.set_content('Image attached....')
with open('village.jpeg','rb') as f:
    file_data = f.read()
    file_type = 'jpeg'
    file_name = f.name
msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:


    smtp.login(EMAIL_ADD ,EMAIL_PASS)

    smtp.send_message(msg)
