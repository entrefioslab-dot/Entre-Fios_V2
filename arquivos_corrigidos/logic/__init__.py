# -*- coding: utf-8 -*-
"""
Pacote de Lógica
Centraliza toda a lógica de cálculos e geração de documentos.
"""

from .calculos import (
    calcular_frete_fornecedor,
    calcular_desconto_progressivo,
    calcular_pacotes_envio,
    calcular_custo_item,
    calcular_resumo_orcamento
)

from .pdf_generator import gerar_proposta_pdf

__all__ = [
    'calcular_frete_fornecedor',
    'calcular_desconto_progressivo',
    'calcular_pacotes_envio',
    'calcular_custo_item',
    'calcular_resumo_orcamento',
    'gerar_proposta_pdf',
]
