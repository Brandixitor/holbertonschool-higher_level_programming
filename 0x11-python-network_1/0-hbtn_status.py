#!/usr/bin/python3
""""A Python script that fetches for https://intranet.hbtn.io/status""""
from urllib import request

if __name__ == "__main__":
    url = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('ascii'))
        
