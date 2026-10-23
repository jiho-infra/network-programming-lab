import socket
import threading

SERVER_IP = "10.10.34.23" 

def receive():
    while True:
        try:
            data = client.recv(1024)
        except OSError:
            break
        if not data:
            print("[서버 연결이 끊어졌습니다]")
            break
        print(data.decode())


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
client.connect((SERVER_IP, 50005))                       
print("접속 종료 커맨드: q")                              

threading.Thread(target=receive, daemon=True).start()

while True:                    
    # 클라이언트가 나가기   
    msg = input()
    if msg == "q":                          
        break
    client.send(msg.encode())


client.close()                                          
