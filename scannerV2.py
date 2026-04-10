import socket 
import sys
'''
creer un host pour entrer l'ip avec input
faire un boucle pour scanner chaque port 
    dans la boucle, declarer un socket,
    settimeout
    capturer le connect((hosrt, port))
    print port ouvert
    close 

appeler la fonction

je crois

'''

host = sys.argv[1]
temps_par_scan = sys.argv[2]
temps_par_scan = float(temps_par_scan)
scan_all = sys.argv[3]
#host = input("Entrez l'adresse ip a scanner : ")
#temps_par_scan = input("Entre le temps en secondes pour un scan : ")
#temps_par_scan = float(temps_par_scan)
 
def scanner(host, temps_par_scan, scan_all):
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(temps_par_scan)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"port {port} ouvert")
        elif scan_all == "1":
            print(f"port {port} ferme.")
        s.close()
        

scanner(host, temps_par_scan, scan_all)

