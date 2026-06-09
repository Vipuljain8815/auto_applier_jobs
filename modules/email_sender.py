import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import ssl

def send_application_email(to_email, subject, body, resume_path, gmail_user, gmail_password):
    """
    Sends an email with a resume attached using Gmail's SMTP server.
    """
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = gmail_user
        message['To'] = to_email
        message['Subject'] = subject

        # Attach body
        message.attach(MIMEText(body, 'plain'))

        # Open the resume file in binary mode
        if os.path.exists(resume_path):
            with open(resume_path, 'rb') as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            filename = os.path.basename(resume_path)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message
            message.attach(part)
        else:
            print(f"Warning: Resume not found at {resume_path}. Sending without attachment.")

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to Gmail SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, to_email, message.as_string())
            
        print(f"Successfully sent email to {to_email}")
        return True

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        return False
