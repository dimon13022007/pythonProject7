import requests

# url = 'http://lib.ru/INOSTRHIST/SENKEWICH/kamo_gryadeshi.txt'
#
# response = requests.get(url)

# with open('test_1.txt') as file:
#     file.write(response.text)


# print(response.encoding)
# with open('text_2.txt', 'w') as f:
#     for piece in response.iter_lines(chunk_size=5000):
#         print('piece ...')
#         f.write(piece.decode(response.encoding))


url = 'http://www.ukr.net'

response = requests.get(url)

with open('text_3', 'w') as f:
    f.write(response.text)



















