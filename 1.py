pequeno = 10
medio = 12
grande = 15
valor = 0

def calcularValor(quantPequeno, quantMedio, quantGrande):
    valor = (pequeno*quantPequeno) + (medio*quantMedio) + (grande*quantGrande)
    print("O valor arrecadado com as camisas é:", valor,"R$")

def main():
    quantPequeno = int(input("Insira a quantidade de camisas pequenas: ")) 
    quantMedio = int(input("Insira a quantidade de camisas medias: "))
    quantGrande = int(input("Insira a quantidade de camisas grandes: "))
    calcularValor(quantPequeno, quantMedio, quantGrande)
    
main()
