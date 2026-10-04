import socket
import threading

HOST, PORT = '127.0.0.1', 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive_messages():
    while True:
        try:
            data, _ = client_socket.recvfrom(1024)
            print(f"\n[BROADCAST RECEIVED] {data.decode('utf-8')}\n> ", end="")
        except:
            break

try:
    print("[*] Registering with server...")
    client_socket.sendto(b"REGISTER", (HOST, PORT))
    resp, _ = client_socket.recvfrom(1024)
    print(f"[SERVER RESPONSE] {resp.decode('utf-8')}")

    threading.Thread(target=receive_messages, daemon=True).start()

    print("\n[*] Enter alert text (or 'exit' to quit):")
    while True:
        msg = input("> ")
        if msg.lower() == 'exit':
            break
        if msg.strip():
            payload = f"ALERT: {msg}"
            client_socket.sendto(payload.encode('utf-8'), (HOST, PORT))

except Exception as e:
    print(f"[!] Error: {e}")
finally:
    client_socket.close()

