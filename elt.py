#importa os pacotes necessários

#pacotes para trabalhar com o sheets
from google.colab import auth
import gspread

#Pandas é o melhor pacote de Python para manipulação de dados
import pandas as pd

#Pacote para trabalhar com arrays
import numpy as np

#Pacote para listar arquivos de diretório
import glob

#pacote para manipulação de data e horas
import datetime

#Importa as credencias para conectar ao Sheets
auth.authenticate_user()
from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default())

#Não há necessidade de copiar a URL da planilha aqui, basta inserir o nome do arquivo do Sheets
worksheet = gc.open('your Google Sheet').sheet1

#a fórmula get_all_values retorna as linhas e colunas
columns = worksheet.get_all_records()
rows = worksheet.get_all_values()
ws = pd.DataFrame.from_records(columns)

#traz os títulos das colunas
ws.head()

#traz os valores únicos
ws['váriavel que deseja retornar os valores únicos'].unique()

# Exclui os valores em branco
ws = ws[~(ws['váriavel que deseja retornar os valores únicos'] == ' ')]

#retorna novo resultado de valores únicos
ws['váriavel que deseja retornar os valores únicos'].unique()

#Função para filtrar os valores desejados e separar em planilhas separadas. Neste caso vamos salvar em CSV
for suafunção in ws['váriavel que deseja retornar os valores únicos'].unique():
  print(suafunção)
  ws_equip = ws[ws['váriavel que deseja retornar os valores únicos'] == equip]
  ws_equip.to_csv('caminho do local onde será salvo' + sua função + '.csv')

  
  
