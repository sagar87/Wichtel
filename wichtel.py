import random
import smtplib


### Specify the eMail address of the organizer and set the username and password of the outgoing SMTP server.
fromaddr = ''
username = ''
password = ''

def sendMail(fromaddr, toaddrs, msg):
    """
    sendMail sends a Mail to person (toaddr) with a message defined in (msg).
    """
    FROM = fromaddr
    TO = toaddrs
    SUBJECT = "Secret Santa Gift Exchange"
    TEXT = msg

    # Prepare actual message
    message = "\From: %s\nTo: %s\nSubject: %s\n\n%s" % (FROM, TO, SUBJECT, TEXT)
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()

def createNameList(text):
    """
    Takes a tabs top separated txt-file as input and returns a list which
    contains all persons participating in secret santa.

    In order to process the txt-file correctly, the txt-file should have
    this format:

    forename surname*TABSTOP*eMail address
    """
    fopen = open(text, 'r')
    names = []
    for line in fopen:
        fields = line.split('\t')
        names.append(fields[0])
        #eMail.append(fields[1])

    return names

def createEmailDic(text):
    """
    Takes a tabs top separated txt-file as input and returns a dictionary which
    contains all persons and their eMail adresses.

    In order to process the txt-file correctly, the txt-file should have
    this format:

    forename surname*TABSTOP*eMail address
    """
    fopen = open(text, 'r')
    eMail = {}
    for line in fopen:
        fields = line.split('\t')
        eMail[fields[0]] = fields[1][0:-1]
        #print fields[1]

    return eMail

def findWichtelPartner(names):
    """
    Takes a list of names and assigns to each name another name. FindWichtelPartner
    returns a dictionary with all randomly chosen names.
    """
    copy1 = list(names)
    copy2 = list(names)
    partner = {}
    while len(copy1) != 0:
    #for i in range(0, len(names)):
        name1 = random.choice(copy1)
        name2 = random.choice(copy2)
        #print name1, name2
        if name1 == name2:
            pass
        else:
            partner[name1] = name2
            copy1.remove(name1)
            copy2.remove(name2)

    return partner


def createTextAndSendMail(text):
    """
    This function finally sends the mails to all guests.
    """
    eMail = createEmailDic(text)
    names = createNameList(text)
    partner = findWichtelPartner(names)

    for name in partner.keys():
        msg = """Dear %s,\n\nthe Secret Santa Script has (randomly) chosen %s as your partner.

We (the people attending the X-ray crystallography course) spontaneously decided to make a christmas dinner next week (further informations will be posted on fb). To spice things up a bit we want to organize a Secret Santa Gift Exchange, therefore, your have to get a present for %s (max. 5 Euro).

This Email was sent automatically to: %s. If you want to organize your own Secret Santa Gift Exchange you may want to use pieces of paper, otherwise check: https://github.com/sagar87/Wichtel/ ;). \n""" % (name.split(' ')[0], partner[name], partner[name].split(' ')[0], eMail[name])
        #print msg
        sendMail(fromaddr, eMail[name], msg)
