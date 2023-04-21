import tkinter as tk
from tkinter import messagebox

class MenuPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu Principal")

        # Definir a largura e altura da janela
        largura = 400
        altura = 300

        # Obter a largura e altura da tela
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        # Calcular a posição x e y da janela para centralizá-la na tela
        x = (largura_tela / 2) - (largura / 2)
        y = (altura_tela / 2) - (altura / 2)

        # Definir a posição da janela
        self.root.geometry("%dx%d+%d+%d" % (largura, altura, x, y))
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

        # Criação da label de exibição da hora
        self.hora_label = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"), bg="#ADD8E6")
        self.hora_label.place(relx=0.0, rely=1.0, anchor="sw", y=0)
        self.atualizar_hora()  # Atualiza a hora na label

    def abrir_gui(self):
        from gui import Gui
        self.root.withdraw()  # Esconde a janela do Menu Principal
        self.gui = Gui()
    
    def sair(self):
        self.root.quit()

    def iniciar(self):
        self.root.mainloop()

    def atualizar_hora(self):
        from datetime import datetime
        agora = datetime.now().strftime("%H:%M:%S")
        self.hora_label.config(text=agora)
        self.root.after(1000, self.atualizar_hora)

