# Gungnir (spear phishing tool)

![Gungnir](https://github.com/e2f5db0/gungnir/blob/main/img/gungnir.png)

## How do phishing countermeasures work?

Any legitimate email server performs some checks when receiving email. These checks will determine whether a phishing email will actually arrive to the receiver's inbox or end up in the spam folder.  

### Sender Policy Framework (SPF)

An SPF TXT record is a DNS record that helps prevent spoofing and phishing by verifying the domain name from which email messages are sent. SPF validates the origin of email messages by verifying the IP address of the sender against the alleged owner of the sending domain. 

### DomainKeys Identifier Mail (DKIM)

DKIM is a protocol that allows an organization to take responsibility for transmitting a message by signing it in a way that mailbox providers can verify. DKIM record verification is made possible through cryptographic authentication.

First, the sender identifies what fields they want to include in their DKIM record signature. These fields include the “from” address, the body, the subject, and many others. These fields must remain unchanged in transit, or DKIM authentication will fail.

### DMARC check

A DMARC TXT record is a DNS record, which can be used to validate the origin of email messages by verifying the IP address of an email's author against the alleged owner of the sending domain.

## Bypassing the countermeasures

Many services send email to their customers using third-party solutions such as Mailgun, SendGrid, Mailtrap, etc. which handle SPF, DKIM and DMARC for the services. This means that the services must have allowed their email to go through these third-parties, which means that if a spear phishing email spoofing a service domain is sent through the correct third-party (e.g. SendGrid), the phishing email has a higher probability of bypassing the checks.

## System goals

This tool can be used to send a targeted spear phishing email. If no external smtp server is set, a simple debugging server will be started. Emails sent through this server will not pass any of the checks used to counter phishing and spoofing.

## System architecture

Gungnir is a command line tool written in python. The system consists of the command line interface and a simple smtp server, which starts up if no external smtp server has been provided during the configuration of gungnir (i.e. running the tool).

## Components / modules

- SMTP Debugging server: [Python SMTP Server](http://docs.python.org/library/smtpd.html)
    - Can be used to view the raw contents of the spoofed emails.

- The smtp library: [smtplib](https://docs.python.org/3/library/smtplib.html)
    - Actually sends the spoofed emails with the parameters given by the user.

## Communication channels (between the components)

The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.

![smtp-protocol](https://github.com/e2f5db0/gungnir/blob/main/img/smtp-protocol.png)

source: https://www.rfc-editor.org/rfc/rfc821 

## Pros & cons of the open-source components

The smtp server built-in Python can't be used as an actual smtp server, which would bypass any spoofing checks made by the receiver's email server. It could be configured to sign the email header fields with a key but this would not help much without the real keys of the spoofed domain.

## Integration / extension by other systems

Gungnir could be easily extended or integrated by other systems as is, because the tool is essentially just a python script. It can run as a part of other systems with minimal or zero modification given that the external smtp servers are configured by the user.

## Evaluation of the project

Although the configuration of external smtp servers (SaaS) are fairly uniform, the tool has not been actually tested with a multitude of external smtp servers. Servers typically use tokens or username/password combinations to authenticate senders and the code should be compatible with most servers, but this has not been thoroughly tested. The versatility of accepted payloads and field values can be tested fairly well with the built-in smtp debugging server. Most payloads are accepted (e.g. executable binary attachments).

## Avenues for future work

- Although Gungnir is a spear phishing tool, it could be easily extended to accommodate larger phishing campaigns with multiple receivers.

- At the moment there is no way for the user to know if the external smtp server is reachable or not. For example the port could be wrong and the user wouldn't know.

- The payloads could be renamed before sending. Now the user needs to rename the payload file before running Gungnir.

# Configuration & usage

Clone the repository:
```bash
git clone git@github.com:e2f5db0/gungnir.git
```

Spin up the smtp debugging server (not needed if using an external smtp server):
```bash
$ python3 -m smtpd -c DebuggingServer -n localhost:1025
```

Run Gungnir:
```bash
$ python3 gungnir.py
```

An example run of the tool using the debugging server:

![example-run](https://github.com/e2f5db0/gungnir/blob/main/img/example-run.png)

Debugging server output:

![debugging-server-output](https://github.com/e2f5db0/gungnir/blob/main/img/debugging-server.png)