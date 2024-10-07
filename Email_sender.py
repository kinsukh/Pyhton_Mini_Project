import smtplib

to = input("Enter the  recipient's email address: ")

subject = input("Enter the subject of the email: ")

body = input("Enter the body/content of the email: ")

def send_email(to, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("Sender_gmail_add_@gmail.com", "password_for_mail")
    message = 'Subject: {}\n\n{}'.format(subject, body)
    server.sendmail("Sender_gmail_add_@gmail.com", to, message)
    server.quit()
    print("Email sent successfully!")

send_email(to,subject,body)

## make sure to replace Sender_gmail_add_@gmail.com and password_for_mail with your actual Gmail account credentials
## make sure to allow less secure apps in your account settings to run this script