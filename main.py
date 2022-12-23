import smtplib
#python library to use SMPT protocol for Emails

print(server)

server = smtplib.SMTP('smtp.gmail.com', 587)
#Hardcoding Server Details

server.starttls()
#Starting server using transport layer security.

server.login('awsmanglu@gmail.com', 'uiceviextwufbfbv')
#Gmail Dummy creds for app.

server.sendmail('awsmanglu@gmail.com', 'dhruvohra@gmail.com', 'Mail sent from python script run via jenkins using gmail smtp server')
# This is taking 3 Parameters as arguments as of now Sender Address, recipient Address, Email Body.
