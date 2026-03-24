import pandas as pd
import os

import re
import unicodedata

def normalizar(texto):

    if pd.isna(texto):
        return ""

    texto = str(texto).lower()

    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")

    return texto

# localizar pasta do script
pasta = os.path.dirname(__file__)

# carregar inventário
inventario = pd.read_excel(os.path.join(pasta, "inventario_prado_chaves.xlsx"))

# carregar tabela de tipos
tipos = pd.read_excel(os.path.join(pasta, "tipos_documentais.xlsx"))

# lista de tipos documentais
palavras_chave = dict(zip(tipos["palavra_chave"], tipos["nome_tipo"]))

# função para procurar tipo na descrição
def encontrar_tipo(texto):

    texto = normalizar(texto)

    encontrados = []

    for chave, tipo in palavras_chave.items():

        chave_norm = normalizar(chave)

        if re.search(chave_norm, texto):
            encontrados.append(tipo)

    if encontrados:
        return ", ".join(str(x) for x in set(encontrados))

    return None

# aplicar na coluna descrição
inventario["Tipo Documental Detectado"] = inventario["Descrição"].apply(encontrar_tipo)

# salvar resultado
inventario.to_excel("auditoria_tipo_documental.xlsx", index=False)

print("Auditoria concluída. Arquivo gerado: auditoria_tipo_documental.xlsx")