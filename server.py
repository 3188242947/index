import socket

# 创建TCP套接字
# AF_INET = IPv4地址类型
# SOCK_STREAM = TCP协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定本机IP和端口
server.bind(('127.0.0.1', 8080))

# 开始监听，最大等待连接数128
server.listen(128)
print("[服务端] 等待客户端连接...(SYN)")

# accept()会阻塞，直到有客户端连接
# 返回一个新的套接字和客户端地址
client_socket, client_addr = server.accept()
print(f"[服务端] 收到SYN，来自 {client_addr}")
print("[服务端] 发送 SYN+ACK...")

# 接收客户端发来的数据
data = client_socket.recv(1024)
print(f"[服务端] 收到ACK，连接建立成功！")
print(f"[服务端] 收到消息：{data.decode('utf-8')}")

# 回复客户端
client_socket.send("你好，客户端！握手成功！".encode('utf-8'))

# 关闭连接
client_socket.close()
server.close()