import smtplib
import os
from email.message import EmailMessage
from string import Template
from pathlib import Path
from dotenv import load_dotenv
#env 
load_dotenv()
name=os.getenv("NAME")
password=os.getenv("PASSWORD")

#email content
email=EmailMessage()
email['subject']="you won 10000000 dollars"
email['to']="sureshpradhana3@gmail.com"
email['from']='Dev Testing'
html=Template(Path('index.html').read_text())
email.set_content(html.substitute({'name':'traveller'}),'html')

#send email

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login(name,password)
	smtp.send_message(email)




