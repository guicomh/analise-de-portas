import socket 

host = input("Ip: ")
portas = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080]


ip = socket.gethostbyname(host)

def analise_porta():
    print(f"Conectando a {ip}")
    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = s.connect_ex((host, porta))

        if resultado == 0:
            print(f"porta {porta} está aberta!")
        s.close()

analise_porta()

pause = input("\nAperte Enter para Sair")

# ============================================
# Desenvolvido por https://github.com/guicomh 
# ============================================