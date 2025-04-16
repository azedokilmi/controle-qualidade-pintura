import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Diretório onde os arquivos estão localizados
diretorio = r'C:\Users\pcicilini.CORP\PROGRAMAS EM PYTHON\PINTURA'

# Arquivo de dados do dia
arquivo_nome_dia = 'DADOS_PINTURA_DIA.txt'
caminho_completo_dia = os.path.join(diretorio, arquivo_nome_dia)

# Arquivo de dados da noite
arquivo_nome_noite = 'DADOS_PINTURA_NOITE.txt'
caminho_completo_noite = os.path.join(diretorio, arquivo_nome_noite)

# Diretório da área de trabalho para salvar as cópias dos arquivos TXT
desktop_diretorio = os.path.join(os.path.expanduser("~"), 'Desktop')

# Arquivos de destino na área de trabalho
arquivo_nome_desktop_dia = 'DADOS_PINTURA_DIA.txt'
arquivo_nome_desktop_noite = 'DADOS_PINTURA_NOITE.txt'
caminho_completo_desktop_dia = os.path.join(desktop_diretorio, arquivo_nome_desktop_dia)
caminho_completo_desktop_noite = os.path.join(desktop_diretorio, arquivo_nome_desktop_noite)

def adicionar_ou_apagar_dados(caminho_arquivo, periodo):
    print(f"\nDigite os dados do período {periodo} no formato: 'DD/MM/AAAA, Veículo, Métrica'")
    print("Pressione ENTER sem digitar nada para mudar o período ou finalizar o programa.")
    print("Se deseja apagar os dados digite 'remover' seguido de 'DD/MM/AAAA, Veículo, Métrica'.")

    # Ler os dados existentes no arquivo
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    while True:
        entrada = input(f"Dados ({periodo}): ").strip()

        if entrada == "":
            # Finaliza a entrada de dados ou muda o período
            return False

        try:
            # Verificar se a entrada corresponde a dados a excluir
            if ',' in entrada:
                # Verificar se é para adicionar ou excluir
                if entrada.lower().startswith("remover "):  # Se começar com 'remover', será exclusão
                    dados_remover = entrada[8:].strip()  # Remove a palavra 'remover ' da entrada
                    if dados_remover + '\n' in linhas:
                        linhas.remove(dados_remover + '\n')
                        print(f"Dado '{dados_remover}' removido com sucesso.")
                        # Reescrever o arquivo com as linhas atualizadas
                        with open(caminho_arquivo, 'w') as arquivo:
                            arquivo.writelines(linhas)
                    else:
                        print(f"Dados '{dados_remover}' não encontrados no arquivo.")
                else:
                    # Adicionar os dados ao arquivo (apenas se válido)
                    data, veiculo, metrica = entrada.split(',')
                    datetime.strptime(data.strip(), '%d/%m/%Y')  # Valida a data
                    float(metrica.strip())  # Valida a métrica como número
                    linhas.append(entrada.strip() + '\n')
                    print("Dados adicionados com sucesso.")
                    # Reescrever o arquivo com os dados adicionados
                    with open(caminho_arquivo, 'w') as arquivo:
                        arquivo.writelines(linhas)
            else:
                print("Erro: Formato inválido. Use o formato: 'DD/MM/AAAA, Veículo, Métrica' para adicionar ou 'Remover DD/MM/AAAA, Veículo, Métrica' para excluir.")

        except ValueError:
            print("Erro: Formato inválido. Use o formato: 'DD/MM/AAAA, Veículo, Métrica'.")

    print("Operação finalizada.")

# Função principal para processar os períodos
def processar_dados():
    print("\n--- Entrada de Dados de Pintura ---")
    periodo = "DIA"
    mudar_periodo = False

    while True:
        caminho_arquivo = (
            caminho_completo_dia if periodo == "DIA" else caminho_completo_noite
        )

        mudar_periodo = mudar_periodo = adicionar_ou_apagar_dados(caminho_arquivo, periodo)
        if not mudar_periodo:
            if periodo == "DIA":
                print("\nMudando para o período NOITE.")
                periodo = "NOITE"
            else:
                print("\nFinalizando o programa.")
                break

# Executar o programa
if __name__ == "__main__":
    processar_dados()

