import socket
tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def connect_test(ip, port):
    try:
        tcp_client_socket.connect(ip, port)
    except:
        return False

    tcp_client_socket.send("0xc1".encode("utf-8"))
    feedback = tcp_client_socket.recv(1024)
    if feedback.decode("utf-8") == "0xc2":
        tcp_client_socket.close()
        return True
    else:
        tcp_client_socket.close()
        return False

def get_netconfig(ip,port):
    pass