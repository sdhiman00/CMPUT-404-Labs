import requests

response = requests.get('https://raw.githubusercontent.com/sdhiman00/CMPUT-404-Labs/main/lab-1.py')
print(response.text)