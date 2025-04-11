#preço de cada item do menu do restaurante

#dados do cliente
print("Bem vindo(a) à loja da Beatrice")
nome_cliente = input("Qual o seu nome? \n")

#declaração de preços
hamburguer = 23.90
babata_frita = 12.00
refrigerante = 9.50
milk_shake = 18.90
cafezinho = 7.00
coxinha = 9.00

#retornando o valor dos itens:
print(f"Olá {nome_cliente}! Este é o menu: ")
print(f"Hamburguer: {hamburguer}")
print(f"Bata frita: {babata_frita}")
print(f"Refrigerante: {refrigerante}")
print(f"Milk shake: {milk_shake}")

#definição da quantidade
quantidade_hamburguer = int(input("Digite a quantidade de hamburguer desejada: "))
quantidade_batata_frita = int(input("Digite a quantidade de batata frita desejada: "))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerante desejada: "))
quantidade_milk_shake = int(input("Digite a quantidade milk shake desejada: "))

#retornando o preço total
preco_total = (hamburguer * quantidade_hamburguer) + (babata_frita * quantidade_batata_frita) + (refrigerante * quantidade_refrigerante) + (milk_shake * quantidade_milk_shake)
print(f"{nome_cliente}, o valor do seu pedido é de R$ {preco_total:.2f}")
