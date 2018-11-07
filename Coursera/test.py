import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('https://docs.google.com/forms/d/1i0T8Tl2dsATvADtcuecDUGfcq6y3aNiZ_RBwQATogPg/edit#responses')
for line in fhand:
    print(line.decode().strip())
