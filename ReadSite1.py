import requests

link = "http://www.somesite.com/details.pl?urn=2344"
f = requests.get(link)

#f = urlopen(link)
myfile = f.read()
myfile1 = myfile.decode()

print(f.text)