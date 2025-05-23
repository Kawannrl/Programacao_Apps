class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.fome = 50
        self.higiene = 100
        self.mental = 100
        self.dinheiro = 50
        self.trabalho = None
        self.saude = 100

    def comer (self):
        if self.dinheiro < 10:
            return f"{self.nome} não tem dinheito para comer"
        else:
            self.fome = min (100, self.fome + 30)
            self.energia += 5
            self.dinheiro -= 10
            self.higiene -= 5
            self.mental += 15
            self.saude += 5
            return f"{self.nome} se alimentou"
        
    def dormir (self):
        if self.energia == 100:
            return f"{self.nome} não está com sono"

        else:
            self.energia = min (100, self.energia + 80)
            self.fome -= 15
            self.higiene -= 10
            self.mental += 50
            self.saude += 25
            return f"{self.nome} dormiu"
        
    def trabalhar (self):
        if self.energia < 35:
            return f"{self.nome} está muito cansado para ir trabalhar"
        
        else:
            self.energia -= 35
            self.fome -= 25
            self.mental -= 25
            self.higiene -= 15
            self.dinheiro += 40
            self.saude -= 10

    def treinar (self):
        if self.energia < 30:
            return f"{self.nome} está muito cansado para ir treinar"
        else:
            self.energia -= 30
            self.fome -= 30
            self.higiene -= 25
            self.mental += 35
            self.saude += 15

    def mostrar_status (self):
        return f"{self.nome}\n💤 Energia: {self.energia}\n🍽 Fome: {self.fome}\n🚿 Higiene: {self.higiene}\n🧠 Mental: {self.mental}\n💰 Dinheiro: {self.dinheiro}\n❤ Saúde: {self.saude}"

if __name__ == "__main__":
    obj1 = Personagem ("Detona Prato")
    # print (obj1.comer ())
    # print (obj1.fome)
    print (obj1.mostrar_status ())