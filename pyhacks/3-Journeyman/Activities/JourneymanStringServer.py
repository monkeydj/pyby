import socket



def main():
    HOST  = 'localhost'
    PORT  = 50001    
    message_list = ['alpha' , 'bravo' , 'charlie' , 'delta']
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.bind((HOST , PORT))
    
    for i in message_list:
        s.listen(1)
        conn, addr = s.accept()
        print conn, addr
        print 'sending', i
        conn.send(i)
        conn.close()
        
main()
