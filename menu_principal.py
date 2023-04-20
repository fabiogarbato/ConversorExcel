import tkinter as tk
from tkinter import messagebox

class MenuPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu Principal")
        self.root.geometry("400x300")  # Definir a geometria da janela principal

        # Criação de uma label de boas-vindas
        self.welcome_label = tk.Label(self.root, text="Conversor de Arquivos", font=("Helvetica", 16, "bold"))
        self.welcome_label.pack(pady=20)

        # Criação de um botão para abrir a tela de conversão
        self.button_conversor = tk.Button(self.root, text="Converter XLSX para CSV", command=self.abrir_gui)
        self.button_conversor.pack(pady=10)

        # Criação de um botão para sair do programa
        self.button_sair = tk.Button(self.root, text="Sair", command=self.sair)
        self.button_sair.pack(pady=10)

    # Função para abrir a tela de conversão
    def abrir_gui(self):
        from gui import Gui
        self.root.withdraw()  # Esconde a janela do Menu Principal
        self.gui = Gui()
        #self.root.deiconify()  # Torna a janela do Menu Principal visível novamente

    # Função para sair do programa
    def sair(self):
        self.root.destroy()

    def iniciar(self):
        self.root.mainloop()
