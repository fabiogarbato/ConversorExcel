import pandas as pd
import os

def converter_xlsx_para_csv(xlsx_path):
    try:
        # Gerar o nome do arquivo CSV a partir do nome do arquivo XLSX
        csv_path = xlsx_path.replace('.xlsx', '.csv')
        
        if os.path.exists(csv_path):
            # Se o arquivo CSV já existir, pergunte ao usuário se ele deseja converter novamente
            answer = input("O arquivo já foi convertido anteriormente. Deseja fazer novamente? (S/N) ")
            if answer.lower() != 's':
                return False
        
        # Ler o arquivo XLSX
        df = pd.read_excel(xlsx_path)

        # Converter para CSV e salvar o arquivo
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')

        return True

    except FileNotFoundError:
        print("O caminho especificado não existe. Verifique se o caminho está correto e tente novamente.")
        return False
