import socket, logging, math, struct

logging.basicConfig(level=logging.ERROR)

port = 12345
# 1. create a socket
listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 2. bind the socket with IP address and port number
listener.bind(('', port))
# 3. generate a listener
# listener.listen(0)
# 4. wait for a connection request
# 4.1 making a connection
while True:
    str_num, address = listener.recvfrom(2048)  # waits for a connection request
    # when to stop, if client is done
    str_num = str_num.decode()
    if int(str_num)  == 0:
        break
    else:
        # 4.2 getting data from the client
        num = int(str_num)
        print("num is ", num)
        # 4.3 parse the data from the client
        num_factorial = math.factorial(num)
        # struct.pack("l", num_factorial)
        # 4.3 sending a response to the client
        listener.sendto(str(num_factorial).encode(), address)
        listener.shutdown(1)  # signal close of the writing side of the socket
    # 5. close the socket and terminate program
listener.close()
