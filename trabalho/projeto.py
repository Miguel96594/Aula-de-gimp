def main():
    nomeEscola = input("Digite o nome da escola: ")
    quantSalas = 0

    while quantSalas <= 0:
        quantSalas = int (input("dIGITE A QUANTIDADE DE SALAS: "))
        if quantSalas <= 0:
            print("Valor inválido")
    mediasEscola = [0.0] * quantSalas
    print(mediasEscola)
    
    return 0
main()