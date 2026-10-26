import smtplib
from email.message import EmailMessage

msg=EmailMessage()
msg["subject"]="practical exam"
msg["from"]="vidya@gmail.com"
msg["to"]="lol@gmail.com"
msg.set_content("hello world")

with smtplib.SMTP("smpt.example.com,587")as server:
    server.starttls()
    server.login("sender@example.com","APP_PASSWORD")
    server.send_message(msg)
print("email sent")

