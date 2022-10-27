import re
import smtplib
import email.utils
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(server_address, port, sender, recipient, subject, body, payload_path):
    # include the payload as an attachment
    if payload_path:
        msg = MIMEMultipart()
        with open(payload_path, 'rb') as f:
            part = MIMEApplication(f.read(), Name=basename(payload_path))
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(payload_path))
        msg.attach(part)
    # no attachment
    else:
        msg = MIMEText(body)
        msg['To'] = email.utils.formataddr(('Recipient', recipient))
        msg['From'] = email.utils.formataddr(('Author', sender))
        msg['Subject'] = subject
    # if no external smtp server is provided, smtp debugging server will be used
    if server_address == '127.0.0.1' or server_address == 'localhost':
        client = smtplib.SMTP('127.0.0.1', port)
    # use external smtp server
    else:
        client.login(username, password)
        client = smtplib.SMTP(server_address, port)
    # Change to True to show communication with the server
    client.set_debuglevel(False)
    try:
        client.sendmail(sender, [recipient], msg.as_string())
        print('\nGungnir was sent flying.')
        print('Where you recognize evil, speak out against it, and give no truces to your enemies.\n')
    except Error as e:
        print(f"An error occured: {e.msg}")
    finally:
      client.quit()

# print the banner when the tool is run
print("""
                                     __                
   ____  __ __  ____    ____   ____ |__|______ 
  / ___\|  |  \/    \  / ___\ /    \|  \_  __ \ 
 / /_/  >  |  /   |  \/ /_/  >   |  \  ||  | \/
 \___  /|____/|___|  /\___  /|___|  /__||__|
/_____/            \//_____/      \/           

– They are truly wise who's travelled far and knows the ways of the world.

""")
# check that server address is valid
while True:
    server_address = input('Enter smtp server address [addr:port] (optional):\n')
    if not server_address:
        server_address = '127.0.0.1'
        port = 1025
        break
    if ':' in server_address and 'smtp.' in server_address:
        try:
            port = server_address.split(':')[1]
            port = int(port)
            server_address = server_address.split(':')[0]
            break
        except:
            print('\nInvalid address. Try again.\n')
    else:
        print('\nInvalid address. Try again.\n')

if server_address != '127.0.0.1' and server_address != 'localhost':
    username = input(f"\nEnter username (default: 'apikey'):\n")
    if not username:
        username = 'apikey'
    password = input('\nEnter password or apikey:\n')

while True:
    recipient = input(f"\nEnter the recipient's email address:\n")
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', recipient)
    if match:
        break
    else:
        print('\nNot a valid email address. Try again.')

while True:
    spoofed_address = input(f"\nEnter the sender's spoofed email address:\n")
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', spoofed_address)
    if match:
        break
    else:
        print('\nNot a valid email address. Try again.')

subject = input('\nEnter the subject of the email:\n')

message = input('\nEnter the message:\n')

payload_path = input('\nEnter the absolute path of payload file (optional):\n')

while True:
    # ask for confirmation
    print('=====================================================================')
    print(f"You're about to send Gungnir flying with the following parameters:\n")
    print(f"Server: {server_address}\nPort: {port}\nSender: {spoofed_address}\nReceiver: {recipient}\nSubject: {subject}\nMessage body: {message}\nPayload: {payload_path}\n")
    print('=====================================================================')
    confirmation = input('\nSend gungnir flying? [y/N]\n')
    if confirmation == 'y' or confirmation == 'Y':
        send_email(server_address, port, spoofed_address, recipient, subject, message, payload_path)
        break
    elif confirmation == 'n' or confirmation == 'N' or not confirmation:
        print('\nAborted. Email not sent.')
        print(f"The foolish man thinks he will live forever if he keeps away from fighting; but old age won't grant him a truce, even if the spears do.\n")
        break
    else:
        print('\nInvalid input.')