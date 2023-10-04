#!/usr/bin/env python
# coding: utf-8

# # Практическая работа

# # Задача

# Один из способов повысить эффективность взаимодействия банка с клиентами — отправлять предложение о новой услуге не всем клиентам, а только некоторым, которые выбираются по принципу наибольшей склонности к отклику на это предложение.
# 
# Задача заключается в том, чтобы предложить алгоритм, который будет выдавать склонность клиента к положительному или отрицательному отклику на предложение банка. Предполагается, что, получив такие оценки для некоторого множества клиентов, банк обратится с предложением только к тем, от кого ожидается положительный отклик.

# Для решения этой задачи загрузите файлы из базы в Postgres.
# Эта БД хранит информацию о клиентах банка и их персональные данные, такие как пол, количество детей и другие.
# 
# Описание таблиц с данными представлено ниже.

# **D_work**
# 
# Описание статусов относительно работы:
# - ID — идентификатор социального статуса клиента относительно работы;
# - COMMENT — расшифровка статуса.
# 
# 
# **D_pens**
# 
# Описание статусов относительно пенсии:
# - ID — идентификатор социального статуса;
# - COMMENT — расшифровка статуса.
# 
# 
# **D_clients**
# 
# Описание данных клиентов:
# - ID — идентификатор записи;
# - AGE	— возраст клиента;
# - GENDER — пол клиента (1 — мужчина, 0 — женщина);
# - EDUCATION — образование;
# - MARITAL_STATUS — семейное положение;
# - CHILD_TOTAL	— количество детей клиента;
# - DEPENDANTS — количество иждивенцев клиента;
# - SOCSTATUS_WORK_FL	— социальный статус клиента относительно работы (1 — работает, 0 — не работает);
# - SOCSTATUS_PENS_FL	— социальный статус клиента относительно пенсии (1 — пенсионер, 0 — не пенсионер);
# - REG_ADDRESS_PROVINCE — область регистрации клиента;
# - FACT_ADDRESS_PROVINCE — область фактического пребывания клиента;
# - POSTAL_ADDRESS_PROVINCE — почтовый адрес области;
# - FL_PRESENCE_FL — наличие в собственности квартиры (1 — есть, 0 — нет);
# - OWN_AUTO — количество автомобилей в собственности.
# 
# 
# **D_agreement**
# 
# Таблица с зафиксированными откликами клиентов на предложения банка:
# - AGREEMENT_RK — уникальный идентификатор объекта в выборке;
# - ID_CLIENT — идентификатор клиента;
# - TARGET — целевая переменная: отклик на маркетинговую кампанию (1 — отклик был зарегистрирован, 0 — отклика не было).
#     
#     
# **D_job**
# 
# Описание информации о работе клиентов:
# - GEN_INDUSTRY — отрасль работы клиента;
# - GEN_TITLE — должность;
# - JOB_DIR — направление деятельности внутри компании;
# - WORK_TIME — время работы на текущем месте (в месяцах);
# - ID_CLIENT — идентификатор клиента.
# 
# 
# **D_salary**
# 
# Описание информации о заработной плате клиентов:
# - ID_CLIENT — идентификатор клиента;
# - FAMILY_INCOME — семейный доход (несколько категорий);
# - PERSONAL_INCOME — личный доход клиента (в рублях).
# 
# 
# **D_last_credit**
# 
# Информация о последнем займе клиента:
# - ID_CLIENT — идентификатор клиента;
# - CREDIT — сумма последнего кредита клиента (в рублях);
# - TERM — срок кредита;
# - FST_PAYMENT — первоначальный взнос (в рублях).
# 
# 
# **D_loan**
# 
# Информация о кредитной истории клиента:
# - ID_CLIENT — идентификатор клиента;
# - ID_LOAN — идентификатор кредита.
# 
# **D_close_loan**
# 
# Информация о статусах кредита (ссуд):
# - ID_LOAN — идентификатор кредита;
# - CLOSED_FL — текущий статус кредита (1 — закрыт, 0 — не закрыт).

# *Ниже* представлен минимальный список колонок, которые должны находиться в итоговом датасете после склейки и агрегации данных. По своему усмотрению вы можете добавить дополнительные к этим колонки.

#     - AGREEMENT_RK — уникальный идентификатор объекта в выборке;
#     - TARGET — целевая переменная: отклик на маркетинговую кампанию (1 — отклик был зарегистрирован, 0 — отклика не было);
#     - AGE — возраст клиента;
#     - SOCSTATUS_WORK_FL — социальный статус клиента относительно работы (1 — работает, 0 — не работает);
#     - SOCSTATUS_PENS_FL — социальный статус клиента относительно пенсии (1 — пенсионер, 0 — не пенсионер);
#     - GENDER — пол клиента (1 — мужчина, 0 — женщина);
#     - CHILD_TOTAL — количество детей клиента;
#     - DEPENDANTS — количество иждивенцев клиента;
#     - PERSONAL_INCOME — личный доход клиента (в рублях);
#     - LOAN_NUM_TOTAL — количество ссуд клиента;
#     - LOAN_NUM_CLOSED — количество погашенных ссуд клиента.

