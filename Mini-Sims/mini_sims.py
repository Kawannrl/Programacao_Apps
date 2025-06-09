class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.dia = 0
        self.energia = 100
        self.fome = 50
        self.higiene = 100
        self.mental = 100
        self.dinheiro = 50
        self.trabalho = None
        self.tralho_nivel = 0
        self.saude = 100

    def comer (self):
        if self.dinheiro < 10:
            return f"{self.nome} não tem dinheito para comer"
        else:
            self.fome = min (100, self.fome + 30)
            self.energia = min (100, self.energia + 5)
            self.dinheiro = max (0, self.dinheiro - 10)
            self.higiene = max (0, self.higiene - 5)
            self.mental = min (100, self.mental + 15)
            self.saude = min (100, self.saude + 5)
            return f"{self.nome} se alimentou"
        
    def dormir (self):
        if self.energia == 100:
            return f"{self.nome} não está com sono"

        else:
            self.energia = min (100, self.energia + 80)
            self.fome = max (0, self.energia - 15)
            self.higiene = max (0, self.higiene - 10)
            self.mental = min (100, self.mental + 50)
            self.saude = min (100, self.saude + 25)
            self.dia += 1
            return f"{self.nome} dormiu"
        
    def trabalhar (self):
        if self.energia < 35:
            return f"{self.nome} está muito cansado para ir trabalhar"
        
        else:
            self.energia = max (0, self.energia - 35)
            self.fome = max (0, self.fome - 25)
            self.mental = max (0, self.mental - 25)
            self.higiene = max (0, self.higiene - 15)
            self.dinheiro = min (100, self.dinheiro + 40)
            self.saude = max (0, self.saude - 10)

    def treinar (self):
        if self.energia < 30:
            return f"{self.nome} está muito cansado para ir treinar"
        else:
            self.energia = max (0, self.energia - 30)
            self.fome = max (0, self.fome - 30)
            self.higiene = max (0, self.higiene - 25)
            self.mental = min (100, self.mental + 35)
            self.saude = min (100, self.saude + 15)
            
    def tomar_banho (self):
        if self.higiene == 100:
            return f"{self.nome} não precisa tomar banho"
        else:
            self.energia = min (100, self.energia + 10)
            self.higiene = min (100, self.higiene + 75)
            self.mental = min (100, self.mental + 25)
            self.saude = min (100, self.saude + 10)
            
    def ser_contratado (self, objeto_trabalho):
        self.trabalho = objeto_trabalho
        self.tralho_nivel = 1
        return f"{self.nome} foi contratado na carreira de {self.trabalho.carreira} no cargo {self.trabalho.ver_cargo (self.tralho_nivel)}"
        
    def ser_demitido (self, objeto_trabalho):
        self.trabalho = objeto_trabalho
        self.trabalho_nivel = 1
        return f"{self.nome} foi demitido da carreira {self.trabalho.carreira} do cargo {self.trabalho.ver_cargo (self.trabalho_nivel)}"
        
    def pedir_demissao (self, objeto_trabalho):
        pass
        
    def mostrar_status (self):
        return f"{self.nome}\n💤 Energia: {self.energia}\n🍽 Fome: {self.fome}\n🚿 Higiene: {self.higiene}\n🧠 Mental: {self.mental}\n💰 Dinheiro: {self.dinheiro}\n❤ Saúde: {self.saude}"
    
class Trabalho:
    def __init__(self, carreira, cargos, salarios, energia, fome, higiene, mental, saude):
        self.__carreira = carreira
        self.__cargos = cargos
        self.__salarios = salarios
        self.__energia_gasta = energia
        self.__fome_gasta = fome
        self.__higiene_gasta = higiene
        self.__mental_gasta = mental
        self.__saude_gasta = saude
        
    @property
    def informacoes (self):
        return f'''Carreira: {self.__carreira} \nCargos: {self.__cargos} \nSalários: {self.__salarios} \nEnergia: {self.__energia_gasta} \nFome: {self.__fome_gasta} \nHigiene: {self.__higiene_gasta} \nMental: {self.__mental_gasta} \nSaúde: {self.__saude_gasta}'''

    @property
    def carreira (self):
        return self.__carreira
    
    def ver_cargo (self, nivel):
        return self.__cargos [nivel-1]

if __name__ == "__main__":
    carreira = "Cozinheiro"
    cargos = ["Cozinheiro profissional", "Pedreiro"]
    salarios = [30, 40, 75]
    energia = -45
    fome = -30
    higiene = -25
    mental = 20
    saude = -20
    
    objeto_trabalho = Trabalho (carreira, cargos, salarios, energia, fome, higiene, mental, saude)
    mensagem = objeto_trabalho.informacoes
    print (mensagem)
    
    objeto_pessoa = Personagem ("Detona Prato")
    # mensagem = objeto_pessoa.ser_contratado (objeto_trabalho)
    mensagem = objeto_pessoa.ser_demitido (objeto_trabalho)
    print (mensagem)