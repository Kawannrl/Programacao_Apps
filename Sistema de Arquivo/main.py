class Arquivo:
    def __init__ (self, nome, data, tamanho, tipo):
        self.nome = nome
        self.data = data
        self.tamanho = tamanho
        self.tipo = tipo
        
    def ver_nome (self, nome):
        return print (f"O nome do Aquivo: {nome}")
    
    def ver_data_criacao (self, data):
        return print (f"Aquivo criado: {data}")
    
    def ver_tamanho (self, tamanho):
        return print (f"Tamanho do Arquivo: {tamanho}")
    
    def ver_extensao (self, tipo):
        return print (f"Tipo do Arquivo: {tipo}")
        
class Diretorio:
    def __init__ (self, nome):
        self.nome = nome
        self.lista_diretorios = []
        self.lista_arquivos = []
        
    def adicionar_arquivo (self, arquivo):
        self.lista_arquivos.append (arquivo)
        
    def adicionar_diretorio (self, diretorio):
        self.lista_diretorios.append (diretorio)
    
    def mostrar_conteudo (self, nome):
        print (f"\n{nome}: ")
        for arquivo in self.lista_arquivos:
            print (f"Nome -> {arquivo.nome} || Data -> {arquivo.data} || Tamanho -> {arquivo.tamanho} || Tipo -> {arquivo.tipo}")
    
    def mostrar_conteudo_recursivo (self):
        for arquivo in self.lista_diretorios:
            print (f"Nome -> {arquivo.nome} || Data -> {arquivo.data} || Tamanho -> {arquivo.tamanho} || Tipo -> {arquivo.tipo}")
        
if __name__ == "__main__":
    arquivo1 = Arquivo (nome = "Harry Potter", data = "06/06/2025", tamanho = "10 KB", tipo = ".doc")
    arquivo2 = Arquivo (nome = "Um elefante em meu Jardim", data = "06/06/2025", tamanho = "100 KB", tipo = ".doc")
    arquivo3 = Arquivo (nome = "Rubi", data = "06/06/2025", tamanho = "150 KB", tipo = ".mp3")
    arquivo4 = Arquivo (nome = "Canto da Sereia", data = "06/06/2025", tamanho = "125 KB", tipo = ".mp3")
    arquivo5 = Arquivo (nome = "One Piece", data = "06/06/2025", tamanho = "∞ GB", tipo = ".pdf")  
    
    diretorio2 = Diretorio (nome = "Músicas")
    diretorio2.adicionar_arquivo (arquivo3)
    diretorio2.adicionar_arquivo (arquivo4)
    diretorio2.mostrar_conteudo (diretorio2.nome)
    
    diretorio3 = Diretorio (nome = "Mangás")
    diretorio3.adicionar_arquivo (arquivo5)
    diretorio3.mostrar_conteudo (diretorio3.nome)
    
    diretorio1 = Diretorio (nome = "Livros")
    diretorio1.adicionar_arquivo (arquivo1)
    diretorio1.adicionar_arquivo (arquivo2)
    diretorio1.adicionar_diretorio (diretorio3)
    diretorio1.mostrar_conteudo (diretorio1.nome)