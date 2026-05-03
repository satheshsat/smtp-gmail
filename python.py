import smtplib
from email.message import EmailMessage

# 1. Define your email details
sender_email = "satheshs.sat@gmail.com"
receiver_email = "satheshs.sat@gmail.com"
password = "Your-password"  # Do NOT use your regular password; see security note below

# 2. Construct the message
msg = EmailMessage()
msg.set_content("This is a test email sent from Python!")
msg['Subject'] = "Python Email Test"
msg['From'] = sender_email
msg['To'] = receiver_email

# 3. Send the email via SMTP server
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
