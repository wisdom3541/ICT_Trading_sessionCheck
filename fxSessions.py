import datetime
import pytz

x = datetime.datetime
nyTimeZone = pytz.timezone("America/New_york")
y = (x.now().hour - x.now(nyTimeZone).hour)
z = x.now()
currentNyhourTime = z.hour - y


def checkLondon():
    for i in range(2, 5):
        if currentNyhourTime == i:
            return "Currently in London Trading session"


def checkNewyork():
    for i in range(7, 9):
        if currentNyhourTime == i:
            return "Currently in New York Trading session"


def session():
    ln = checkLondon()
    ny = checkNewyork()

    if ny and ln is not None:
        print("Currently not in ICT trading session")
    elif ln is not None:
        print(ln)
    elif ny is not None:
        print(ny)


session()
