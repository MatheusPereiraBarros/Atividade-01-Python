carlos = 0
andre = 0
felipe = 0
primeiroValor = 0
terceiroValor = 0
def racharConta(valorConta):
    primeiroValor = float(int(valorConta/3))
    terceiroValor = valorConta - (primeiroValor*2)
    print("O primeiro paga:", primeiroValor)
    print("O segundo paga:", primeiroValor)
    print("O terceiro paga:", terceiroValor)
    
def main():
    valorConta = float(input("Valor da conta: "))
    racharConta(valorConta)

main()
