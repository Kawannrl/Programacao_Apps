import tkinter as tk
from mini_sims import Personagem

class SimsApp:
    def __init__ (self, root):
        # Criando o personagem
        self.personagem = Personagem ("Detona Prato")

        # Ttulo da Janela
        root.title ("Mini Sims")
        # Tamanho da Janela
        root.geometry ("500x500")

        self.label_status = tk.Label (root, text = self.personagem.mostrar_status (), font = ("Arial", 15), pady = 10)
        self.label_status.pack ()

        self.btn_comer = tk.Button (root, text = "🍽 Comer", command = self.acao_botao_comer)
        self.btn_comer.pack (pady = 5)

        self.btn_dormir = tk.Button (root, text = "💤 Dormir", command = self.acao_botao_dormir)
        self.btn_dormir.pack (pady = 5)

        self.btn_trabalhar = tk.Button (root, text = "💼 Trabalhar", command = self.acao_botao_trabalhar)
        self.btn_trabalhar.pack (pady = 5)
        
        self.btn_tomar_banho = tk.Button (root, text = "🚿 Tomar Banho", command = self.acao_botao_tomar_banho)
        self.btn_tomar_banho.pack (pady = 5)

        self.label_mensagem = tk.Label (root, text = "", font = ("Arial", 10))
        self.label_mensagem.pack ()

    def atualizar_status (self):
        self.label_status.config (text = self.personagem.mostrar_status ())

    def acao_botao_comer (self):
        mensagem = self.personagem.comer ()
        self.label_mensagem.config (text = mensagem)
        self.atualizar_status ()
    
    def acao_botao_dormir (self):
        mensagem = self.personagem.dormir ()
        self.label_mensagem.config (text = mensagem)
        self.atualizar_status ()

    def acao_botao_trabalhar (self):
        mensagem = self.personagem.trabalhar ()
        self.label_mensagem.config (text = mensagem)
        self.atualizar_status ()
        
    def acao_botao_tomar_banho (self):
        mensagem = self.personagem.tomar_banho ()
        self.label_mensagem.config (text = mensagem)
        self.atualizar_status ()

if __name__ == "__main__":
    root = tk.Tk ()
    app = SimsApp (root)
    root.mainloop ()