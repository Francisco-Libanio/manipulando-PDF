from funcoes_pdf import extrai_tabelas
import pandas as pd


vale = extrai_tabelas(
    'http://www.vale.com/PT/investors/information-market/quarterly-results/ResultadosTrimestrais/Vale_IFRS_1T21_BRL_v26042021_vf.pdf',
    pages='10',
)
vale = vale[0]
vale.columns = vale.iloc[0]
vale[[0, 1]] = vale["Variação percentual"].str.split(" ", expand=True)
vale = vale[1:9]
vale = vale.set_index("R$ milhões")
vale.columns = vale.iloc[0]
vale = vale[1:]
vale = vale.drop('1T21/4T20 1T21/1T20',axis=1)
print(vale)
