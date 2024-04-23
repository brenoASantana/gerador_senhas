import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")
    comprimento = int(input("Insira o comprimento da senha desejada: "))
    
    senha = gerar_senha(comprimento)
    print("Sua senha gerada é:", senha)

if __name__ == "__main__":
    main()
