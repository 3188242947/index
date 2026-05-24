import socket
import time

# 创建TCP套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[客户端] 准备发起连接...")
time.sleep(1)

# connect()触发三次握手
print("[客户端] 发送 SYN...")
client.connect(('127.0.0.1', 8080))  # 三次握手在这里自动完成

print("[客户端] 收到 SYN+ACK，发送 ACK...")
print("[客户端] 三次握手完成，连接建立成功！")

# 发送一条消息
client.send("Hello！三次握手完成！".encode('utf-8'))

# 接收服务端的回复
reply = client.recv(1024)
print(f"[客户端] 收到服务端回复：{reply.decode('utf-8')}")

client.close()