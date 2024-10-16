# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

def verificar_paridade(numero):
    if numero % 2 == 0:
        return f"o numero {numero} e par."
    else:
        return f"o numero{numero} e impar." 

numero_input = int(input("digite um numero"))

resultado = verificar_paridade(numero_input)

print(resultado)