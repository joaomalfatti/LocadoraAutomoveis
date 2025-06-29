import os

carrosDisponiveis = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130),
]
alugados = []


print("============")
print("Bem vindo à locadora de carros.")
print("============")

### Função os carros disponíveis.
def mostrar_lista_de_carros(carrosDisponiveis):
    for codigo, car in enumerate(carrosDisponiveis):
        print("[{}] {} - R$ {} /dia.".format(codigo, car[0], car[1]))
mostrar_lista_de_carros(carrosDisponiveis)

### Interface mostrar os carros.

while True:
    os.system("cls")
    print("============")
    print("Bem vindo à locadora de carros.")
    print("============")
    print("O que deseja fazer? ")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    op = int(input())

    os.system("cls")
    if op == 0:
        mostrar_lista_de_carros(carrosDisponiveis)
    elif op == 1:
        mostrar_lista_de_carros(carrosDisponiveis)
        print("============")
        print("Escolha o código do carro: ")
        cod_car = int(input())
        print("Por quantos dias você deseja alugar este carro? ")
        dias = int(input())
        os.system("cls")

        print("Você escolheu o {} por {} dias.".format(carrosDisponiveis[cod_car][0], dias))
        print(" O aluguel totlizaria R$ {}. Deseja aluga?".format(dias * carrosDisponiveis[cod_car][1]))

        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print("Parabéns você alugou o {} por {} dias.".format(carrosDisponiveis[cod_car][0], dias))
            alugados.append(carrosDisponiveis.pop(cod_car))
    elif op == 2:
        if len(alugados) == 0:
            print("Não há carros para devolver.")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver? ")
            mostrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            cod = int(input())
            if conf == 0:
                print("Obrigado por devolver o carro {}". format(alugados[cod][0]))
                carrosDisponiveis.append(alugados.pop(cod))
    
    print("============")
    print("0 - CONTINUAR | 1 - SAIR")
    if int(input()) == 1:
        break