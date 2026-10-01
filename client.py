import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


message = input("Enter emergency message:")


client.sendto(message.encode(),("127.0.0.1",5000))

print("Emergrncy message sent!")
