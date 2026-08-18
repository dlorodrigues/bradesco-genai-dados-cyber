# 📊 Processo de ETL com Power Query — Base SAP

Projeto prático desenvolvido na aula **02.5** com o objetivo de construir um pipeline de **ETL (Extract, Transform, Load)** sobre uma base bruta extraída de um sistema ERP (SAP).

---

## 🎯 Objetivo do Projetos
Tratar e sanitizar os dados brutos da planilha `sap_extract_raw.xlsx`, eliminando ruídos, corrigindo inconsistências de tipos de dados e gerando uma base consolidada para análise de estoque e faturamento.

---

## 🛠️ Pipeline de ETL Aplicado

### 1. Extração (Extract)
* **Fonte de dados:** Planilha Excel contendo a aba `SAP-EXTRACT` (118 registros brutos).
* **Conexão:** Ingestão do arquivo no editor do **Power Query**.

### 2. Transformação (Transform)
* **Higienização de Linhas:** Remoção de 4 linhas totalmente nulas e filtragem de registros corrompidos/incompletos (contendo marcadores `-----`).
* **Tratamento de Moeda (`Preço Unit Price`):** Remoção de caracteres especiais (`$`), limpeza de espaçamentos e conversão de tipo de dado de `Texto` para `Número Decimal (Moeda)`.
* **Tratamento de Estoque (`Stock Quantity`):** Ajuste do tipo de dado de `Texto` para `Número Inteiro`.
* **Padronização Temporal (`Send Date`):** Conversão de formatos de texto/data para o tipo de dado `Data`.
* **Métrica Calculada (`Total Value`):** Criação de coluna personalizada multiplicando `Stock Quantity` $\times$ `Preço Unit Price`.

### 3. Carga (Load)
* Carga da base tratada e modelada contendo **109 registros válidos**.
* Exportação para uma nova tabela dinamizada no Excel / Modelo de Dados do Power Pivot.

---

## 📈 Resultados da Base Higienizada

* **Registros Válidos:** 109 itens
* **Volume Total em Estoque:** 11.341 unidades
* **Valor Total Consolidado em Estoque:** $411.239,81