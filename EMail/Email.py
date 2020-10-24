import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

class Email (object):
        def __init__(self, subject, body):
            self.subject=subject
            self.body=body
        
        def SendMail(self, to_address, from_address, from_password=None, connection_type='SSL'):
            if from_password==None:
                from_password=getpass(prompt='Password: \n', stream=None) 
            
            # Server Authentication
            server=self.ServerAuthentication(from_address, from_password, connection_type)
            
            # Message Creation
            message = MIMEMultipart()
            message['From']=from_address
            message['To']=to_address
            message['Subject']=self.subject
            message.attach(MIMEText(self.body, 'plain'))
            text=message.as_string()
            
            # Message Sending
            try:
                server.sendmail(from_address, to_address, text)
                print('[INFO] Email sent')
                print('From: ' + from_address)
                print('To: ' + to_address)
                print('Subject: ' + message['Subject'])
            except:
                print('[ERROR] Email delivery failed')
            
            server.quit()
            return None 
            
        def ServerAuthentication(self, from_email, from_password, connection_type='SSL'):            
            
            # Server Authentication
            try:
                if connection_type=='SSL':
                    server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo
                if connection_type=='TLS':
                    server=smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo
                    server.starttls()
            except:
                print('[ERROR] Server not responding')
            
            # Server Login
            try: 
                server.login(from_email, from_password)
                print('[INFO] Server login successful')
                
            except:
                print('[ERROR] Server login failed')
                                       
            return server
    