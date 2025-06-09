class Animal:
    def __init__(self, nome_cientifico):
        self.__nome_cientifico = nome_cientifico
        
    @property
    def nome_cientifico (self):
        return self.__nome_cientifico
    
    def falar (self):
        print ("Sou um animal gemérico")
        
class Cachorro (Animal):  # A classe cachorro herda da classe animal
    def __init__ (self, nome_cientifico, racao_favorita):
        super ().__init__ (nome_cientifico)
        self.racao_favorita = racao_favorita
        
    def falar (self):
        print ('Sou um cachorro, au au!')
    
class Gato (Animal):
    def __init__(self, nome_cientifico, tamanho_bigode):
        super ().__init__ (nome_cientifico)
        self.tamanho_bigode = tamanho_bigode
        
    def falar(self):
        print ('Sou um gato, miau miau!')

if __name__ == "__main__":
    objeto_cachorro = Cachorro ('Canis lupus Caramelis', 'Pedigri')
    objeto_cachorro.falar ()
    print (objeto_cachorro.nome_cientifico)
    
    objeto_gato = Gato ('Gatus Pretus', 10)
    objeto_gato.falar ()
    print (objeto_gato.nome_cientifico)