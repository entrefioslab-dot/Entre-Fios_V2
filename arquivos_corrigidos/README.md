# Sistema de Orçamento de Estamparia

Sistema profissional para cálculo de orçamentos com múltiplos fornecedores.

## Estrutura do Projeto

```
ENTRE-FIOS/
├── data/
│   ├── __init__.py
│   ├── estampas.py
│   ├── fornecedores.py
│   └── pagamentos.py
├── logic/
│   ├── __init__.py
│   ├── calculos.py
│   └── pdf_generator.py
├── app.py
├── README.md
└── requirements.txt
```

## Descrição dos Módulos

### data/
Pacote que centraliza todos os dados do sistema:
- **estampas.py**: Custos de estampas DTF e custos fixos de produção
- **fornecedores.py**: Dados de fornecedores e produtos
- **pagamentos.py**: Formas de pagamento e taxas

### logic/
Pacote que contém a lógica de negócio:
- **calculos.py**: Funções matemáticas para cálculo de orçamentos
- **pdf_generator.py**: Geração de propostas comerciais em PDF

### app.py
Interface Streamlit para interação com o usuário.

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
streamlit run app.py
```

## Correções Realizadas

1. **Estrutura de importações corrigida** em `calculos.py`:
   - Importações agora vêm de `data.estampas` e `data.pagamentos`
   - Adicionada importação de `obter_custo_estampa`

2. **Estrutura de importações corrigida** em `app.py`:
   - Importações específicas de funções necessárias
   - Corrigido nome do módulo `calculos`
   - Adicionadas importações de `obter_produtos_fornecedor` e `obter_produto_info`

3. **Nome do arquivo corrigido**:
   - `pdf.generator.py` → `pdf_generator.py`

4. **Arquivos `__init__.py` criados**:
   - Facilitam importações entre módulos
   - Exportam funções públicas de cada pacote

## Observações

- A lógica de cálculo foi mantida intacta conforme solicitado
- Apenas estrutura e importações foram corrigidas
- Sistema pronto para uso com Streamlit
