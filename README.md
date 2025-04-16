# 🎨 Controle de Qualidade da Pintura

Este projeto tem como objetivo analisar e monitorar a qualidade da pintura automotiva ao longo do tempo, com base em dados históricos e critérios técnicos de avaliação. Através da geração de gráficos e métricas, é possível identificar padrões de desempenho, desvios e oportunidades de melhoria nos turnos de produção.

---

## ⚙️ Como Funciona?

1. ## 🧠 Funcionalidades

- Leitura e processamento de dados históricos de pintura.
- Geração automática de gráficos com limites de controle e faixas de qualidade perfeita.
- Análise individual por turno (dia e noite).
- Destaque visual para picos e vales de qualidade.
- Anotações explicativas com intervenções técnicas realizadas.
- Exportação de gráficos com alta resolução em PNG.

2. 📥 **Entrada e Edição de Dados**
   - Os dados são registrados manualmente pelo terminal no seguinte formato:
     
     ```
     DD/MM/AAAA, Veículo, Métrica
     ```
   - Também é possível **remover dados** digitando:
     
     ```
     remover DD/MM/AAAA, Veículo, Métrica
     ```
   - Os dados são salvos em dois arquivos de texto:
     - `DADOS_PINTURA_DIA.txt` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/controle-qualidade-pintura/blob/main/DADOS-PINTURA-DIA.txt))
     - `DADOS_PINTURA_NOITE.txt` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/controle-qualidade-pintura/blob/main/DADOS-PINTURA-NOITE.txt))
       
     - Os arquivos `.txt` atualizados são copiados para a área de trabalho.

3. 📊 **Geração de Gráficos**
   - Os gráficos mostram a **evolução da métrica de qualidade da pintura** ao longo do tempo.
   - Linhas horizontais indicam:
     - Limite inferior/superior de qualidade
     - Faixa ideal de qualidade
   - Destaques automáticos:
     - 📈 Pico (maior valor)
     - 📉 Vale (menor valor)
       
   - Inclui anotações técnicas sobre o processo de pintura.

4. 💾 **Exportação Automática**
   - Os gráficos são salvos automaticamente na **área de trabalho** com nomes como (data baseada na atual):
     
     - `PINTURA_DIA_31-03-2025.png` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/controle-qualidade-pintura/blob/main/PINTURA-DIA-31-03-2025.png))
     - 
     - `PINTURA_NOITE_31-03-2025.png` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/controle-qualidade-pintura/blob/main/PINTURA-NOITE-31-03-2025.png))
     
---

## 🧪 Detalhes Técnicos

- 📌 O sistema considera métricas entre 0 e 130%.
- A **métrica de qualidade** é obtida por meio de um **equipamento de ultrassom** que mede a **espessura da camada de tinta** em **micrômetros**. Essa métrica indica se a tinta aplicada está:
  - Muito fina (valores baixos)
  - Muito grossa (valores altos)
  - Ideal (próximo de **80 microns**, considerado o valor perfeito)

- As anotações técnicas incluídas no gráfico:
  ```
  Utilização de 2 bicos de pintura (1,3mm - fundo e 1,8mm - tinta).
  Aplicação de 2 camadas de fundo e 2 camadas de tinta.
  Controle da viscosidade da tinta preta tornando-a mais espessa.
  Utilização de iluminação adicional fixa e portátil.
  ```
  
---

## 🚀 Passo a Passo da Execução

### 📁 Preparar os Arquivos

⚠️ Ambos os arquivos devem estar na área de trabalho:

#### `DADOS_PINTURA_DIA.txt` e `DADOS_PINTURA_NOITE.txt`
- Arquivos onde os dados são armazenados e atualizados.
- O script irá gerar e atualizar automaticamente conforme as entradas.

![Prévia dos Dados do Dia e Noite](https://github.com/azedokilmi/controle-qualidade-pintura/blob/main/preview-dados.png)

#### `PINTURA-DIA-E-NOITE.py`
- Script principal do projeto que deve estar na mesma pasta (preferencialmente na área de trabalho).

![Prévia do Script](https://github.com/azedokilmi/controle-qualidade-pintura/blob/main/preview-script.png)

### ▶️ Rodar o Programa

1. **Tenha o Python instalado**  
Recomendado: Python 3.8+

2. **Instale as dependências do projeto:**

   No terminal (ou prompt de comando), execute o comando:

   ```bash
   pip install pandas matplotlib numpy
   ```

3. **Execute o programa:**

   No terminal (ou prompt de comando), navegue até a área de trabalho onde o arquivo `.py` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/controle-qualidade-pintura/blob/main/PINTURA-DIA-E-NOITE.py)) deve estar localizado e execute o comando abaixo:

   ```bash
   python PINTURA-DIA-E-NOITE.py
   ```
   Após a execução do script, os arquivos de saída serão gerados na mesma pasta onde o programa foi executado.

4. **Entrada de Dados:**

   O terminal solicitará que você insira ou remova dados com base no padrão:
   ```
   DD/MM/AAAA, Veículo, Métrica
   remover DD/MM/AAAA, Veículo, Métrica
   ```

   Após a inserção ou remoção, os dados serão atualizados nos arquivos `.txt` e os gráficos serão gerados automaticamente.

   ![Prévia dos Gráficos Diurno e Noturno](https://github.com/azedokilmi/controle-qualidade-pintura/blob/main/preview-graficos.png)

### 🖱️ Executável OneFile (.exe)

Para facilitar o uso diário e tornar o processo mais prático, pode-se gerar um executável "onefile" (.exe) que pode ser rodado diretamente com dois cliques, sem a necessidade de abrir o prompt de comando ou editores de código.

📂 O arquivo `.exe`, quando gerado, pode ser colocado na área de trabalho do Windows e executado normalmente como se fosse o script `.py`.

---

## 💡 Melhorias Futuras

- Interface gráfica (GUI) para facilitar entrada de dados.
- Exportação em PDF dos relatórios.
- Dashboard interativo para análise de tendências.
- Integração com sistemas MES/ERP.

---

## ✍️ Autor

Feito com dedicação por Pedro Cicilini de Nadai 💪\
GitHub: [@azedokilmi](https://github.com/azedokilmi)
