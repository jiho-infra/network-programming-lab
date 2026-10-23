import socket

SERVER_IP = "127.0.0.1" # 다른 사람과 통신할 때는 서버 pc의 ip 입력

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1. 소켓 만들기
client.connect((SERVER_IP, 50005))                          # 2. 서버에 접속

print("접속 종료 커맨드: q")                                  # 3. 보내기
while True:                    
    # 클라이언트가 나가기   
    msg = input("나:")

    if msg == "q":                          
        break

    client.send(msg.encode())

    # 서버가 나가기                           
    data = client.recv(1024)
    
    if not data:
        print("상대가 나갔습니다")
        break

    print("상대:", data.decode())


client.close()                                              # 5. 접속 종료
