#EXERCÍCIOS DE LÓGICA DE PROGRAMAÇÃO")

#1)Escreva um programa que escreva seu nome na tela.

# Solicita o nome do usuário
#nome = input("Digite o seu nome: ")

# Exibe o nome na tela
#print("Olá,", nome, ", seja bem vindo Salesforce DEV!")

#2) Escreva um algoritmo para mostrar na tela a soma de dois números.

# Pedir a entrada de dois números e atribuir as varíaveis
#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))

# Calcular a soma dos números e mostrar o resultado
#soma = numero1 + numero2
#print(soma)

#3) Escreva um algoritmo para calcular o dobro de um número qualquer.

# Pedir o numero e atribuir a variavel
#fator1 = float(input("Digite o primeiro número: "))

# Calcular o dobro do numero e mostrar o resultado
#dobro = fator1 * 2
#print(dobro)

#4) Escreva um programa que receba duas variáveis, uma que seja o seu primeiro nome e uma que seja o seu sobrenome e escreva seu nome completo na tela.

# Pedir o nome e sobrenome do usuário
#nome = input("Digite o seu nome: ")
#sobrenome = input("Digite o seu sobre nome: ")

# Exibir o nome completo na tela
#print("Olá,", nome, sobrenome, ", seja bem vindo Salesforce DEV!")

#5) Os pares de instruções abaixo produzem o mesmo resultado?

#A <- (4 / 2) + (2 / 4) e A <- 4 / 2 + 2 / 4
#B <- 4 / (2 + 2) / 4 e B <- 4 / 2 + 2 / 4
#C <- (4 + 2) * 2 - 4 e C <- 4 + 2 * 2 – 4

# Analise de A
#A1 = (4 / 2) + (2 / 4)
#A2 = 4 / 2 + 2 / 4
#ResultadoA = A1 == A2
#print(ResultadoA)

# Analise de B
#B1 = 4 / (2 + 2) / 4
#B2 = 4 / 2 + 2 / 4
#ResultadoB = B1 == B2
#print(ResultadoB)

# Analise de C
#C1 = (4 + 2) * 2 - 4
#C2 = 4 + 2 * 2 - 4
#ResultadoC = C1 == C2
#print(ResultadoC)

#6) Reescreva as instruções abaixo com o mínimo de parênteses possível, mas sem alterar o resultado:

#A <- 6 * (3 + 2)
#B <- 2 + (6 * (3 + 2))
#C <- 2 + (3 * 6) / (2 + 4)
#D <- 2 * (8 / (3 + 1))
#E <- 3 + (16 - 2) / (2 * (9 - 2))
#F <- (6 / 3) + (8 / 2)
#G <- ((3 + (8 / 2)) * 4) + (3 * 2)
#H <- (6 * (3 * 3) + 6) - 10
#I <- (((10 * 8) + 3) * 9)
#J <- ((-12) * (-4)) + (3 * (-4))

#A = 6 * (3 + 2)
#print(A)
#B = 2 + 6 * (3 + 2)
#print(B)
#C = 2 + 3 * 6 / (2 + 4)
#print(C)
#D = 2 * 8 / (3 + 1)
#print(D)
#E = 3 + (16 - 2) / (2 * (9 - 2))
#print(E)
#F = 6 / 3 + 8 / 2
#print(F)
#G = ((3 + (8 / 2)) * 4) + (3 * 2)
#print(G)
#H = 6 * 3 * 3 + 6 - 10
#print(H)
#I = (10 * 8 + 3) * 9
#print(I)
#J = -12 * -4 + 3 * -4
#print(J)

#7) Analise os algoritmos abaixo e diga o que será impresso na tela ao serem executados:

#A = 10
#B = 20
#print(B) #20
#B = 5
#print(A, B) #10 5

#A = 30
#B = 20
#C = A + B
#print(C) #50
#B = 10
#print(B, C) #10 50
#C = A + B
#print(A, B, C) #30 10 40

#A = 10
#B = 20
#C = A
#B = C
#A = B
#print(A, B, C) #10 10 10

#A = 10
#B = A + 1
#A = B + 1
#B = A + 1
#print(A) #12
#A = B + 1
#print(A, B) #14 13

#A = 10
#B = 5
#C = A + B
#B = 20
#A = 10
#print(A, B, C) #10 20 15

#X = 1
#Y = 2
#Z = Y - X
#print(Z) #1
#X = 5
#Y = X + Z
#print(X, Y, Z) #5 6 1

#8) Faça um programa que calcule a média simples (aritmética) de 3 valores quaisquer. Utilize as variáveis valor1, valor2 e valor3.

# Entrada dos valores
#valor1 = float(input("Digite o primeiro valor: "))
#valor2 = float(input("Digite o segundo valor: "))
#valor3 = float(input("Digite o terceiro valor: "))

# Cálculo da média
#media = (valor1 + valor2 + valor3) / 3

# Exibição do resultado
#print(f"A média dos valores é: {media:.2f}")

#9) Escreva um algoritmo para ler um número e mostrar seu sucessor e seu antecessor, positivo ou negativo.

# Pedir o número e atribuir a variavel
#numero = float(input("Digite um número: "))
# Calcular o sucessor e antecessor
#sucessor = numero + 1
#antecessor = numero - 1
# Exibir o resultado
#print(f"O sucessor de {numero} é {sucessor} e o antecessor é {antecessor}.")

#10) Sabendo que a área quadrada é dada pela multiplicação dos lados, escreva um algoritmo que leia dois valores, correspondentes à Base e Altura de um retângulo e mostre a área quadrada de um espaço qualquer.
#Exemplo:
#A área de 3x9 é igual a 27
#3 * 9 = 27
# Pedir a base e altura do retângulo
#base = float(input("Digite a base do retângulo: "))
#altura = float(input("Digite a altura do retângulo: "))
# Calcular a área quadrada
#area = base * altura
# Exibir o resultado
#print(f"A área do retângulo é: {area} m²")

#11) Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B. A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram armazenados nas variáveis. Utilize o método de “Variável Auxiliar”.

# Armazenando os valores iniciais
#A = 10
#B = 20
#print(A, B)

# Troca utilizando variável auxiliar
#aux = A  #10
#print(aux, A, B)
#A = B  #10 e agora assumiu 20
#print(aux, A, B)
#B = aux  #20 e agora assumiu 10
#print(aux, A, B)

# Exibindo os valores após a troca
#print("Valor em A:", A)  #20
#print("Valor em B:", B)  #10
