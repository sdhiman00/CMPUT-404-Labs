import requests

response = requests.get('https://raw.githubusercontent.com/sdhiman00/CMPUT-404-Labs/main/lab-1.py')
open('lab1.txt', 'wb').write(response.content)
with open('/Users/smriti/Desktop/lab-1/lab1.txt', 'r') as f:
    print(f.read())