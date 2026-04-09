import socket

# prendre une IP en argument, scanner les ports 1 à 1024, afficher les ports ouverts.

'''socket.connect() 
socket.accept()
socket.getpeername()
socket.timeout() 
socket.getaddrinfo()
'''
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0, None) as s:
host = " "
port = 443 
r = range(1, 1024)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Entrez l'adresse ip que vous souhaitez scanner : ")
host = input(">")

s.connect_ex((host, port))
'''s.recv(s.connect)
'''
print(f"le port {r} est ouvert")