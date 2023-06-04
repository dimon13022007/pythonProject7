import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))  #>1024

server.listen(10)

print('Working now....')
client_socket, address = server.accept()
data = client_socket.recv(1024).decode('utf-8')
print(data)

Hdrs = 'HTTP/1.1 200 ok\r \n Content Type: text/html; charset=utf-8\r\n\r\n'

content = 'Hi! ... server  working ... '.encode('utf-8')
client_socket.send(Hdrs.encode('utf-8') + content)


print('Shutdown this shit ...')