# Função para ler os dados de um arquivo TXT e gerar o gráfico
def gerar_grafico(caminho_arquivo, caminho_imagem, periodo):
    dados = []

    try:
        # Ler os dados do arquivo
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                data, produto, metrica = linha.strip().split(',')
                dados.append({
                    'Data': data,
                    'Produto': produto,
                    'Metrica': float(metrica)
                })

        # Verificar se o arquivo original precisa ser atualizado na área de trabalho
        caminho_destino = (
            caminho_completo_desktop_dia if periodo == 'dia' else caminho_completo_desktop_noite
        )

        if not os.path.exists(caminho_destino) or open(caminho_destino, 'r').read() != open(caminho_arquivo, 'r').read():
            # Copiar o conteúdo do arquivo original para o novo arquivo na área de trabalho
            with open(caminho_arquivo, 'r') as arquivo_origem:
                conteudo = arquivo_origem.read()

            # Salvar o arquivo na área de trabalho
            with open(caminho_destino, 'w') as arquivo_destino:
                arquivo_destino.write(conteudo)
            print(f"O arquivo de dados foi salvo na área de trabalho como '{os.path.basename(caminho_destino)}'.")

        # Criar um DataFrame do Pandas
        df = pd.DataFrame(dados)

        if not df.empty:
            # Converter a coluna 'Data' para o formato de data e formatar como DIA-MÊS-ANO
            df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
            df.sort_values(by='Data', inplace=True)

            # Criar o gráfico
            fig, ax = plt.subplots(figsize=(15, 10))  # Tamanho da figura em polegadas

            # Definir o fundo da figura como cinza
            fig.patch.set_facecolor('lightgray')
            ax.set_facecolor('lightgray')

            cores = plt.cm.tab10(np.linspace(0, 1, df['Produto'].nunique()))

            for i, produto in enumerate(df['Produto'].unique()):
                dados_produto = df[df['Produto'] == produto]
                ax.plot(dados_produto['Data'], dados_produto['Metrica'], label=produto, color=cores[i], marker='o', linewidth=2)

            ax.set_xlabel('Data', fontsize=14)
            ax.set_ylabel('Métrica de Qualidade', fontsize=14)
            ax.set_title(f'Evolução da Qualidade de Pintura - {periodo.capitalize()}', fontsize=18, fontweight='bold')
            ax.grid(True, which='both', linestyle='--', linewidth=0.6, color='gray')

            # Adicionar as linhas de limite de qualidade
            ax.axhline(y=70, color='red', linestyle='--', linewidth=1.5, label='Limite Inferior')
            ax.axhline(y=90, color='red', linestyle='--', linewidth=1.5, label='Limite Superior')
            ax.axhline(y=75, color='green', linestyle='--', linewidth=1.5, label='Qualidade Perfeita (Min)')
            ax.axhline(y=85, color='green', linestyle='--', linewidth=1.5, label='Qualidade Perfeita (Max)')

            ax.legend(title='Produto', fontsize=12, title_fontsize='13', loc='upper left')
            ax.tick_params(axis='x', rotation=45)

            # Definir o eixo Y para ser simétrico de 30 a 130
            ax.set_ylim(30, 130)

            # Encontrar o pico e o vale
            pico = df['Metrica'].idxmax()  # Índice do maior valor
            vale = df['Metrica'].idxmin()  # Índice do menor valor

            # Adicionar as anotações de pico e vale com setas
            ax.annotate(f"Pico: {df.loc[pico, 'Metrica']:.2f}%", 
                        xy=(df.loc[pico, 'Data'], df.loc[pico, 'Metrica']), 
                        xytext=(10, 20), textcoords="offset points", 
                        arrowprops=dict(arrowstyle="->"), color="purple")

            ax.annotate(f"Vale: {df.loc[vale, 'Metrica']:.2f}%", 
                        xy=(df.loc[vale, 'Data'], df.loc[vale, 'Metrica']), 
                        xytext=(-50, -30), textcoords="offset points",  # Deslocado para cima
                        arrowprops=dict(arrowstyle="->"), color="brown")

            # Texto informativo sobre o processo de pintura
            informativo = """
            Utilização de 2 bicos de pintura (1,3mm - fundo e 1,8mm - tinta).
            Aplicação de 2 camadas de fundo e 2 camadas de tinta.
            Controle da viscosidade da tinta preta tornando-a mais espessa.
            Utilização de iluminação adicional fixa e portátil.
            """

            # Adicionar o texto informativo no gráfico
            ax.text(0.5, 0.95, informativo, ha='center', va='top', transform=ax.transAxes, fontsize=10, color='black', 
                    bbox=dict(facecolor='white', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.5'))

            if not os.path.exists(os.path.dirname(caminho_imagem)):
                os.makedirs(os.path.dirname(caminho_imagem))

            # Salvar o gráfico com fundo cinza e qualidade alta
            plt.savefig(caminho_imagem, dpi=600, bbox_inches='tight', facecolor='lightgray')
            plt.show()

    except FileNotFoundError:
        print(f"Erro: O arquivo '{os.path.basename(caminho_arquivo)}' não foi encontrado no diretório '{diretorio}'.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

# Definir o nome do arquivo com a data de hoje
data_hoje = datetime.today().strftime('%d-%m-%Y')

# Caminho para salvar os gráficos
caminho_imagem_dia = os.path.join(desktop_diretorio, f'PINTURA_DIA_{data_hoje}.png')
caminho_imagem_noite = os.path.join(desktop_diretorio, f'PINTURA_NOITE_{data_hoje}.png')

# Gerar gráficos para o dia e noite
gerar_grafico(caminho_completo_dia, caminho_imagem_dia, 'dia')
gerar_grafico(caminho_completo_noite, caminho_imagem_noite, 'noite')