import pandas as pd

# ----------------------------
# 1. Carregar arquivos
# ----------------------------

inventario = pd.read_excel("dados/auditoria_tipo_documental.xlsx")
tipos = pd.read_excel("dados/tipos_documentais.xlsx")

# ----------------------------
# 2. Criar dicionário tipo -> categoria
# ----------------------------

tipo_categoria = dict(zip(
    tipos["nome_tipo"].astype(str).str.strip(),
    tipos["categoria_macro"].astype(str).str.strip()
))

# ----------------------------
# 3. Definir prioridade
# ----------------------------

prioridade = {
    "Jurídico": 1,
    "Técnico": 2,
    "Financeiro": 3,
    "Administrativo": 4,
    "Comunicação": 5,
    "Operacional": 6,
    "Não classificado": 7
}

# ----------------------------
# 4. Escolher tipo principal
# ----------------------------

def escolher_tipo(texto):

    if pd.isna(texto):
        return "Não identificado"

    tipos_detectados = [t.strip() for t in str(texto).split(",") if t.strip()]

    melhor_tipo = None
    melhor_prioridade = 999

    for tipo in tipos_detectados:

        categoria = tipo_categoria.get(tipo)

        if categoria is None:
            continue

        p = prioridade.get(categoria, 999)

        if p < melhor_prioridade:
            melhor_prioridade = p
            melhor_tipo = tipo

    if melhor_tipo:
        return melhor_tipo

    return "Não identificado"

# ----------------------------
# 5. Aplicar classificação
# ----------------------------

inventario["Tipo Documental"] = inventario["Tipo Documental Detectado"].apply(escolher_tipo)

# ----------------------------
# 6. Salvar resultado
# ----------------------------

inventario.to_excel("dados/inventario_classificado.xlsx", index=False)

print("Classificação concluída.")
print("Arquivo gerado: dados/inventario_classificado.xlsx")
