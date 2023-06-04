import requests

from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.youtube.com/results'
query = {'search_query': 'bmw'}

response = requests.get(url, params=query)

print(response.headers, 'headers')
print(response.status_code, 'status_code')
print(response.url, 'url')

url = 'https://httpbin.org/post'
query = [('search_query', 'bmw')]

response = requests.post(url, data=query)
print(response)


url = 'https://vseosvita.ua/test/kontrolna-robota-fizyka-atoma-ta-atomnoho-iadra-2648225.html'

query = [('search_query', 'a')]


response = requests.get(url, params=query)
print(response.headers, 'headers')
print(response.status_code)

import requests
from bs4 import BeautifulSoup


# Загрузка веб-страницы
page = requests.get("https://example.com")

# Создание объекта BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Поиск элементов на странице
results = soup.find_all('h2', class_='title')

# Создание списка данных
data = []
for result in results:
    data.append(result.text)

# Создание DataFrame из списка данных
df = pd.DataFrame(data, columns=['Заголовок'])

# Вывод DataFrame
print(df.head())














