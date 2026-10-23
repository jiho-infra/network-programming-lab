import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 50005))
server.listen()
print("접속을 기다립니다...")

while True:
    conn, addr = server.accept() # 객체가 또 객체가 된다(?) / 파이썬 문법적 질문
    print(addr, "에서 접속했습니다")

    while True:
        data = conn.recv(1024)
        if not data:
            print("클라이언트가 나갔습니다.")
            break ; 
        print("클라이언트:", data.decode())
        reply = input("서버:")
        conn.send(reply.encode()) 

    conn.close()

server.close()