import smtplib

def sendEmail():
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("senderemail","password" )
    server.sendmail("sendermail","to","Message: testing email automation")
    server.close()

sendEmail()
