class Veiculo:
    def __init__(self):
        self.nome = None
        self.design = None
        self.cor = None
        self.valor = None
        self.ano = None
        self.status = None

    def criar_carro(self, nome, design, cor, valor, ano, status):
        self.nome = nome
        self.design = design
        self.cor = cor
        self.valor = valor 
        self.ano = ano
        self.status = status

        print("Nome:", self.nome)
        print("Design:", self.design)
        print("Cor:", self.cor)
        print("Valor:", self.valor)
        print("Ano:", self.ano)
        print("Status:", self.status)

class Cliente:
    def cliente (self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco

        print ("Nome: ", self.nome)
        print ("CPF: ", self.cpf)
        print ("Telenone: ", self.telefone)
        print ("Endereço: ", self.endereco)

class Locacao:
    def locacao (self, cliente, carro, valor, forma_pagamento, data, quantidade_de_dias):

        if carro.status != "Disponivel":
            print (f"Não tem o carro {carro.nome} disponível para locação")
        else:
            self.cliente = cliente
            self.carro = carro
            self.valor = valor
            self.forma_pagamento = forma_pagamento
            self.data = data
            self.quantidade_de_dias = quantidade_de_dias

            print ("Clinte: ", cliente.nome)
            print ("Carro: ", carro.nome)
            print ("Valor: ", self.valor)
            print ("Forma de Pagamento: ", self.forma_pagamento)
            print ("Data: ", self.data)
            print ("Quantidade: ", self.quantidade_de_dias)

if __name__ == "__main__":
    meu_carro = Veiculo()
    meu_carro.criar_carro("Dodge Dart", "Modelo Esportivo", "Preto", "50.000", "1980", "Disponivel")
    
    novo_cliente = Cliente ()
    novo_cliente.cliente ("Rodrigo", "000.000.000-11", "41 99999 9999", "?\n")

    locacao = Locacao ()
    locacao.locacao (novo_cliente, meu_carro, "2.500", "Boleto", "05/06/2025", "1")