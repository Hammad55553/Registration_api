# email_utils.py

import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "hammadaslam78612@gmail.com"
SENDER_PASSWORD = "twzo talg wris crnt"

def send_registration_email(receiver_email: str):
    subject = "Welcome to Our Pack Tracker App!"
    body = "Hello,\n\nThank you for registering on our platform.\n\nRegards,\nTeam"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
