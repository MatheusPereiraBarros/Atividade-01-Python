pesoQueijo = 0.05
pesoPresunto = 0.05
pesoHamburger = 0.1
quantQueijo = 0
quantPresunto = 0
quantHamburger = 0

def calcularCompra(quantSand):
    quantQueijo = quantSand*pesoQueijo*2
    quantPresunto = quantSand*pesoPresunto
    quantHamburger = quantSand*pesoHamburger
    print("%d kg de queijo, %d kg de presunto, %d kg de hamburger" % (quantQueijo, quantPresunto, quantHamburger))
    
def main():

    quantSanduiche = int(input("Quantidade de sanduiches: "))
    calcularCompra(quantSanduiche)

main()
