import smtplib
from email.message import EmailMessage
import getpass

def send_email(smtp_server, port, sender, receiver, subject, body, password):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

def main():
    print("===== SIMPLE EMAIL SENDER =====")
    smtp_server = input("SMTP server (e.g., smtp.gmail.com): ").strip() or "smtp.gmail.com"
    port_input = input("Port (default 587): ").strip()
    port = int(port_input) if port_input else 587
    sender = input("Your email: ").strip()
    receiver = input("To email: ").strip()
    subject = input("Subject: ").strip()
    print("Enter message body (single line):")
    body = input().strip()
    print("Note: For Gmail, create an App Password and use it here (do NOT share your password).")
    password = getpass.getpass("Email password / app password: ")

    try:
        send_email(smtp_server, port, sender, receiver, subject, body, password)
        print("✔ Email sent.")
    except Exception as e:
        print("❌ Failed to send email:", e)

if __name__ == "__main__":
    main()
