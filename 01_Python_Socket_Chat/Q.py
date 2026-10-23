import socket
import threading
import queue                                  # ★ ① 큐 모듈 추가

clients = []
q = queue.Queue()                             # ★ ① 메시지를 맡아 둘 큐

def handle(conn, addr):                       # 받기 담당 (사람마다 1명)
    print(addr, "입장 (현재", len(clients), "명)")
    while True:
        try:
            data = conn.recv(1024)
        except OSError:
            break
        if not data:
            break
        text = f"[{addr[0]}:{addr[1]}] {data.decode()}"
        q.put((conn, text))                   # ★ ② 직접 보내지 않고 큐에 넣기만
    clients.remove(conn)
    conn.close()
    print(addr, "퇴장 (현재", len(clients), "명)")

def broadcast():                              # ★ ③ 전달 담당 (서버 전체에 1명)
    while True:
        sender, text = q.get()                # 큐에서 꺼내기 (비어 있으면 기다림)
        print(text)
        for c in clients:
            if c != sender:
                try:
                    c.send(text.encode())
                except OSError:
                    pass

threading.Thread(target=broadcast, daemon=True).start()   # ★ ③ 전달 담당 시작

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 50005))
server.listen()
print("채팅 서버 시작 - 접속을 기다립니다...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle, args=(conn, addr), daemon=True).start()