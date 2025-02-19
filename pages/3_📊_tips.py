import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Аналитика DataFrame - 'tips'")


uploaded_file = st.sidebar.file_uploader('Загрузи CSV файл', type='csv')
if uploaded_file is not None:
    tips = pd.read_csv(uploaded_file)
    st.write("Данные из файла:")
    st.dataframe(tips)  # Отображение DataFrame

else:
    st.stop()



st.subheader("График зависимости размера чаевых от дня недели и пола")
order = ['Thur', 'Fri', 'Sat', 'Sun']
tips["day"] = pd.Categorical(tips["day"], categories=order, ordered=True)
plt.figure(figsize=(12,6))
sns.scatterplot(data=tips, x="tip", y="day", hue="sex", palette="coolwarm", alpha=0.7)
plt.title("Зависимость: размер чаевых от дня недели")
plt.xlabel("Размер чаевых")
plt.ylabel("День недели")
plt.grid()

plt.savefig('tips_week.png', dpi=400)
st.pyplot()



st.subheader("График распределения суммы счета от времени суток и пола")
sns.displot(data=tips, x='total_bill', kind='hist', kde=True, hue="time", multiple='stack', col="time", row="sex", facet_kws={'despine': False})
plt.grid(linestyle='--', alpha=0.5)
plt.savefig('total_bill_time_sex.png', dpi=400)
plt.tight_layout()
st.pyplot()


with open("tips_week.png", "rb") as file:
    btn = st.sidebar.download_button(
        label="График зависимости размера чаевых от дня недели и пола",
        data=file,
        file_name="tips_week.png",
        mime="image/png")


with open("total_bill_time_sex.png", "rb") as file:
    btn = st.sidebar.download_button(
        label="График распределения суммы счета от времени суток и пола",
        data=file,
        file_name="total_bill_time_sex.png",
        mime="image/png")