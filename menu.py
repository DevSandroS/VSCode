#preço de cada item do menu do restaurante

#declaração de preços
hamburguer = 23.90
babata_frita = 12.00
refrigerante = 9.50
milk_shake = 18.90

#definição da quantidade
quantidade_hamburguer = int(input("Digite a quantidade de hamburguer desejada: "))
quantidade_batata_frita = int(input("Digite a quantidade de batata frita desejada: "))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerante desejada: "))
quantidade_milk_shake = int(input("Digite a quantidade milk shake desejada: "))

#retornando o preço total
preco_total = (hamburguer * quantidade_hamburguer) + (babata_frita * quantidade_batata_frita)