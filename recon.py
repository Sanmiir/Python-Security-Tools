import sys

if len(sys.argv) < 3:
    print("Erro: Faltam argumentos. Uso: python recon.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]

try:
    port = int(sys.argv[2])
except ValueError:
    print("Erro: A porta deve ser um número inteiro.")
    sys.exit(1)

print("scanning host:", host)

class Target:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def show_info(self):
        print(f"Target Host: {self.host}, Target Port: {self.port}")

class Recon:
    def __init__(self, target):
        self.target = target
    def run(self):
        match self.target.port:
            case 22:
                print("Serviço SSH detectado")
            case 80:
                print("Serviço HTTP detectado")
            case 443:
                print("Serviço HTTPS detectado")
            case _:
                print("Serviço desconhecido")
                
        print("Reconhecimento concluído.")

meu_alvo = Target(host, port)
meu_alvo.show_info()
scanner = Recon(meu_alvo)
scanner.run()
