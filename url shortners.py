import pyshorteners

url = input("Enter the url : ")


#defin function 


def shortners(url):
    s = pyshorteners.Shortener()
    print (s.tinyurl.short(url))

shortners(url)