# -*- coding: utf-8 -*-
"""
ENTRE FIOS
Sistema de orçamento
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
import pandas as pd
from data.fornecedores import obter_fornecedores, obter_produtos_fornecedor, obter_produto_info
from data.estampas import obter_custos_estampa
from data.pagamentos import obter_formas_pagamento
from logic.calculos import calcular_resumo_orcamento
from logic.pdf_generator import gerar_proposta_pdf

# --- Configuração da Página ---
st.set_page_config(
    layout="wide",
    page_title="Sistema de Orçamento de Estamparia",
    initial_sidebar_state="expanded"
)

# --- Inicialização do Estado da Sessão ---
if "orcamento_itens" not in st.session_state:
    st.session_state.orcamento_itens = []

# --- Título e Descrição ---
st.title("👕 Sistema de Orçamento de Estamparia")
st.markdown("**Ferramenta profissional para cálculo de orçamentos com múltiplos fornecedores**")
st.markdown("---")

# --- SIDEBAR - Instruções ---
with st.sidebar:
    st.header("📋 Instruções de Uso")
    st.markdown("""
    **Passo a passo:**
    
    1. Selecione um **fornecedor** e o **produto**
    2. Escolha os tipos de **estampa** (frente/costas)
    3. Defina a **quantidade** de peças
    4. Clique em **"Adicionar ao Orçamento"**
    5. Selecione a **forma de pagamento**
    6. Visualize o **resumo** e **gere o PDF**
    """)
    
    st.markdown("---")
    st.markdown("**Versão:** 3.1 | **Data:** 14/02/2026")

# --- SEÇÃO 1: Adição de Itens ---
st.header("1️⃣ Adicionar Item ao Orçamento")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    fornecedor_selecionado = st.selectbox(
        "Fornecedor",
        obter_fornecedores(),
        key="fornecedor_select"
    )

with col2:
    produtos_do_fornecedor = obter_produtos_fornecedor(fornecedor_selecionado)
    produto_selecionado = st.selectbox(
        "Produto",
        produtos_do_fornecedor,
        key="produto_select"
    )

with col3:
    estampa_frente = st.selectbox(
        "Estampa Frente",
        list(obter_custos_estampa().keys()),
        key="estampa_frente_select"
    )

with col4:
    estampa_costas = st.selectbox(
        "Estampa Costas",
        list(obter_custos_estampa().keys()),
        key="estampa_costas_select"
    )

with col5:
    quantidade = st.number_input(
        "Quantidade",
        min_value=1,
        value=1,
        step=1,
        key="quantidade_input"
    )

# Botão para adicionar item
col_btn1, col_btn2 = st.columns([3, 1])
with col_btn1:
    if st.button("➕ Adicionar ao Orçamento", use_container_width=True):
        produto_info = obter_produto_info(fornecedor_selecionado, produto_selecionado)
        if produto_info:
            st.session_state.orcamento_itens.append({
                'fornecedor': fornecedor_selecionado,
                'produto_nome': produto_selecionado,
                'produto_info': produto_info,
                'estampa_frente': estampa_frente,
                'estampa_costas': estampa_costas,
                'quantidade': quantidade,
            })
            st.success(f"✅ {quantidade}x {produto_selecionado} adicionado ao orçamento!")

st.markdown("---")

# --- SEÇÃO 2: Itens no Orçamento ---
st.header("2️⃣ Itens no Orçamento")

if not st.session_state.orcamento_itens:
    st.info("📭 Nenhum item adicionado ao orçamento ainda. Comece adicionando um produto acima.")
else:
    # Tabela de itens
    df_orcamento = pd.DataFrame([
        {
            "Fornecedor": item["fornecedor"],
            "Produto": item["produto_nome"],
            "Estampa Frente": item["estampa_frente"],
            "Estampa Costas": item["estampa_costas"],
            "Qtd": item["quantidade"],
            "Peso (kg)": f"{item['produto_info']['peso'] * item['quantidade']:.2f}"
        }
        for item in st.session_state.orcamento_itens
    ])
    
    st.dataframe(df_orcamento, use_container_width=True, hide_index=True)

    # Seção de remoção de itens
    st.subheader("Remover Item")
    col_remove1, col_remove2 = st.columns([3, 1])
    with col_remove1:
        if st.session_state.orcamento_itens:
            item_para_remover = st.selectbox(
                "Selecione o item para remover:",
                range(len(st.session_state.orcamento_itens)),
                format_func=lambda x: f"{st.session_state.orcamento_itens[x]['quantidade']}x {st.session_state.orcamento_itens[x]['produto_nome']} ({st.session_state.orcamento_itens[x]['fornecedor']})",
                key="remove_select"
            )
    with col_remove2:
        if st.button("🗑️ Remover", use_container_width=True):
            st.session_state.orcamento_itens.pop(item_para_remover)
            st.rerun()

st.markdown("---")

# --- SEÇÃO 3: Resumo e Cálculos ---
if st.session_state.orcamento_itens:
    st.header("3️⃣ Resumo do Orçamento")

    # Seleção da forma de pagamento
    col_pagamento, col_space = st.columns([2, 3])
    with col_pagamento:
        forma_pagamento_selecionada = st.selectbox(
            "Forma de Pagamento",
            obter_formas_pagamento(),
            key="pagamento_select"
        )

    # Calcular resumo
    resumo = calcular_resumo_orcamento(st.session_state.orcamento_itens, forma_pagamento_selecionada)

    # --- Informações para o Cliente ---
    st.subheader("💰 Informações para o Cliente")
    
    # Lista de modelos e detalhes
    st.markdown("### 📝 Detalhes dos Produtos")
    for item in resumo['itens']:
        estampas = []
        if item['estampa_frente'] != 'Nenhum': estampas.append(f"Frente: {item['estampa_frente']}")
        if item['estampa_costas'] != 'Nenhum': estampas.append(f"Costas: {item['estampa_costas']}")
        estampa_str = " | ".join(estampas) if estampas else "Sem estampa"
        
        st.markdown(f"- **Modelo:** {item['produto_nome']} | **Estampa:** {estampa_str} | **Qtd:** {item['quantidade']} un | **Valor Unitário:** R$ {item['valor_venda_unitario']:.2f}")

    st.markdown("---")
    
    col_cliente1, col_cliente2, col_cliente3 = st.columns(3)
    
    with col_cliente1:
        st.metric(
            label="Valor Total",
            value=f"R$ {resumo['valor_final_com_taxa']:.2f}",
            delta=f"Desconto: {resumo['percentual_desconto']:.1%}" if resumo['percentual_desconto'] > 0 else None
        )
    
    with col_cliente2:
        st.metric(
            label="Forma de Pagamento",
            value=forma_pagamento_selecionada
        )
    
    with col_cliente3:
        if resumo['num_parcelas'] > 1:
            st.metric(
                label="Parcelamento",
                value=f"{resumo['num_parcelas']}x",
                delta=f"R$ {resumo['valor_parcela']:.2f}"
            )
        else:
            st.metric(
                label="Quantidade Total de Peças",
                value=f"{resumo['total_quantidade']}"
            )

    # --- Informações Internas ---
    st.subheader("🔍 Informações Internas (Uso Interno)")
    
    col_int1, col_int2, col_int3, col_int4 = st.columns(4)
    
    with col_int1:
        st.metric(
            label="Custo Total",
            value=f"R$ {resumo['custo_total']:.2f}"
        )
    
    with col_int2:
        st.metric(
            label="Lucro",
            value=f"R$ {resumo['lucro_total']:.2f}",
            delta=f"Margem: {resumo['margem_percentual']:.2f}%"
        )
    
    with col_int3:
        st.metric(
            label="Taxa de Pagamento",
            value=f"R$ {resumo['valor_taxa']:.2f}",
            delta=f"{resumo['taxa_percentual']:.2f}%"
        )
    
    with col_int4:
        st.metric(
            label="Desconto Progressivo",
            value=f"R$ {resumo['valor_desconto']:.2f}",
            delta=f"{resumo['percentual_desconto']:.1%}"
        )

    st.markdown("---")

    # --- Geração de PDF ---
    st.header("4️⃣ Gerar Proposta Comercial")
    
    pdf_output = gerar_proposta_pdf(resumo)
    
    col_pdf1, col_pdf2 = st.columns([2, 1])
    with col_pdf1:
        st.download_button(
            label="📥 Baixar Proposta em PDF",
            data=pdf_output,
            file_name="proposta_comercial.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    
    with col_pdf2:
        if st.button("🔄 Atualizar Cálculos", use_container_width=True):
            st.rerun()

else:
    st.info("📭 Adicione itens ao orçamento para visualizar o resumo e gerar a proposta.")

st.markdown("---")
st.markdown("**© 2026 - Sistema de Orçamento de Estamparia | Desenvolvido com Streamlit**")
