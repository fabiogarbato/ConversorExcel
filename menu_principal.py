import tkinter as tk
from tkinter import messagebox

class MenuPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu Principal")
        self.root.geometry("400x300")  # Definir a geometria da janela principal
        self.root.configure(background="#ADD8E6")  # Definir a cor de fundo

        # Criação de uma label de boas-vindas
        self.welcome_label = tk.Label(self.root, text="Conversor de Arquivos", font=("Helvetica", 16, "bold"), bg="#ADD8E6")
        self.welcome_label.pack(pady=20)

        # Criação de um botão para abrir a tela de conversão
        self.button_conversor = tk.Button(self.root, text="Converter XLSX para CSV", command=self.abrir_gui, borderwidth=5, relief="ridge", padx=10, pady=5, bd=2, bg="White", fg="black", font=("Helvetica", 12), activebackground="#5dade2")
        self.button_conversor.pack(pady=10)

        # Criação de um botão para sair do programa
        self.button_sair = tk.Button(self.root, text="Sair", command=self.sair, borderwidth=5, relief="ridge", padx=10, pady=5, bd=2, bg="White", fg="black", font=("Helvetica", 12), activebackground="#5dade2")
        self.button_sair.pack(pady=10)

        # Criação da label de copyright
        self.copyight_label = tk.Label(self.root, text="Copyright © Fabio Garbato", font=("Helvetica", 8, "bold"), bg="#ADD8E6")
        self.copyight_label.pack(side="bottom", anchor="se")


    # Função para abrir a tela de conversão
    def abrir_gui(self):
        from gui import Gui
        self.root.withdraw()  # Esconde a janela do Menu Principal
        self.gui = Gui()

    # Função para sair do programa
    def sair(self):
        self.root.quit()

    def iniciar(self):
        self.root.mainloop()
