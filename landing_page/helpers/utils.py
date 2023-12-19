from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def email_send(sender, subject, messages):
    receiver_email = 'potadi.ai@gmail.com'
    receiver_password = 'iakm cwfn etjh myve'
    
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(messages, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(receiver_email, receiver_password)
        server.sendmail(sender, receiver_email, message.as_string())
        server.quit()
        # print('Email terkirim dengan sukses')
    except Exception as e:
        print(f'Gagal mengirim email: {str(e)}')        