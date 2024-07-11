import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addr, body):
    from_addr = "c5ijx5ysqqjk2l2y@ethereal.email"
    login = "c5ijx5ysqqjk2l2y@ethereal.email"
    password = 'XC1M4kuWv49esuSVWk'

    msg = MIMEMultipart()
    msg["from"] = "trip_confirmer@email.com"
    msg["to"] = ', '.join(to_addr)
    msg["subject"] = "Trip Confirmation"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addr:
        server.sendmail(from_addr, email, text)
    
    server.quit()
