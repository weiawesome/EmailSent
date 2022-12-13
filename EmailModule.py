from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path

class Email:
    def __init__(self,user,password):
        self.content = MIMEMultipart()
        self.user=user
        self.password=password
        self.content['from'] = user
        self.From = user
        self.ImgRoute=''
        self.FileRoute=''
        self.Cc=[]
        self.State=True
    def setTitile(self,title):
        self.Title = title
    def setReceive(self,receiver):
        self.To = receiver
    def setCc(self,Cc):
        self.Cc=str(Cc).split(',')
    def setContent(self,content):
        self.Content=content
    def attachImg(self,path):
        self.ImgRoute=path
    def attachFile(self,path):
        self.FileRoute=path
    def Send(self):
        with smtplib.SMTP(host='smtp.gmail.com') as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.user,self.password)
                self.content['to'] = self.To
                self.content['subject'] = self.Title
                self.content.attach(MIMEText(self.Content))
                if(len(self.ImgRoute)!=0):
                    self.content.attach(MIMEImage(Path(self.ImgRoute).read_bytes()))
                if(len(self.FileRoute)!=0):
                    File = MIMEApplication(open(self.FileRoute, 'rb').read())
                    File.add_header('Content-Disposition', 'attachment', filename=self.FileRoute)
                    self.content.attach(File)
                if(self.Cc==''):
                    smtp.send_message(self.content,to_addrs=[self.To]+self.Cc)
                else:
                    smtp.send_message(self.content)
                print('Sucess to send the email!')
                print('Content:')
                print(self.content)
            except Exception as e:
                print('Error to send the email!',e)