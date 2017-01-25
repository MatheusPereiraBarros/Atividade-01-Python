pao = 0.12
broa = 1.50
valor = 0
#comentario
def fatura(quantPao, quantBroa):
    valor = (pao*quantPao)+(broa*quantBroa)
    print("A fatura do dia é: ", valor, "R$")
    print("Você deve guardar", valor*0.10, "R$ na poupança")
    

def main():
    #"1 2".split() = ["1", "2"]
    quantPao, quantBroa = [int(i) for i in input("Digite a quantidade de pão e broa vendidos hoje: ").split()]
    fatura(quantPao, quantBroa)

main()
