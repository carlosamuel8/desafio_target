
# ler um número
# verificar se o número pertence a sequência de Fibonacci
# se pertencer, imprimir uma mensagem informando que o número pertence a sequência
# se não pertencer, imprimir uma mensagem informando que o número não pertence a sequência

numero = int(input("Digite um número: "))
anterior = 0
atual = 1
proximo = 0

while proximo < numero:
    proximo = anterior + atual
    anterior = atual
    atual = proximo

if proximo == numero:
    print("O número pertence a sequência de Fibonacci")
else:
    print("O número não pertence a sequência de Fibonacci")

