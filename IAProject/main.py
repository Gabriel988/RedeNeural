import plotly as pl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from Classes.Person import Person

pd.set_option('display.max_columns', None)  # Mostra todas as colunas
pd.set_option('display.max_rows', None)     # Mostra todas as linhas
pd.set_option('display.max_colwidth', None) # Ajusta a largura das colunas
pd.set_option('display.width', None)        # Ajusta a largura máxima de exibição

base_credit = pd.read_csv(r'C:\Users\gabri\Desktop\Gabriel\credit_risk_dataset.csv')

print(base_credit.head(5))
print('-----------------------------')
print(base_credit.describe())
print('-----------------------------')

print(np.unique(base_credit['cb_person_default_on_file'],return_counts=True))

data = np.unique(base_credit['cb_person_default_on_file'],return_counts=True)
x = data[0]
y = data[1]