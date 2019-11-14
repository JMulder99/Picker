import random
import smtplib

gmail_user = '<naam@gmail.com'
gmail_password = '<wachtwoord>'
def picker(range):
    pick = random.randint(0, len(range)-1)
    return pick

persoon = [<lijst_van_personen>] # zelfde volgorde
kiest = [<lijst_van_personen>] # zelfde volgorde
emails = [<lijst_van_mail_adres>] # zelfde volgorde
while persoon != []:
    persoon1 = persoon[0]
    to = emails[0]
    file = persoon1 + ".txt"
    koppel = kiest[picker(kiest)]
    persoon.remove(persoon1)
    kiest.remove(koppel)
    emails.remove(to)
    koppelkoppel = persoon1 + " trok " + koppel
    sent_from = gmail_user
    subject = 'OMG Super Important Message'
    body = koppelkoppel

    email_text = """
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')
        
