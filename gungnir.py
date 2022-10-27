import re
import smtplib
import email.utils
from email.mime.text import MIMEText

# if no external smtp server is provided, a simple smtp server will be used
def send_with_simple_server(sender, recipient, subject, body):
    msg = MIMEText(body)
    msg['To'] = email.utils.formataddr(('Recipient', recipient))
    msg['From'] = email.utils.formataddr(('Author', sender))
    msg['Subject'] = subject

    client = smtplib.SMTP('127.0.0.1', 1025)
    client.set_debuglevel(False) # show communication with the server
    try:
      client.sendmail(sender, [recipient], msg.as_string())
    finally:
      client.quit()

print("""
                                     __                
   ____  __ __  ____    ____   ____ |__|______ 
  / ___\|  |  \/    \  / ___\ /    \|  \_  __ \ 
 / /_/  >  |  /   |  \/ /_/  >   |  \  ||  | \/
 \___  /|____/|___|  /\___  /|___|  /__||__|
/_____/            \//_____/      \/           

– They are truly wise who's travelled far and knows the ways of the world.

""")

server_address = input('Enter smtp server address (optional):\n')

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

payload_path = input('\nEnter absolute path of a payload file (optional):\n')

while True:
    print('=====================================================================')
    print(f"You're about to send Gungnir flying with the following parameters:\n")
    print(f"Sender: {spoofed_address}\nReceiver: {recipient}\nSubject: {subject}\nMessage body: {message}\nPayload: {payload_path}\n")
    print('=====================================================================')
    confirmation = input('\nSend gungnir flying? [y/N]\n')
    if confirmation == 'y' or confirmation == 'Y':
        # send the email
        if not server_address or server_address == '127.0.0.1' or server_address == 'localhost':
            send_with_simple_server(spoofed_address, recipient, subject, message)
            print('\nGungnir was sent flying.')
            print('Where you recognize evil, speak out against it, and give no truces to your enemies.\n')
            break
        else:
            # send via external smtp server
            print('TBA external server')
    elif confirmation == 'n' or confirmation == 'N' or not confirmation:
        print('\nAborted. Email not sent.')
        print(f"The foolish man thinks he will live forever if he keeps away from fighting; but old age won't grant him a truce, even if the spears do.\n")
        break
    else:
        print('\nInvalid input.')