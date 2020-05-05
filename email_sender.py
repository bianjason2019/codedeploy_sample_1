pip install smtplib
pip install ssl

import smtplib, ssl
port = 465  # For SSL
smtp_server = "smtp.qq.com"
sender_email = "1767824623@qq.com"  # Enter your address
receiver_email = "bianjason@126.com"  # Enter receiver address
password = "zoedsbmylutnedie"
message = """\
Subject: Hi there

This is a test message sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
