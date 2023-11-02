import socket

HOST = '10.0.0.15'
PORT = 61570

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

mensagem = client.recv(1024)
if mensagem == b'SALA':
    client.send(b'Games')
    client.send(b'jefferson')
    