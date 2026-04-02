# 📁 Projeto Prado Chaves — Inventário Documental

Projeto desenvolvido para estruturar e viabilizar a recuperação eficiente de documentos físicos armazenados em arquivo externo, eliminando a dependência de conhecimento informal e reduzindo o tempo de localização das informações.

## 📌 Objetivo

Estruturar um inventário digital de documentos físicos armazenados em caixas, com foco na **localização rápida e eficiente da informação**.

O projeto organiza registros históricos provenientes de relatórios não estruturados, transformando-os em uma base consistente, padronizada e consultável.

---

## 🗂️ Estrutura do Projeto

```
PRADO_CHAVES/
│
├── _dados/
│   ├── inventario_prado_chaves_original.xlsx
│   ├── inventario_classificado.xlsx
│   └── inventario_final_prado_chaves.xlsx
│
├── _scripts/
│   ├── auditoria_tipo_documental_A.py
│   ├── classificacao_tipo_documental_B.py
│   ├── revisao_estrutura_C.py
│   └── classificar_assunto_D.py
│
├── documentação/
│   ├── Manual de Metodologia do Inventário Documental.docx
│   ├── Registro de Evolução Projeto de Catalogação Prado Chaves.docx
│   └── Resumo Executivo.docx
│
├── sql/
│   ├── queries.slq
│    
│
└── README.md
```

---

## 🔄 Pipeline de Tratamento de Dados

```
PDFs históricos
↓
Extração assistida por IA
↓
Padronização textual
↓
Consolidação em planilha
↓
Auditoria textual (Python)
↓
Classificação documental (Python)
↓
Reestruturação do inventário
↓
Modelagem e análise de dados (SQL)
↓
Inventário final estruturado
```

---

## 🧠 Metodologia

O projeto foi conduzido com base em três princípios:

* **Não inferência de conteúdo**: apenas informações explicitamente presentes foram consideradas
* **Validação humana**: todas as classificações automatizadas foram revisadas
* **Rastreabilidade**: todas as etapas do processo foram documentadas

---

## 🧩 Estrutura do Inventário Final

O inventário consolidado contém os seguintes campos:

* **Caixa** — identificação física da unidade de armazenamento
* **Unidade Organizacional** — origem do acervo
* **Assunto** — empreendimento ou referência documental
* **Tipo de Assunto** — natureza do assunto (ex.: empreendimento, premiação)
* **Tipo Documental** — classificação do documento
* **Data/Período** — referência temporal
* **Descrição** — detalhamento do conteúdo
* **Observação** — informações complementares

---

## 🔍 Forma de Consulta

O inventário permite recuperação da informação por diferentes caminhos:

* por **assunto** (ex.: empreendimento ou instituição)
* por **tipo documental** (ex.: contratos, correspondências)
* por **caixa física**

O objetivo principal é permitir a **identificação rápida da localização dos documentos no arquivo físico**.

---

## ⚙️ Tecnologias Utilizadas

* Python (pandas)
* Excel
* Inteligência Artificial (apoio à extração e padronização textual)
* SQLite online (modelagem e análise de dados)
  
---

## ⚙️ Após o tratamento dos dados com Python, foi realizada a modelagem e análise utilizando SQLite.

As principais análises incluíram:

* Distribuição de documentos por tipo documental
* Volume de documentos por assunto
* Cruzamento entre assunto e tipo documental
* Identificação de inconsistências nos dados

As consultas SQL utilizadas estão disponíveis em /sql/queries.sql.

---

### Exemplo de Análise

Consulta: Quantidade de documentos por tipo documental

Resultado (exemplo):

- Contratos: 46
- Correspondências: 38
- Documentos legais: 20

---

## 📊 Principais Insights

A análise dos dados permitiu identificar alguns padrões relevantes:

- A maior parte dos documentos está concentrada em determinados tipos documentais, como contratos e correspondências
- Existem ocorrências de dados classificados como "Não identificado", indicando oportunidades de melhoria na catalogação
- Alguns assuntos apresentam maior volume documental, sugerindo áreas de maior atividade histórica
- Foi possível identificar variações na padronização de tipos documentais, evidenciando a necessidade de normalização dos dados

Esses insights contribuem para uma melhor organização do acervo e suporte à tomada de decisão.


## 📌 Status do Projeto

Projeto finalizado com inventário estruturado, padronizado e validado para uso operacional.

---

