import smtplib

sender = 'zibrankhan786@gmail.com'
receivers = ['zibrankhan0313@gmail.com']

message = """From: From Person <zibrankhan786@gmail.com>
To: To Person <zibrankhan0313@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
