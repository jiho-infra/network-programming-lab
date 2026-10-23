import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 50005))
server.listen()
print("접속을 기다립니다...")

conn, addr = server.accept() # 튜플 언패킹 socket.socket() / 유저 정보
print(addr, "에서 접속했습니다")

data = conn.recv(1024)
print("받은 메세지:", data.decode())

conn.send("잘 받았습니다".encode())

conn.close()
server.close()