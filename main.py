import smtplib
import os
#python library to use SMPT protocol for Emails

server_type = os.environ['Server']

if server_type == 'smtp.gmail.com':
  port = 587
elif server_type == 'smtp.office365.com':
  port = 587
elif server_type == 'smtp.mail.yahoo.com':
  port = 465
  

sender_address = os.environ['Sender']
sender_password = os.environ['Sender_pass']
recipient_address = os.environ['Recipient']
email_content = os.environ['email_message']


print(os.environ['email_message'])
print(type(os.environ['email_message']))


server = smtplib.SMTP(server_type, port)
#Hardcoding Server Details

server.starttls()
#Starting server using transport layer security.

server.login(sender_address, sender_password)
#Gmail Dummy creds for app.

server.sendmail(sender_address, recipient_address, email_content)
# This is taking 3 Parameters as arguments as of now Sender Address, recipient Address, Email Body.
