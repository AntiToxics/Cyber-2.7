import socket

MAX_MSG_LENGTH_SIZE = 1024

def send(sock: socket.socket, msg):

    """"
    msg = dir C:\
    msg = dir#C:\
    send((1024-7)*0 + 7) 000000....0007
    send(msg)
    """
    msg = msg.replace(" ", "#").encode()
    if len(msg) > MAX_MSG_LENGTH_SIZE:
        raise Exception("Message too big")

    msg_size = b'0' * (MAX_MSG_LENGTH_SIZE - len(msg)) + bytes(len(msg))
    print("Message Length Size:", len(msg_size))
    sock.send(msg_size)
    sock.send(msg)

def recv(sock: socket.socket):
    """
    msg_length = 00000.....000007
    msg_length = 7
    sock.recv(7)
    msg = dir#C:\
    [dir, C:\]
    """
    msg_length = sock.recv(MAX_MSG_LENGTH_SIZE)
    msg = sock.recv(int(msg_length)).decode()
    print(msg.split("#"))

    """"
    msg = msg.decode()
    index = msg.find("#")
    length = msg[:index]
    index2 = index+1
    for char in msg[index+1:]:
        if char == "#":
            return [msg[index+1:index2],msg[index2:]]
        else:
            index2 = index2+1
    """



   # index2 = new_msg.find("#")
  #  return [str(len(msg)),msg[index+1:],new_msg[index2+1:]]


    # 1024#screenshot#C:\temp\screenshot.txt