# Будьте внимательны при сборке датасета: это реальные банковские данные, в которых могут наблюдаться дубли, некорректно заполненные значения или значения, противоречащие друг другу. Для получения качественной модели необходимо предварительно очистить датасет от такой информации.

# ## Задание 1
# 
# Соберите всю информацию о клиентах в одну таблицу, где одна строчка соответствует полной информации об одном клиенте.

# In[2]:


import pandas as pd


# In[3]:


PATH = r'C:\Users\nikel\OneDrive\Рабочий стол\data\\'

D_clients = pd.read_csv(PATH + 'D_clients.csv', sep=',')
D_job = pd.read_csv(PATH + 'D_job.csv')
D_salary = pd.read_csv(PATH + 'D_salary.csv')
D_last_credit = pd.read_csv(PATH + 'D_last_credit.csv')
D_loan = pd.read_csv(PATH + 'D_loan.csv')
D_close_loan = pd.read_csv(PATH + 'D_close_loan.csv')
D_target = pd.read_csv(PATH + 'D_target.csv')


# In[4]:


D_clients.describe()


# In[ ]:





# In[5]:


D_job.describe()


# In[6]:


D_salary.describe()


# In[7]:


D_last_credit.describe()


# In[8]:


D_close_loan.describe()


# In[9]:


D_target.describe()


# В таблицах нет аномальных значений

# Удалим явные дубликаты из таблиц

# In[10]:


D_clients = D_clients.drop_duplicates()
D_job = D_job.drop_duplicates()
D_salary = D_salary.drop_duplicates()
D_last_credit = D_last_credit.drop_duplicates()
D_close_loan = D_close_loan.drop_duplicates()
D_target = D_target.drop_duplicates()
D_loan = D_loan.drop_duplicates()


# In[11]:


D_target


# In[12]:


df


# In[ ]:





# Объединим таблицы в одну

# In[13]:


df = D_clients.merge(D_job, left_on='ID', right_on='ID_CLIENT', how='left')
df = df.merge(D_salary, left_on='ID', right_on='ID_CLIENT', how='left')
df = df.merge(D_last_credit, left_on='ID', right_on='ID_CLIENT', how='left')

df = df.merge(D_target, left_on='ID', right_on='ID_CLIENT', how='inner')


num_total = D_loan.groupby('ID_CLIENT').agg('count')
df = df.merge(num_total, left_on='ID', right_on='ID_CLIENT', how='left')

D_loan = D_loan.merge(D_close_loan, on='ID_LOAN', how='left')
D_loan_group = D_loan.groupby(by='ID_CLIENT').agg('sum')

df = df.merge(D_loan_group, left_on='ID', right_on='ID_CLIENT', how='left')


# Удалим ненужные столбцы

# In[14]:


df = df.drop(['REG_ADDRESS_PROVINCE', 'FACT_ADDRESS_PROVINCE', 'POSTAL_ADDRESS_PROVINCE', 'FL_PRESENCE_FL',
         'OWN_AUTO', 'GEN_INDUSTRY', 'JOB_DIR', 'GEN_TITLE', 'WORK_TIME', 'ID_CLIENT_x', 'FAMILY_INCOME', 'ID_CLIENT_y', 
        'CREDIT', 'TERM', 'FST_PAYMENT', 'ID_CLIENT_x', 'ID_LOAN_y', 'EDUCATION', 'MARITAL_STATUS', 'ID'], axis=1)


# In[15]:


df.columns


# In[16]:


df = df.rename(columns={"ID_LOAN_x": "LOAN_NUM_TOTAL", "CLOSED_FL": "LOAN_NUM_CLOSED"})


# Проверим на пропуски

# In[17]:


df.isna().sum()


# In[18]:


df.to_csv(r'C:\Users\nikel\OneDrive\Рабочий стол\data\df.csv', index=False)


# ## Задание 2
# 
# При помощи инструмента Streamlit проведите разведочный анализ данных. В него может входить:
# 
# * построение графиков распределений признаков
# * построение матрицы корреляций
# * построение графиков зависимостей целевой переменной и признаков
# * вычисление числовых характеристик распределения числовых столбцов (среднее, min, max, медиана и так далее)
# * любые другие ваши идеи приветствуются!
# 
# [Пример Streamlit-приложения](https://rateyourflight.streamlit.app) с разведочным анализом, прогнозом модели и оценкой ее результатов.

# In[32]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


Распределение личного дохода


# In[28]:


plt.boxplot(df['PERSONAL_INCOME'])
plt.show()


# Распределение возраста

# In[29]:


plt.boxplot(df['AGE'])
plt.show()


# Матрица корреляций

# In[41]:


plt.figure(figsize=(16, 8))
sns.heatmap(df.corr(), annot=True)
plt.show()


# Зависимость целевой переменной от личного дохода

# In[46]:


plt.bar(df['TARGET'], df['PERSONAL_INCOME'])
plt.show()


# Зависимость целевой переменной от возраста

# In[47]:


plt.bar(df['TARGET'], df['AGE'])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




