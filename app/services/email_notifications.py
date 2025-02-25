import smtplib
from email.mime.text import MIMEText
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USERNAME, EMAIL_PASSWORD

class EmailNotificationService:
    def __init__(self):
        self.smtp_server = EMAIL_HOST
        self.smtp_port = EMAIL_PORT
        self.username = EMAIL_USERNAME
        self.password = EMAIL_PASSWORD

    def send_email(self, recipient_email: str, subject: str, message: str):
        try:
            msg = MIMEText(message)
            msg["Subject"] = subject
            msg["From"] = self.username
            msg["To"] = recipient_email

            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.username, self.password)
                server.sendmail(self.username, recipient_email, msg.as_string())

            return "Email sent successfully."
        except Exception as e:
            return f"Error sending email: {str(e)}"
