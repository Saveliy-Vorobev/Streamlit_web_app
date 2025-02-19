import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(
    page_title="Multipage App",
)


st.title("Это главная страница")
st.write("#### Справа в колонке вы можете выбрать необходимую страницу для просмотра")
st.sidebar.success("Выбери страницу")


