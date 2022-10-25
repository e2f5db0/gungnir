import re

print("""
                                     __                
   ____  __ __  ____    ____   ____ |__|______ 
  / ___\|  |  \/    \  / ___\ /    \|  \_  __ \ 
 / /_/  >  |  /   |  \/ /_/  >   |  \  ||  | \/
 \___  /|____/|___|  /\___  /|___|  /__||__|
/_____/            \//_____/      \/           

– They are truly wise who's travelled far and knows the ways of the world.

""")

server_address = input('Enter smtp server address:\n')

while True:
    recepient = input(f"\nEnter the recepient's email address:\n")
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', recepient)
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
    confirmation = input('\nSend gungnir flying? [y/N]\n')
    if confirmation == 'y' or confirmation == 'Y':
        # send the email
        # TBA
        print('\nGungnir was sent flying.')
        print('Where you recognize evil, speak out against it, and give no truces to your enemies.\n')
        break
    elif confirmation == 'n' or confirmation == 'N' or not confirmation:
        print('\nAborted. Email not sent.')
        print(f"The foolish man thinks he will live forever if he keeps away from fighting; but old age won't grant him a truce, even if the spears do.\n")
        break
    else:
        print('\nInvalid input.')