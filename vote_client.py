# Client to collect votes from a client and send them to a server.
# Author: Marc Grant 2019-09-26
# Version: 0.1
#!/usr/bin/python3

import socket
import sys


def serverHello():
    """Generates server hello message"""
    status = "100 Hello"
    return status


def voteNotification(strCandidate):
    """Generates message to let server know of user selection."""
    if strCandidate=='jack':
        print("jack selected")
        status = "110 Vote. " + strCandidate
    
        
    elif strCandidate=='jill':
        print("jill selected")
    
        status = "110 Vote. " + strCandidate
    
    return status

def pollClosing():
    """Generates message to let server know of poll closing."""
    status = "120 Poll closed"
    return status

# s       = socket
# msg     = initial message being processed
# state   = dictionary containing state variables
def processMsgs(sy, msg,status):
    """This function processes messages that are read through the socket. It
        returns a status, which is an integer indicating whether the operation
        was successful"""
    
    """You will need to complete this method """
    status = 2
    if msg == '105 Candidates jack,jill': #check if the message is valid 
        print("Server said hello")
        print(msg)
        nes=input("Enter a Candidate(no Capital letters): ")
        nes=str(nes)
        pes=voteNotification(nes)
        sy.send(pes.encode())
        status = 1

    msg = msg.split('. ')
    

    if msg[0]=="200 OK":
       print(msg[0])
       ges=input("Would you like to cast another vote N/Y")
       if ges=="N":
           es=pollClosing()
           sy.send(es.encode())
           status=1
       elif ges=="Y":
           vt= input("Enter a Candidate(no Capital letters): ")
           vt=str(vt)
           bt=voteNotification(vt)
           sy.send(bt.encode())
           status=1


    if msg[0]=="220 Winner":
        print(msg[0]+" "+msg[1])
        status=1
        
    if msg[0]=="221 Runner-up":
        print(msg[0]+" "+msg[1])
        status=1

    if status == 2: # end processMsgs
        print('Incoming message was not processed. \r\nTerminating Server')


    
    
    return status

def main():
    """Driver function for the project"""
    args = sys.argv#['localhost',11000]
    if len(args) != 2:
        print ("Please supply a server address and port.")
        sys.exit()
    serverHost = 'localhost'       # The remote host
    serverPort =  int(args[1])       # The same port as used by the server
    
    print("Client of ____ A")
    
    # Add code to initialize the socket
    #msg = serverHello()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverHost,serverPort))
    h = serverHello().encode()
    s.send(h)
    
    status = 1
    while (status == 1):
        msg = s.recv(1024).decode('utf-8')
        if not msg:
            status = -1
        else:
            status = processMsgs(s, msg, status)
    if status < 0:
        print("Invalid data received. Closing")   
    s.close()
    print("Closed connection socket")  
   
    # Add code to send data into the socket
    
    # Handle the data that is read through the socket by using processMsgs(s, msg, state)
    
    # Close the socket.
    
    #print(msg[0])
    #if msg[0]=="221 Runner-up jack 0":
     #   print(msg[0])
      #  status=1 
   # if msg[0]=="221 Runner-up jill 0":
    #    print("\n")
     #   print(msg[0])
      #  status=1'''
if __name__ == "__main__":
    main()
