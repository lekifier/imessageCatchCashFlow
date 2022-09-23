# coding=utf-8
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class InoutEmail:
    def __init__(self, config):
        self.ssl_port = config['MAILINFO']['SSLport']
        self.smtp_server = config['MAILINFO']['SMTPServer']
        self.smtp_license = config['MAILINFO']['SMTPLicense']
        self.email_sender = config['MAILINFO']['EmailSender']
        self.email_receiver = config['MAILINFO']['EmailReceiver']
        self.email_subject = config['DAILYMAILINFO']['EmailSubject']

    def sendMail(self, content):
        msg = MIMEMultipart()
        msg['From'] = self.email_sender
        msg['To'] = self.email_receiver
        msg['Subject'] = self.email_subject
        msg.attach(MIMEText(content, 'plain'))
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(
            self.smtp_server, self.ssl_port, context=context)
        server.login(self.email_sender, self.smtp_license)
        server.sendmail(self.email_sender,
                        self.email_receiver, msg.as_string())
        server.quit()
