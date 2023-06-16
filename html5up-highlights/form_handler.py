import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
from flask import Flask, request

app = Flask(__name__)

@app.route('/form_handler.py', methods=['POST'])
def handle_form_submission():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Email configuration
    sender_email = 'dohakhamaiseh1999@gmail.com'
    sender_name = 'Doha'
    recipient_email = 'dohakhamaiseh22@gmail.com'
    subject = 'Form Submission'

    # Compose email message
    msg = MIMEMultipart()
    msg['From'] = formataddr((str(Header(sender_name, 'utf-8')), sender_email))
    msg['To'] = recipient_email
    msg['Subject'] = subject

    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login('dohakhamaiseh1999@gmail.com', 'DJK221023')
            smtp_server.sendmail(sender_email, recipient_email, msg.as_string())
        return 'Email sent successfully!'
    except Exception as e:
        return f'Error sending email: {str(e)}'

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
