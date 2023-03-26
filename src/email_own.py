import smtplib
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rkrameshkanna11@gmail.com', 'lwrvdgazdiwrixvb')
    server.sendmail('rkrameshkanna11@gmail.com', to, content)
    server.close()