#citytourtravel1@gmail.com
#citytourtravel2021
from email.message import MIMEPart
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

correo = 'citytourtravel1@gmail.com'
correo_password = 'citytourtravel2021'

def send_email(html=None, text='Email body', subject='Hello',  from_email='', to_emails=[]):
    assert isinstance(to_emails, list)
    msg=MIMEMultipart('alternative')
    msg['From']=from_email
    msg['To']=", ".join(to_emails)
    msg['Subject']=subject
    txt_part = MIMEText(text,'plain')
    msg.attach(txt_part)

    html_part = MIMEText(f"{html}", 'html')
    msg.attach(html_part)
    msg_str=msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(correo,correo_password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()