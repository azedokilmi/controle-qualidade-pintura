# 🎨 Controle de Qualidade da Pintura

Este projeto em Python foi desenvolvido para registrar, analisar e visualizar dados de **qualidade da pintura** em processos industriais, organizando os resultados por turnos (dia e noite). Além da entrada e remoção de dados, o sistema gera gráficos analíticos com destaques visuais como **picos, vales e limites de qualidade**, fornecendo uma ferramenta prática para o acompanhamento e melhoria contínua do processo.

---

## ⚙️ Como Funciona?

1. 📥 **Entrada e Edição de Dados**
   - Os dados são registrados manualmente pelo terminal no seguinte formato:
     ```
     DD/MM/AAAA, Veículo, Métrica
     ```
   - Também é possível **remover dados** digitando:
     ```
     remover DD/MM/AAAA, Veículo, Métrica
     ```
   - Os dados são salvos em dois arquivos de texto:
     - `DADOS_PINTURA_DIA.txt`
     - `DADOS_PINTURA_NOITE.txt`

2. 📊 **Geração de Gráficos**
   - Os gráficos mostram a **evolução da métrica de qualidade da pintura** ao longo do tempo.
   - Linhas horizontais indicam:
     - Limite inferior/superior de qualidade
     - Faixa ideal de qualidade
   - Destaques automáticos:
     - 📈 Pico (maior valor)
     - 📉 Vale (menor valor)
   - Inclui anotações técnicas sobre o processo de pintura.

3. 💾 **Exportação Automática**
   - Os gráficos são salvos automaticamente na **área de trabalho** com nomes como:
     ```
     PINTURA_DIA_15-04-2025.png
     PINTURA_NOITE_15-04-2025.png
     ```
   - Os arquivos `.txt` atualizados também são copiados para a área de trabalho.

---

## 🧪 Detalhes Técnicos

- 📌 O sistema considera métricas entre 0 e 130%.
- As anotações técnicas incluídas no gráfico:
  ```
  Utilização de 2 bicos de pintura (1,3mm - fundo e 1,8mm - tinta).
  Aplicação de 2 camadas de fundo e 2 camadas de tinta.
  Controle da viscosidade da tinta preta tornando-a mais espessa.
  Utilização de iluminação adicional fixa e portátil.
  ```

---

## 🚀 Como Executar

1. **Tenha o Python instalado (3.8+)**

2. **Instale as dependências**:

   ```bash
   pip install pandas matplotlib numpy
   ```

3. **Execute o script:**

   ```bash
   python controle_qualidade_pintura.py
   ```

   O terminal solicitará os dados de entrada, e ao final serão gerados os gráficos automaticamente.

---

## 💡 Melhorias Futuras

- Interface gráfica (GUI) para facilitar entrada de dados.
- Exportação em PDF dos relatórios.
- Dashboard interativo para análise de tendências.
- Integração com sistemas MES/ERP.

---

## ✍️ Autor

Feito com atenção aos detalhes por Pedro Cicilini de Nadai 🎯  
GitHub: [@azedokilmi](https://github.com/azedokilmi)
