# required imports
import smtplib
import ssl

#list of recipient
tolist=["k.plachta@hotmail.com","k.plachta@hotmail.com", "pekson.production@gmail.com"]

# making connection
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

# login password
server.login('pekson.production@gmail.com', "srfosybkklfmsspm")

# Email Subject and content to send
subject = 'hello world from python!'
body = 'this is email body send from python script'

msg = f"Subject: {subject}\n\n{body}"

# msg = '''\
# ... From: pekson.production@gmail.com
# ... Subject: testin'...
# ...
# ... This is a test '''

# from to
server.sendmail('pekson.production@gmail.com',tolist,msg)

# print just simple message to confirm you that email was sent
print('email was sent')

# close program
server.quit()
