import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Criar a janela principal
root = tk.Tk()

# Configurar a janela
root.title("Conversor de XLSX para CSV")
root.geometry("400x200")

# Criar a label com o título em negrito
title_label = tk.Label(root, text="Conversor de XLSX para CSV", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Função para selecionar o arquivo XLSX
def select_file():
    xlsx_path = filedialog.askopenfilename(title="Selecione o arquivo XLSX", filetypes=[("Arquivos XLSX", "*.xlsx")])
    try:
        # Gerar o nome do arquivo CSV a partir do nome do arquivo XLSX
        csv_path = xlsx_path.replace('.xlsx', '.csv')
        
        if os.path.exists(csv_path):
            # Se o arquivo CSV já existir, pergunte ao usuário se ele deseja converter novamente
            answer = messagebox.askyesno("Arquivo já convertido", "O arquivo já foi convertido anteriormente. Deseja fazer novamente?")
            if not answer:
                return
        
        # Ler o arquivo XLSX
        df = pd.read_excel(xlsx_path)

        # Converter para CSV e salvar o arquivo
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')

        # Exibir mensagem de conclusão
        messagebox.showinfo("Conversão concluída", "O arquivo foi convertido para CSV com sucesso!")

    except FileNotFoundError:
        # Exibir mensagem de erro
        messagebox.showerror("Erro", "O caminho especificado não existe. Verifique se o caminho está correto e tente novamente.")

# Criar botão para selecionar o arquivo
select_button = tk.Button(root, text="Selecionar arquivo", command=select_file)
select_button.pack(pady=20)

# Iniciar a janela principal
root.mainloop()
