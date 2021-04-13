import argparse, socket

parser = argparse.ArgumentParser()
parser.add_argument('targetHost', help='insert target host')
parser.add_argument('targetPort', help='insert target port')
args = parser.parse_args()


target_host = args.targetHost

target_port = int(args.targetPort)

#create a socket obj

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client

client.connect((target_host, target_port))

#send data
string = 'GET / HTTP/1.1\r\nHost:'+target_host+'\r\n\r\n'
str2send = bytes(string, 'utf-8')

client.send(str2send)

#receive data

response = client.recv(4096)

print(response.decode())
client.close()



