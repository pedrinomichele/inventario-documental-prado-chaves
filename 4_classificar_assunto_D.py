import pandas as pd

arquivo = "Resultado/inventario_reestruturado_prado_chaves.xlsx"

df = pd.read_excel(arquivo)

def classificar_assunto(texto):

    if pd.isna(texto):
        return "Não identificado"

    texto = str(texto).lower()

    if "riviera" in texto:
        return "Empreendimento"

    if "espaço cerâmica" in texto or "espaco ceramica" in texto:
        return "Empreendimento"

    if "são carlos" in texto or "sao carlos" in texto:
        return "Empreendimento"

    if "fiabci" in texto:
        return "Premiação"

    if "prêmio master" in texto or "premio master" in texto:
        return "Premiação"

    return "Institucional"


df["Tipo_de_Assunto"] = df["Assunto"].apply(classificar_assunto)

saida = "Resultado/inventario_com_assunto_classificado.xlsx"

df.to_excel(saida, index=False)

print("Classificação de assunto concluída.")