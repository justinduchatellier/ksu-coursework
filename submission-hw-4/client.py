import socket, random, struct

port = 12345
# 1. create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 2. Make a connection to the server
sock.connect(('127.0.0.1', port))
address = ('127.0.0.1', port)
# 3. Send a request to the server
# 3.1 make a request
num = random.randint(0, 10)
# send_num = struct.pack("B", num)
sock.sendto(str(num).encode(), address)
# 4. receive a response from the server
str_svr_num, from_address = sock.recvfrom(2048)
str_svr_num = str_svr_num.decode()
svr_num = int(str_svr_num)
# svr_num = struct.unpack("l", svr_num)
print(int(svr_num))
# send message that operation ended successfully to server knows to stop
message = 0
sock.sendto(str(message).encode(), address)
# 5. close the socket
sock.shutdown(1)
sock.close()
