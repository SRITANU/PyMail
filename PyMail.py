import smtplib
import getpass

# Function of the PyMail Client


def mailsend(
        from_address,
        to_address_list,
        subject,
        message,
        login,
        password,
        smtpserver='smtp.gmail.com:587'):
    header1 = 'From : %s\n' % from_address
    header2 = header1 + 'To : %s\n' % ','.join(to_address_list)
    header = header2 + 'Subject:%s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    server.sendmail(from_address, to_address_list, message)


# Asks the user to enter his login id
log = raw_input("Enter your login id: ")

# Asks the user for his password
pwd = getpass.getpass()

# Asks the user for his email-address
from_addr = raw_input("Enter your email id :")

to_addr_list = []

# Asks the user the number of recipients
n = int(raw_input("How many recipients? "))

for i in range(n):
    # Asks the user to enter the recipient's email-id
    to_addr = raw_input("Enter the recipient's email id:")
    to_addr_list.append(to_addr)

# Subject of the mail
sub = raw_input("Enter your subject: ")

# Body of the mail
msg = raw_input("Enter your message: ")

# Calling the function
mailsend(
    from_address=from_addr,
    to_address_list=to_addr_list,
    subject=sub,
    message=msg,
    login=log,
    password=pwd)
