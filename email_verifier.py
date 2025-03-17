import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "email"
EMAIL_PASSWORD = "password"

def send_email_otp(to_email):
    otp = random.randint(100000, 999999)
    subject = "Your OTP Code"
    body = f"Your verification code is: {otp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

    return otp 

email = input("Enter your email: ")
otp_sent = send_email_otp(email)

otp_received = input("Enter the OTP received: ")

if otp_received == str(otp_sent):
    print("✅ Verification successful!")
else:
    print("❌ Incorrect OTP. Verification failed!")
