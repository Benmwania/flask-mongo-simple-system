import os

class Config:
    SECRET_KEY = 'your_secret_key'
    MONGO_URI = 'mongodb://localhost:27017/simple_flask_app'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@gmail.com'
    MAIL_PASSWORD = 'your_email_password'
