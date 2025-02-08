import streamlit as st
import pandas as pd 
import plotly.express as px 

# Configuração pagina
st.set_page_config(layout="wide")
st.header("Visão Geral", divider=True)
st.sidebar.markdown("Filtros")

# Carregando os dados
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df = df.sort_values("Date")
df = df.drop(columns=["Unnamed: 0","Invoice ID"])
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Filtros
month = st.sidebar.multiselect("Mês", df["Month"].unique())
gender = st.sidebar.selectbox("Genero", df["Gender"].unique())
tipo_cliente = st.sidebar.selectbox("Tipo cliente", df["Customer type"].unique())
branch = st.sidebar.selectbox("Branch", df["Branch"].unique())
df_filter = df[(df["Month"].isin(month)) & (df["Gender"] == gender) & (df["Customer type"] == tipo_cliente) & (df["Branch"] == branch)]
st.sidebar.markdown("Desenvolvido por [Leandro Souza](https://br.linkedin.com/in/leandro-souza-313136190)")


# cards
quantidade = df_filter["Quantity"].sum()
cogs = df_filter["cogs"].sum()
total = df_filter["Total"].sum()
tax = df_filter["Tax 5%"].sum()

col1, col2, col3, col4 = st.columns(4)
tile = col1.container(height=150)
tile.title(f'Investimento \nR$ {cogs}')
tile = col2.container(height=150)
tile.title(f'Quantidade\n{quantidade}')
tile = col3.container(height=150)
tile.title(f'Tax 5% \nR$ {tax}')
tile = col4.container(height=150)
tile.title(f'Total \nR$ {total}')
st.dataframe(df_filter, use_container_width=True)

col1_1, col2_2 = st.columns(2)


total_2 = df_filter.groupby("Product line")[["Quantity","Unit price", "cogs","Tax 5%", "Total", "gross margin percentage"]].sum().reset_index()
total_2 = total_2.sort_values("Total")

grafico_1 = px.bar(total_2, x="Product line", y=["Total","Quantity"], text_auto=True ,title="FATURAMENTO E QUANTIDAE POR PRODUTO", color="Product line")
col1_1.plotly_chart(grafico_1, use_container_width=True)

grafico_2 = px.pie(total_2, values="Total", names="Product line", title="PERCENTUAL POR PRODUTO",hole=0.5, color="Product line")
col2_2.plotly_chart(grafico_2, use_container_width=True)

st.divider()

col3, col4 = st.columns(2)

pagamento = df_filter.groupby("Payment")[["Quantity","Unit price", "cogs","Tax 5%", "Total", "gross margin percentage"]].sum().reset_index()
pagamento = pagamento.sort_values("Total")

grafico_3 = px.pie(pagamento, values="Total", names="Payment", hole=0.5, title="DISTRIBUIÇÃO POR FORMA DE PAGAMENTO %", 
color="Payment", color_discrete_map={"Cash":"#FF2B2B", "Ewallet":"#0068C9", "Credit card":"#83C9FF"})
col3.plotly_chart(grafico_3, use_container_width=True)

grafico_4 = px.bar(pagamento, x="Payment", y="Total", title="FATURAMENTO POR FORMA DE PAGAMENTO", color="Payment", 
color_discrete_map={"Cash":"#FF2B2B", "Ewallet":"#0068C9", "Credit card":"#83C9FF"}, text_auto=True)
col4.plotly_chart(grafico_4, use_container_width=True)

st.divider()

col5, = st.columns(1)
total_1 = df_filter.groupby("Date")[["Quantity","Unit price", "cogs","Tax 5%", "Total", "gross margin percentage"]].sum().reset_index()
total_1 = total_1.sort_values("Date")

grafico_5 = px.bar(total_1, x="Date", y="Total", text_auto=True, title="FATURAMENTO POR PERIDO")
grafico_5.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
col5.plotly_chart(grafico_5, use_container_width=True)

