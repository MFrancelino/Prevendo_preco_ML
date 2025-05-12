import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('pizzas.csv')

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("digite o tamanho do diametro da pizza")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f'o valor da pizza com o diametro de {diametro:.2f} centimetros é de ${preco_previsto:.2f}')
    st.image("https://sabores-new.s3.amazonaws.com/public/2024/11/pizza-de-frango-1.jpg")

