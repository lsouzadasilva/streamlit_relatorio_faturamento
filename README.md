# 🛒 Supermarket Sales Dashboard 📊

Este projeto é um **Dashboard interativo** desenvolvido em **Streamlit** para análise de vendas de um supermercado, permitindo visualizar dados de faturamento, quantidade de produtos, formas de pagamento e distribuição percentual de vendas.

---

## 🌟 Funcionalidades

✅ Filtros interativos por **Período, Gênero, Tipo de Cliente e Filial (Branch)**  
✅ Gráficos dinâmicos com **Plotly Express**  
✅ Indicadores (cards) de **Investimento, Quantidade, Impostos e Faturamento Total**  
✅ Gráficos de **Barras, Pizza e Séries Temporais**  
✅ Visualização limpa e responsiva  
✅ Ocultação do menu padrão do Streamlit para foco total nos dados

---

## 🎯 Como usar

### 1. Clone o repositório

bash
git clone https://github.com/seu-usuario/supermarket-dashboard.git
cd supermarket-dashboard

# 2. Crie e ative um ambiente virtual (opcional)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
# 3. Instale as dependências
bash
Copy
Edit
pip install -r requirements.txt
# 4. Execute o projeto
bash
Copy
Edit
streamlit run app.py
# 🗂️ Estrutura do projeto
bash
Copy
Edit
├── app.py                      # Código principal do Dashboard
├── supermarket_sales.csv       # Base de dados com informações de vendas
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo
# 🚀 Como funciona
# 📄 Base de Dados
O projeto utiliza o arquivo supermarket_sales.csv, contendo dados reais simulados de vendas, como:

Data de compra

Gênero do cliente

Tipo de cliente

Filial (Branch)

Linha de produtos

Quantidade

Impostos e Total da compra

Forma de pagamento

# 🧩 Filtros
Você pode filtrar os dados por:

Período (mês/ano)

Gênero

Tipo de cliente (Membro ou Normal)

Filial (Branch A, B ou C)

# 📊 Visualizações
Indicadores principais → Mostram investimento, quantidade, imposto e faturamento total

Gráfico de barras → Faturamento e quantidade por linha de produto

Gráfico de pizza → Percentual de faturamento por produto

Gráficos de formas de pagamento → Distribuição e total de vendas

Gráfico temporal → Faturamento ao longo do tempo

# 🔥 Tecnologias utilizadas
Python

Streamlit (para a construção do dashboard)

Pandas (para manipulação de dados)

Plotly Express (para gráficos interativos)

# 👨‍💻 Desenvolvido por
Leandro Souza

# ⭐️ Licença
Uso livre para fins pessoais, acadêmicos ou profissionais.
Se quiser adaptar para outro segmento de vendas, é só trocar o arquivo CSV! 😉
