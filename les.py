import requests


response = requests.get('https://www.w3schools.com/python/module_requests.asp')

print(f'text - {response.text}')


print(f'type - {type(response)}')

print(f'dir {dir(response)}')
print(f'content - {response.content}')

print(f'json - {response.json()}')

print(f'headers - {response.headers}')

print(f'status - {response.status_code}')













