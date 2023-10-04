import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\nikel\OneDrive\Рабочий стол\data\df.csv')

st.title('Разведочный анализ данных')

st.text('Конечный датафрейм')
st.dataframe(df.head())



fig, ax = plt.subplots()

st.text('Распределение личного дохода')
plt.boxplot(df['PERSONAL_INCOME'])

fig

fig, ax = plt.subplots()

st.text('Распределение возраста')
plt.boxplot(df['AGE'])

fig



fig, ax = plt.subplots(figsize=(16, 8))

sns.heatmap(df.corr(), annot=True)

plt.show()
st.text('Матрица корреляций')

fig


fig, ax = plt.subplots(figsize=(16, 8))

plt.bar(df['TARGET'], df['PERSONAL_INCOME'])

plt.show()
st.text('Зависимость целевой переменной от личного дохода')

fig


fig, ax = plt.subplots(figsize=(16, 8))

plt.bar(df['TARGET'], df['AGE'])

plt.show()
st.text('Зависимость целевой переменной от возраста')

fig
