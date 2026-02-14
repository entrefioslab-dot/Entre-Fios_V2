# -*- coding: utf-8 -*-
"""
Pacote de Dados
Centraliza todos os dados de fornecedores, estampas e formas de pagamento.
"""

from .estampas import (
    obter_custos_estampa,
    obter_custo_estampa,
    obter_custos_producao,
    calcular_lucro_mao_obra,
    calcular_custos_fixos
)

from .fornecedores import (
    obter_fornecedores,
    obter_produtos_fornecedor,
    obter_produto_info
)

from .pagamentos import (
    obter_formas_pagamento,
    obter_info_pagamento,
    obter_taxa_percentual,
    obter_num_parcelas
)

__all__ = [
    # Estampas
    'obter_custos_estampa',
    'obter_custo_estampa',
    'obter_custos_producao',
    'calcular_lucro_mao_obra',
    'calcular_custos_fixos',
    # Fornecedores
    'obter_fornecedores',
    'obter_produtos_fornecedor',
    'obter_produto_info',
    # Pagamentos
    'obter_formas_pagamento',
    'obter_info_pagamento',
    'obter_taxa_percentual',
    'obter_num_parcelas',
]
