import socket 

HOST = '127.0.0.01'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(3.0)

message = "EMERGENCY: system failure detected in sector 3!"

try:
  print(f"[*] sending alert to {HOST}:{PORT}...")
  client_socket.sendto(message.encode('utf-8'),(HOST,PORT))

  response_data, server_address = client_socket.recvfrom(1024)
  print(f"[SERVER RESPONSE] { response_data.decode('utf-8')}")

except socket.timeout:
   print("[-] Request timed out! Is server.py running?")
except Exception as e:
  print(f"[-] Error: {e}")
finally:
  client_socket.close()
