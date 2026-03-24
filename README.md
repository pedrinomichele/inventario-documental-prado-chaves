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

---

## 📌 Status do Projeto

Projeto finalizado com inventário estruturado, padronizado e validado para uso operacional.

---

