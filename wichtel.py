import random
import smtplib

fromaddr = 'fromuser@gmail.com'
toaddrs  = 'touser@gmail.com'
msg = 'There was a terrible error that occured and I wanted you to know!'


# Credentials (if needed)
username = ''
password = ''

def sendMail(fromaddr, toaddrs, msg):
    FROM = fromaddr
    TO = toaddrs #must be a list
    SUBJECT = "Wichtel"
    TEXT = "You're have to buy a present for %s" % (FROM)

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
    fopen = open(text, 'r')
    names = []
    for line in fopen:
        fields = line.split('\t')
        names.append(fields[0])
        #eMail.append(fields[1])

    return names

def createEmailList(text):
    fopen = open(text, 'r')
    eMail = {}
    for line in fopen:
        fields = line.split('\t')
        eMail[fields[0]] = fields[1][0:-1]
        #print fields[1]

    return eMail

def findWichtelPartner(names):
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


def createText(text):
    eMail = createEmailList(text)
    names = createNameList(text)
    partner = findWichtelPartner(names)

    for name in partner.keys():
        print "Dear %s,\nthe great secret santa algorithm has chosen %s as your partner." % (name, partner[name])
        print "This Email was automatically sent to:", eMail[name], ". For further information please check: www.github.com/"
        print "
