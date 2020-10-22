from google.colab import auth
import gspread
import pandas as pd
import numpy as np
import glob
import datetime


auth.authenticate_user()
from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default())

worksheet = gc.open('Formulário de Atendimento Unificado (respostas)').sheet1

#a fórmula get_all_values retorna uma lista de linhas e colunas
columns = worksheet.get_all_records()
rows = worksheet.get_all_values()
ws = pd.DataFrame.from_records(columns)

ws.head()
ws['Equipamento'].unique()
ws = ws[~(ws['Equipamento'] == ' ')]
ws['Equipamento'].unique()

for equip in ws['Equipamento'].unique():
  print(equip)
  ws_equip = ws[ws['Equipamento'] == equip]
  ws_equip.to_csv('/content/drive/My Drive/Gestão da Informação/Monitoramento Rede de Serviços/M&A - Rede de Direitos Humanos/Bases/' + equip + '.csv')
