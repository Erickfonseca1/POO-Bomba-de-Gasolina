
class Bomba:

    def __init__(self):
        print("Construindo Bomba...{}".format(self))
        
    def abastece (self, valor, combustivel):
        if combustivel == "Gasolina":
            valor = (valor / 6.50)
            print("Foram abastecidos {}L de {}, volte sempre!".format(valor, combustivel))
        elif combustivel == "Alcool":
            valor = (valor / 5.00)
            print("Foram abastecidos {}L de {}, volte sempre!".format(valor, combustivel))
        else:
            print("Combustível inserido é inválido, abastecimento cancelado")

        

