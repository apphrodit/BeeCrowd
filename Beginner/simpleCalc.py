#Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
#o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

#Entrada

#O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros
# e um valor com 2 casas decimais.

#Saída
#A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo,
#lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". 
#O valor deverá ser apresentado com 2 casas após o ponto.


#######

# A função split

#######

peca1, qtdP1, valorP1 = input().split()
peca2, qtdP2, valorP2 = input().split()

qtdP1 = int(qtdP1)
valorP1 = float(valorP1)

qtdP2 = int(qtdP2)
valorP2 = float(valorP2)

calc = (qtdP1 * valorP1) + (qtdP2 * valorP2)

print(f"VALOR A PAGAR: R$ {calc:.2f}")