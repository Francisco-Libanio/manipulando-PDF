import tabula
from pikepdf import Pdf, PdfImage
import PyPDF2

def extrai_tabelas(link, pages='all'):
    return tabula.read_pdf(link, pages=pages)


def extrai_imagens(arquivo, caminho_da_pasta):
    documento = Pdf.open(arquivo)
    for pagina in documento.pages:
        for nome, imagem in pagina.images.items():
            salvar_imagem = PdfImage(imagem)
            salvar_imagem.extract_to(fileprefix=f'{caminho_da_pasta}/{nome}')


def extrai_textos(caminho_arquivo, palavra_chave, separador='\n'):
    lista_texto = []

    with open(caminho_arquivo, 'rb') as arquivo:
        leitor = PyPDF2.PdfReader(arquivo)

        for pagina_num in range(len(leitor.pages)):
            texto_pagina = leitor.pages[pagina_num].extract_text()
            paragrafos = texto_pagina.split(separador)

            for paragrafo in paragrafos:
                if palavra_chave.lower() in paragrafo.lower():
                    lista_texto.append(paragrafo)

    return lista_texto
