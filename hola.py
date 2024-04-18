import streamlit as st
import pandas as pd 

st.title('Mi primera App')

st.header('Demo App')

st.write('Demo de sitio con gráficas')

titanic_link='titanic(1).csv'
titanic_data=pd.read_csv(titanic_link)
st.dataframe(titanic_data)