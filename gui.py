import tkinter as tk
from tkinter import filedialog, messagebox
from conversor import converter_xlsx_para_csv
from menu_principal import MenuPrincipal

class Gui:
    def __init__(self):
        # Criar a janela principal
        self.root = tk.Tk()

        # Configurar a janela
        self.root.title("Conversor de XLSX para CSV")
        self.root.geometry("400x200")
        self.root.configure(background="#ADD8E6")

        # Criar a label com o título em negrito
        self.title_label = tk.Label(self.root, text="Conversor de XLSX para CSV", font=("Helvetica", 16, "bold"), bg="#ADD8E6")
        self.title_label.pack(pady=10)

        # Criar botão para selecionar o arquivo
        self.select_button = tk.Button(self.root, text="Selecionar arquivo", command=self.select_file, borderwidth=5, relief="ridge", padx=10, pady=5, bd=2, bg="White", fg="black", font=("Helvetica", 12), activebackground="#5dade2")
        self.select_button.pack(pady=20)

        # Criar botão para voltar para o menu principal
        self.menu_button = tk.Button(self.root, text="Voltar para o menu principal", command=self.voltar_menu, borderwidth=5, relief="ridge", padx=10, pady=5, bd=2, bg="White", fg="black", font=("Helvetica", 12), activebackground="#5dade2")
        self.menu_button.pack(pady=10)

    # Função para selecionar o arquivo XLSX
    def select_file(self):
        xlsx_path = filedialog.askopenfilename(title="Selecione o arquivo XLSX", filetypes=[("Arquivos XLSX", "*.xlsx")])
        if xlsx_path:
            if converter_xlsx_para_csv(xlsx_path):
                # Exibir mensagem de conclusão
                messagebox.showinfo("Conversão concluída", "O arquivo foi convertido para CSV com sucesso!")

    def iniciar(self):
        # Iniciar a janela principal
        self.root.mainloop()
    
    # Função para abrir a tela de conversão
    def voltar_menu(self):
        self.root.withdraw()
        self.menu_principal = MenuPrincipal()
