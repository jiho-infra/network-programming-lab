import socket

SERVER_IP = "127.0.0.1" # 다른 사람과 통신할 때는 서버 pc의 ip 입력

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1. 소켓 만들기
client.connect((SERVER_IP, 50005))                          # 2. 서버에 접속

client.send("안녕하세요".encode())                            # 3. 보내기

data = client.recv(1024) #receive                           # 4. 받기
print("서버 답장:", data.decode())

client.close()                                              # 5. 접속 종료
