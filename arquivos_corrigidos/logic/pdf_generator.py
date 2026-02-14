# -*- coding: utf-8 -*-
"""
Gerador de Proposta Comercial em PDF
Módulo que gera o PDF da proposta comercial para envio ao cliente.
"""

from datetime import datetime
from fpdf import FPDF
from io import BytesIO

def gerar_proposta_pdf(resumo_orcamento):
    """
    Gera um arquivo PDF com a proposta comercial para o cliente.
    
    Args:
        resumo_orcamento (dict): Dicionário com resumo do orçamento
        
    Returns:
        bytes: Conteúdo do PDF em bytes
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    
    # --- CABEÇALHO ---
    pdf.set_font("Arial", 'B', size=16)
    pdf.cell(0, 12, txt="PROPOSTA COMERCIAL", ln=True, align='C')
    pdf.set_font("Arial", size=9)
    pdf.cell(0, 6, txt=f"Data: {datetime.now().strftime('%d/%m/%Y às %H:%M')}", ln=True, align='C')
    pdf.ln(3)
    
    # --- RESUMO EXECUTIVO ---
    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 8, txt="RESUMO EXECUTIVO", ln=True, border=1)
    pdf.set_font("Arial", size=9)
    
    # Tabela de resumo
    col_width = 100
    pdf.cell(col_width, 6, txt="Valor Total do Orçamento:", border=0)
    pdf.cell(0, 6, txt=f"R$ {resumo_orcamento['valor_final_com_taxa']:.2f}", ln=True, border=0, align='R')
    
    pdf.cell(col_width, 6, txt="Forma de Pagamento:", border=0)
    pdf.cell(0, 6, txt=resumo_orcamento['forma_pagamento'], ln=True, border=0, align='R')
    
    if resumo_orcamento['num_parcelas'] > 1:
        pdf.cell(col_width, 6, txt=f"Parcelamento:", border=0)
        pdf.cell(0, 6, 
            txt=f"{resumo_orcamento['num_parcelas']}x de R$ {resumo_orcamento['valor_parcela']:.2f}",
            ln=True, border=0, align='R')
    
    pdf.cell(col_width, 6, txt="Quantidade Total de Peças:", border=0)
    pdf.cell(0, 6, txt=f"{resumo_orcamento['total_quantidade']}", ln=True, border=0, align='R')
    
    if resumo_orcamento['percentual_desconto'] > 0:
        pdf.cell(col_width, 6, txt="Desconto Progressivo:", border=0)
        pdf.cell(0, 6, 
            txt=f"{resumo_orcamento['percentual_desconto']:.1%} (R$ {resumo_orcamento['valor_desconto']:.2f})",
            ln=True, border=0, align='R')
    
    pdf.ln(3)
    
    # --- ITENS DO ORÇAMENTO ---
    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 8, txt="ITENS INCLUSOS", ln=True, border=1)
    pdf.set_font("Arial", size=8)
    
    for idx, item in enumerate(resumo_orcamento['itens'], 1):
        produto_info = item['produto_info']
        estampa_info = ""
        
        if item['estampa_frente'] != 'Nenhum' or item['estampa_costas'] != 'Nenhum':
            estampa_info = f" | Estampas: "
            if item['estampa_frente'] != 'Nenhum':
                estampa_info += f"Frente {item['estampa_frente']}"
            if item['estampa_costas'] != 'Nenhum':
                if item['estampa_frente'] != 'Nenhum':
                    estampa_info += f" + Costas {item['estampa_costas']}"
                else:
                    estampa_info += f"Costas {item['estampa_costas']}"
        
        pdf.multi_cell(0, 5,
            f"{idx}. {item['quantidade']}x {produto_info['nome']} "
            f"(R$ {item['valor_venda_unitario']:.2f} un){estampa_info}")
    
    pdf.ln(2)
    
    # --- INFORMAÇÕES PARA ENVIO ---
    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 8, txt="INFORMAÇÕES PARA ENVIO", ln=True, border=1)
    pdf.set_font("Arial", size=9)
    
    col_width = 100
    pdf.cell(col_width, 6, txt="Peso Total Estimado:", border=0)
    pdf.cell(0, 6, txt=f"{resumo_orcamento['peso_total']:.2f} kg", ln=True, border=0, align='R')
    
    pdf.cell(col_width, 6, txt="Número de Pacotes:", border=0)
    pdf.cell(0, 6, txt=f"{resumo_orcamento['num_pacotes']}", ln=True, border=0, align='R')
    
    pdf.cell(col_width, 6, txt="Dimensões Padrão por Pacote:", border=0)
    pdf.cell(0, 6, txt="32cm x 40cm", ln=True, border=0, align='R')
    
    pdf.ln(3)
    
    # --- RODAPÉ ---
    pdf.set_font("Arial", 'I', size=8)
    pdf.cell(0, 5,
        txt="Este é um orçamento preliminar. Valores sujeitos a alteração conforme confirmação de detalhes. "
            "Prazo de validade: 7 dias.",
        ln=True, align='C')
    
    # Retornar o PDF como bytes
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    return pdf_bytes
