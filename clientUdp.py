import socket 

target_host = "127.0.0.1"
target_port = 80

# criando objetos 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envia dados
client.sendto("AABBBCCC", (target_host, target_port))

# recebe dados 
data, addr = client.recvfrom(4096)

print data 