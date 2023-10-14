from django.core.mail import EmailMessage

def send(sub,b,m):
    email=EmailMessage(sub,b,to=m)
    email.send()