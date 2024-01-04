figura = int(input( " Digite uma alternativa \n 1- círculo \n 2 - triângulo\n 3 - retângulo"))

if figura == 1:
    raio = float(input("Digite o valor do raio"))
    area = raio * raio * 3.14
    print("A área do círculo é", area)
elif figura == 2:
    base = float(input( "Digite o valor da base"))
    altura = float(input("Digite a altura"))
    area = (base*altura)/2
    print("A área do triângulo é", area)
elif figura == 3:
    base = float(input("Digite o valor da base"))
    altura = float(input("digite o valor da altura"))
    area = base * altura
    print("A área do retângulo é",area)
else:
    print("Digite 1, 2 ou 3")