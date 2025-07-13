# Painel Dinâmico de Processos

### Planilha sem Excel, via DuckDB

> **Esqueça o Excel. Prepare-se para o DuckDB.**

## Visão Geral

Este projeto demonstra como construir um painel analítico profissional utilizando **DuckDB** como motor de consultas, completamente dispensando a necessidade de planilhas tradicionais. Desenvolvido especificamente para advogados e profissionais que lidam com grandes volumes de dados processuais, esta solução oferece velocidade, flexibilidade e controle total sobre suas análises.

## Por que DuckDB?

### Não é Excel

Enquanto o Excel é excelente para dados menores e manipulação manual, o DuckDB é um **banco de dados analítico** que vive dentro do seu programa. Ele processa milhões de linhas de dados em segundos, diretamente no seu computador, sem a necessidade de servidores complexos.

### Seus dados, seu controle

Carregamos dados de arquivos CSV e os consultamos com a velocidade e flexibilidade do SQL. Isso significa que você tem o poder de um banco de dados robusto, mas com a simplicidade de um arquivo que você já conhece.

### Velocidade e Eficiência

Para advogados que precisam analisar grandes volumes de processos, prazos e valores, o DuckDB permite análises complexas em um piscar de olhos, sem travar sua máquina ou exigir softwares caros.

## Características Principais

- **Análise em tempo real** de dados processuais
- **Cálculo automático de honorários** baseado em regras customizáveis
- **Consultas SQL diretas** em arquivos CSV
- **Interface intuitiva** construída com Streamlit
- **Processamento local** - sem necessidade de servidores externos
- **Integração de múltiplas fontes** - combine dados de planilhas independentes

## Funcionalidades

### Gestão de Processos

- Carregamento dinâmico de dados CSV
- Análise de prazos e valores
- Visualização de métricas em tempo real
- Filtros avançados por período, cliente, tipo de processo

### Cálculo de Honorários

- Regras personalizáveis de cálculo
- Relatórios detalhados por cliente
- Projeções de receita
- Análise de rentabilidade por caso

### Consultas Avançadas

- Interface SQL nativa para consultas complexas
- Agregações e agrupamentos dinâmicos
- Joins entre diferentes fontes de dados
- Exportação de resultados

## Tecnologias Utilizadas

- **DuckDB** - Motor de banco de dados analítico
- **Streamlit** - Framework para interface web
- **Python** - Linguagem de programação
- **Pandas** - Manipulação de dados
- **SQL** - Linguagem de consulta


## Estrutura do Projeto

```
painel-processos-duckdb/
├── app.py                 # Aplicação principal Streamlit
├── data/                  # Diretório para arquivos CSV
├── queries/               # Consultas SQL pré-definidas
├── utils/                 # Funções auxiliares
├── requirements.txt       # Dependências
└── README.md             # Este arquivo
```

## Exemplo de Consulta

```sql
SELECT 
    cliente,
    COUNT(*) as total_processos,
    SUM(valor_causa) as valor_total,
    AVG(valor_honorarios) as honorarios_medio
FROM processos 
WHERE data_inicio >= '2024-01-01'
GROUP BY cliente
ORDER BY valor_total DESC;
```


## Casos de Uso

### Para Advogados

- Controle de prazos processuais
- Análise de rentabilidade por cliente
- Relatórios de produtividade
- Gestão de carteira de clientes

### Para Escritórios

- Dashboard executivo
- Análise de performance por advogado
- Projeções financeiras
- Compliance e auditoria

### Para Desenvolvedores

- Exemplo prático de DuckDB em produção
- Integração Streamlit + DuckDB
- Padrões de consulta SQL otimizadas
- Interface responsiva para análise de dados

## Contato

Pedro Potz 

Link do Projeto: https://pedroduck.streamlit.app

---

**Curioso para ver como tudo isso funciona sem ser uma "planilha" comum?**
