from funcoes_pdf import extrai_textos

lista = extrai_textos('ResultadoVale.pdf', palavra_chave='vendas', separador= '.')

for i in lista:
    print(i)