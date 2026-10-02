import socket

HOST = '127.0.0.1'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST,PORT))

print(f"[*] Emergency UDP server started on { HOST}:{PORT}")
print("[*] waiting  for  incoming  emergency alerts...\n")

try:
  while True:
    data,client_address = server_socket.recvfrom(1024)
    message = data.decode('utf-8')

    print(f"[ALERT RECEIVED] from {client_address}:{message}")

    response = f"ACK: Emergency notification received!"
    server_socket.sendto(response.encode('utf-8'),client_address)

except KeyboardInterrupt:
   print("\n[-] shutting down server...")
finally:
   server_socket.close()
