### ETL para análise temporal de vendas
O projeto implementa uma pipeline ETL para analisar dados de vendas ao longo do tempo utilizando Python e SQLite. Tem como objetivo realizar a extração do dados de vendas de um arquivo CSV, ransformá-los para calcular o total de vendas por mês e carregar os resultados em um banco de dados SQLite para análise posterior.

#### Dataset utilizado:
O dataset utilizado contém informações de vendas de um e-commerce, sendo as seguintes colunas principais:
- **InvoiceNo:** Num. identificador da fatura;
- **StockCode:** Cód. do produto;
- **Description:** Descrição do produto;
- **Quantity**: Qtd. vendida;
- **InvoiceDate:** Data/hora da fatura;
- **UnitPrice:** Preço unitário do produto;
- **CustomerID:** Identificador do cliente;
- **Country:** País de origem da compra

#### Ferramentas e tecnologias utilizadas:
- **Python**
- **pandas**
- **SQLite**
- **Jupyter Notebook**


#### Etapas da pieline ETL:
1. **Extração**: Os dados são lidos do arquivo CSV utilizando a biblioteca **pandas**.
2. **Transformação:**
   - Os valores nulos são limpos;
   - A coluna **InvoiceDate** é convertida para formato datetime;
   - O mês é extraído da data;
   - O total de vendas por transação é calculado multiplicando quantidade x preço unitário;
   - Os dados são agrupados por mês, somando o total das vendas.
3. **Carga:** Os dados transformados são salvos em uma tabela SQLite.

#### Instruções de uso:
Para executar o projeto localmente, siga os passos abaixo:
1. Clone o repositório:

```
git clone https://github.com/mariaeac/etl-pipeline-vendas-tempora
```
2. Instale as dependências:
```
pip install -r requirements.txt
```
3. Execute o script:
```
python etl_sales.py
```
#### Resultados:
Os resultados são armazenados na tabela ***sales_by_month** no banco SQLite. É possível consultar através de uma query como:
```
SELECT * FROM sales_by_month
```

