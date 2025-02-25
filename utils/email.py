from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def send_reset_email(email):
    msg = Message('Password Reset Request',
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[email])
    msg.body = 'Click the link below to reset your password.'
    mail.send(msg)
