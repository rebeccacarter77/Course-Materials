import urllib.request, urllib.parse, urllib.error

inp=input('Enter URL-')

try:
    fhand=urllib.request.urlopen(inp)
except:
    print('URL incorrect')
    quit()

count=0
for line in fhand:
    new=len(line)
    line.rstrip()
    count=count+new
    if count<3000:
        print(line.decode())
    else: break

print('There are',count,'characters on this page')
