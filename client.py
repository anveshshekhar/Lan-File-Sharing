import socket   

s= socket.Socket()
host = input(str("Please enter address of the sender:"))
port = 8080
s.connect((host,port))
print("Connected ...")

filename = input(str("Enter name for file incoming:"))
file_data = s.recv(1048576)
file = open(filename , 'wb')
file.write(file_data)
file.close()
print("File has been stored successfully ...")