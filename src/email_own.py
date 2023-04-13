import smtplib
import imaplib
import time
from bs4 import BeautifulSoup

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rkrameshkanna11@gmail.com', 'lwrvdgazdiwrixvb')
    server.sendmail('rkrameshkanna11@gmail.com', to, content)
    server.close()

class Mail:
    T = time.time()
    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password
        self.M = imaplib.IMAP4_SSL('imap.gmail.com')
        self.M.login(self.user, self.password)
        
    def checkMail(self) -> int:
        self.M.select('inbox')
        self.unRead = self.M.search(None, '(UNSEEN FROM "narayanandvsurya@gmail.com" SUBJECT "Test")')
        print(len(self.unRead[1][0].split()))
        return len(self.unRead[1][0].split())

    def readLatest(self):
        ids = self.unRead[1][0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        print(ids)
        print(id_list)
        result, data = self.M.fetch(latest_email_id, "(RFC822)")
        raw_body = data[0][1]
        
        parsedContent = BeautifulSoup(raw_body, 'html.parser')
        result = parsedContent.find('div').get_text()
        # result = parsedContent.get_text(parsedContent.find('div'))
        # print(parsedContent.prettify() + '\n\n\n')
        return result

email = Mail('dbvenkat857@gmail.com', "qlmrnzadkwfzbhqh")
