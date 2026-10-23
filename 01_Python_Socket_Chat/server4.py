import socket
import threading

clients = []

def handle(conn, addr):
    print(addr, "입장 (현재", len(clients), "명))")
    while True:
        try:
            data = conn.recv(1024)
        except OSError:
            break
        if not data:
            break
        text = f"[{addr[0]}:{addr[1]}] {data.decode()}"
        print(text)
        for c in clients:
            if c != conn:
                try:
                    c.send(text.encode())
                except OSError:
                    pass
    clients.remove(conn)
    conn.close()
    print(addr, "퇴장 (현재", len(clients), "명))")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 50005))
server.listen()
print("접속을 기다립니다...")

while True:
    conn, addr = server.accept() # 객체가 또 객체가 된다(?) / 파이썬 문법적 질문\
    clients.append(conn)
    threading.Thread(target=handle, args=(conn, addr), daemon=True).start()
