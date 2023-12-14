import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()

    # Email server setup
    my_email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_email, password)

    # Read recipients from CSV
    with open('job_contacts.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Create the message
            message = MIMEMultipart()
            message['From'] = my_email
            message['To'] = row['email']
            message['Subject'] = 'Job Application'

            # Email body
            body = f"Hello {row['name']},\n\nI am interested in the {row['position']} position at {row['company']}.\n\nBest regards,\n[Your Name]"
            message.attach(MIMEText(body, 'plain'))

            # Attach resume
            with open('path/to/your/resume.pdf', 'rb') as attachment:
                part = MIMEApplication(attachment.read(), Name='resume.pdf')
                part['Content-Disposition'] = 'attachment; filename="resume.pdf"'
                message.attach(part)

            # Send the email
            server.send_message(message)

    # Disconnect from the server
    server.quit()

if __name__ == "__main__":
    main()
