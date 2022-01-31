import smtplib
print('Sending Mail..')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
with open('email.txt', 'r') as e:
    email = e.read()    
with open('password.txt', 'r') as p:
    password = p.read()  
server.login(email, password)
server.sendmail(email,email,'Keep it going')
print('Mail Sent')