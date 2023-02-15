import os
import smtplib                              #inbuilt
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method




password = os.environ.get('password')
print(password)
email_add = '076bct033.mahima@pcampus.edu.np'                              #senders email
passwd_pass  = password                          #app generated password
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login( email_add , passwd_pass)

    subject = 'hello'
    body = 'Happy valientines day! '

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(email_add , 'dhakalmahima18@gmail.com', msg)     #receivers email
