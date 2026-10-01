 import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.blind(("127.0.0.1",5000))

print("UDP Emergency server started...")
print("waiting for  emergency message...")

while true:
   data,address=server.recvfrom(1024)

   message = data.decode()

   print("Emergency message received:", message)
   print("From:",address)
