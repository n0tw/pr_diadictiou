import requests  

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = 'http://eclass.upatras.gr/'  

with requests.get(url) as response:  
    html = response.text
    server = response.headers.get('Server')
    if server:
        print("server")
    more(html)