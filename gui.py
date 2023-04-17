import tkinter as tk
from tkinter import filedialog, messagebox
from conversor import converter_xlsx_para_csv

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
    if xlsx_path:
        if converter_xlsx_para_csv(xlsx_path):
            # Exibir mensagem de conclusão
            messagebox.showinfo("Conversão concluída", "O arquivo foi convertido para CSV com sucesso!")

# Criar botão para selecionar o arquivo
select_button = tk.Button(root, text="Selecionar arquivo", command=select_file)
select_button.pack(pady=20)

# Iniciar a janela principal
root.mainloop()
