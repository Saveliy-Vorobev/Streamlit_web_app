import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import datetime, date



st.write("""
# Аналитка акций компании Apple
Демонстрация цены **закрытия** и **объем** торгов акций AAPL
""")


with st.sidebar:
    start_date = st.date_input("Начальная дата", value=pd.to_datetime("2020-01-01"))
    end_date = st.date_input("Конечная дата", value=pd.to_datetime("2023-01-01"))



tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker

if start_date < end_date:
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

    # График цены закрытия
    st.write("## 📊 Цена закрытия")
    st.line_chart(tickerDf.Close)

    # График объема торгов
    st.write("## 📉 Объем торгов")
    st.line_chart(tickerDf.Volume)
else:
    st.error("Ошибка: Конечная дата должна быть больше начальной!")