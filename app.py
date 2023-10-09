import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
import joblib

# model = joblib.load('filename.pkl')

df = pd.read_csv('https://raw.githubusercontent.com/nikitaely/linear_model_and_dev/main/df.csv')

threshold = st.select_slider(
    'Введите порог вероятности, начиная с которого модель будет относить объект к положительному классу',
    options=list(np.arange(0, 1, 0.05)))
st.write(f'accuracy: {accuracy_score(y_test, new_pred)}\nprecision: {precision_score(y_test, new_pred)}\nrecall {recall_score(y_test, new_pred)}\nf1: {f1_score(y_test, new_pred)}\n')

st.title('Разведочный анализ данных')

st.text('Конечный датафрейм')
st.dataframe(df.head())

fig, ax = plt.subplots()
st.text('Распределение личного дохода')
plt.boxplot(df['PERSONAL_INCOME'])
st.pyplot(fig)

fig, ax = plt.subplots()
st.text('Распределение возраста')
plt.boxplot(df['AGE'])
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))
sns.heatmap(df.corr(), annot=True)
st.text('Матрица корреляций')
st.pyplot(fig)


fig, ax = plt.subplots()
plt.bar(df['TARGET'], df['PERSONAL_INCOME'])
st.text('Зависимость целевой переменной от личного дохода')
st.pyplot(fig)

fig, ax = plt.subplots()
plt.bar(df['TARGET'], df['AGE'])
st.text('Зависимость целевой переменной от возраста')
st.pyplot(fig)

numbers = ['AGE', 'CHILD_TOTAL', 'DEPENDANTS', 'PERSONAL_INCOME', 'LOAN_NUM_TOTAL', 'LOAN_NUM_CLOSED']
categorical = ['GENDER', 'DEPENDANTS', 'SOCSTATUS_WORK_FL', 'SOCSTATUS_PENS_FL']

st.text('Характеристики числовых столбцов')
st.dataframe(df[numbers].describe())

st.text('Характеристики категориальных столбцов')
st.dataframe(df[categorical].astype('category').describe())
