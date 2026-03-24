import pandas as pd

# ---------------------------
# 1. Carregar inventário final
# ---------------------------

arquivo = "Dados/inventario_final_prado_chaves.xlsx"

df = pd.read_excel(arquivo)

print("Registros carregados:", len(df))


# ---------------------------
# 2. Criar coluna ASSUNTO
# ---------------------------

df["Assunto"] = df["Projeto/Categoria"]


# ---------------------------
# 3. Criar coluna TIPO_DE_ASSUNTO
# (inicialmente vazia para classificação futura)
# ---------------------------

df["Tipo_de_Assunto"] = ""


# ---------------------------
# 4. Renomear coluna de localização
# ---------------------------

df = df.rename(columns={
    "Localização/Tipo": "Unidade_Organizacional"
})


# ---------------------------
# 5. Reorganizar colunas
# ---------------------------

ordem_colunas = [
    "Caixa",
    "Unidade_Organizacional",
    "Assunto",
    "Tipo_de_Assunto",
    "Tipo Documental",
    "Descrição",
    "Data/Período",
    "Observação"
]

df = df[ordem_colunas]


# ---------------------------
# 6. Salvar nova versão do inventário
# ---------------------------

saida = "Resultado/inventario_reestruturado_prado_chaves.xlsx"

df.to_excel(saida, index=False)

print("Inventário reestruturado salvo em:", saida)