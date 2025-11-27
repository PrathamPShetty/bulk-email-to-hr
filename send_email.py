import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


from data import sender_email, app_password, subject, body, filename


df = pd.read_csv("hr_emails.csv")
hr_emails = df.iloc[:, 2].dropna().tolist()   # clean list

print("Total HR Emails Found:", len(hr_emails))

for receiver_email in hr_emails:

    print(f"Sending to {receiver_email}...")

    # Create message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] =  receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "html"))

    # Attach resume
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={filename.split('/')[-1]}",
    )

    msg.attach(part)

    # Send email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {receiver_email}!")

    except Exception as e:
        print(f"Error sending to {receiver_email}: {str(e)}")

print("Process completed!")
