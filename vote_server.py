# Server to implement simple program to get votes tallied from two different
# clients. The server will wait until two different clients connect, before
#  sending a message down to each client.
# Author: Marc Grant 2019-09-26
# Version: 0.1
#!/usr/bin/python3
import random
import string 
import socket
import sys


def clientACK():
    """Generates client acknowledgment"""
    status = "200 OK"
    return status

def candidatesHello(str1,str2):
    """Generates client hello message"""
    status = "105 Candidates "+ str1 + "," + str2
    return status

        
def WinnerMsg(strWinner, votes):
    """Sends message with winner identified"""
    status = "220 Winner. " + strWinner + " " + votes
    return status

def RunnerUpMsg(strRunnerUp, votes):
    """Sends message with runner-up identified"""
    status = "221 Runner-up. " + strRunnerUp + " " + votes
    return status

klist=[11,12]
# s      = socket
# msg     = initial message being processed
# state  = dictionary containing state variables
def processMsgs(s, msg, status):
    """This function processes messages that are read through the socket. It
        returns a status, which is an integer indicating whether the operation
        was successful"""
    strWinner=''
    votes=''
    runnerup=''
    Rvote=''
    
   
    status =2
    str1="jack"
    str2="jill"
    if msg== "100 Hello":
        print("100 Hello.")
        
        res= candidatesHello(str1,str2)
        s.send(res.encode())
        status=1

    msg = msg.split('. ')

    if msg[0]=='110 Vote':
        print(msg[0])
        if msg[1]== 'jack':
            klist.insert(0,klist[0]+1)
            klist.remove(klist[1])
        elif msg[1] == 'jill':
            klist.insert(1,klist[1]+1)
            klist.remove(klist[2])
        ty=clientACK()
        s.send(ty.encode())
        status =1

            
        


        
        
    if msg[0]=='120 Poll closed':
        print(msg[0])
        
        
        if klist[0]>klist[1]:
            strWinner=str1
            votes=str(klist[0])
            runnerup=str2
            Rvote=str(klist[1])
        elif klist[1]>klist[0]:
            strWinner=str2
            votes=str(klist[1])
            runnerup=str1
            Rvote=str(klist[0])
            

        

        des=WinnerMsg(strWinner, votes)
        des1=RunnerUpMsg(runnerup, Rvote)
       # print(des)
        s.send(des.encode())
        #print(des1)
        s.send(des1.encode())
        status=-1



    

    if status==-1:
        print("Thanks for voting")
        
    return status

def main():
    """Driver function for the project"""
    args = sys.argv#['localhost',12000]
    if len(args) != 2:
        print ("Please supply a server port.")
        sys.exit()
    HOST = 'localhost'                # Symbolic name meaning all available interfaces
    PORT =  int(args[1])   # The port on which the server is listening
    if PORT < 1023 or PORT > 65535:
        print("Invalid port specified.")
        sys.exit()
        
    print("Server of MR. Brown")        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
       s.bind((HOST, PORT))# Bind socket
       s.listen(1) # listen
       print("Waiting for 2 connections")
       conn, addr = s.accept()# accept connection using socket
       print("Client_A has connected")
       conn1,addr = s.accept()# accept connection1 using socket
       print("Client_B has connected")
    


       
       with conn,conn1:
            print('Connected by', addr)
            status = 1
            while (status==1):
                msg = conn.recv(1024).decode('utf-8')
                msg = conn1.recv(1024).decode('utf-8')
                if not msg:
                    status = -1
                else:
                    status = processMsgs(conn, msg, status)
                    status = processMsgs(conn1, msg, status)
            if status < 0:
                print("Invalid data received. Closing")
            conn.close()        
            print("Closed connection socket")

    

if __name__ == "__main__":
    main()
