import datetime
import pytz

x = datetime.datetime
nyTimeZone = pytz.timezone("America/New_york")
y = (x.now().hour - x.now(nyTimeZone).hour)
z = x.now()
currentNyhourTime = z.hour - y
dow = x.now().strftime("%A")


def checkAsian():
    for i in range(19, 21):
        if currentNyhourTime == i:
            return "Currently in Asian Trading session"


def checkLondon():
    for i in range(2, 5):
        if currentNyhourTime == i:
            return "Currently in London Trading session"


def checkNewyork():
    for i in range(7, 10):
        if currentNyhourTime == i:
            return "Currently in New York Trading session"


def checkLondonClose():
    for i in range(10, 12):
        if currentNyhourTime == i:
            return "Currently in London Close Trading session"


def getSession():
    ln = checkLondon()
    ny = checkNewyork()
    an = checkAsian()
    lc = checkLondonClose()

    if an is not None:
        print(an)
    elif ln is not None:
        print(ln)
    elif ny is not None:
        print(ny)
    elif lc is not None:
        print(lc)
    else:
        print("Market Closed!! No Trading During the Weekend")


weekend = ["Saturday", "Sunday"]
for i in weekend:
    if dow == i:
        print("Market Closed!! No Trading During the Weekend")
        break
    else:
        getSession()