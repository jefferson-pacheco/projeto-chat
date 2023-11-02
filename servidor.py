"""Primeiro passo para criar um servidor de chat """
import socket
import threading

HOST = '10.0.0.15'
PORT = 61570

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

#Terceiro passo criar broadcast serve para conectar todas as pessoa do chat para receber as mensagens
def broadcast(sala, mensagem):
    for i in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()
        

        i.send(mensagem)
#Qaurto passo para receber as mensagem do chat e enviar mensagem
def enviarMensagem(nome, sala, client):
    while True:
        mensagem = client.recv(1024)
        mensagem = f"{nome}: {mensagem.decode()}\n"
        broadcast(sala, mensagem)
#Segundo passo criar o loop que vai receber as informçoes no sevidor
while True:
    client, addr = server.accept()
    client.send(b'SALA')
    sala = client.recv(1024).decode()
    nome = client.recv(1024).decode()
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)
    print(f'{nome} se conectou na sala {sala}! INFO {addr}')
#esta ligado ao terceiro passo
    broadcast(sala, f'{nome}: Entrou na sala!\n')
#esta ligado ao quarto passo
    thread = threading.Thread(target=enviarMensagem, args=(nome, sala, client))
    thread.start()
