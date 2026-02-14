# -*- coding: utf-8 -*-
"""
Dados de Formas de Pagamento e Taxas
Módulo que centraliza as formas de pagamento e suas respectivas taxas.
"""

# Tabela de Taxas de Pagamento
# Formato: {'parcelas': número de parcelas, 'taxa_percentual': taxa em percentual}
TAXAS_PAGAMENTO = {
    'Pix': {
        'parcelas': 1,
        'taxa_percentual': 0.00
    },
    'Débito': {
        'parcelas': 1,
        'taxa_percentual': 1.37
    },
    'Crédito à vista': {
        'parcelas': 1,
        'taxa_percentual': 3.15
    },
    'Crédito 2x': {
        'parcelas': 2,
        'taxa_percentual': 5.39
    },
    'Crédito 3x': {
        'parcelas': 3,
        'taxa_percentual': 6.12
    },
    'Crédito 4x': {
        'parcelas': 4,
        'taxa_percentual': 6.85
    },
    'Crédito 5x': {
        'parcelas': 5,
        'taxa_percentual': 7.57
    },
    'Crédito 6x': {
        'parcelas': 6,
        'taxa_percentual': 8.28
    },
    'Crédito 7x': {
        'parcelas': 7,
        'taxa_percentual': 8.99
    },
    'Crédito 8x': {
        'parcelas': 8,
        'taxa_percentual': 9.69
    },
    'Crédito 9x': {
        'parcelas': 9,
        'taxa_percentual': 10.38
    },
    'Crédito 10x': {
        'parcelas': 10,
        'taxa_percentual': 11.06
    },
    'Crédito 11x': {
        'parcelas': 11,
        'taxa_percentual': 11.74
    },
    'Crédito 12x': {
        'parcelas': 12,
        'taxa_percentual': 12.40
    }
}

def obter_formas_pagamento():
    """Retorna lista de formas de pagamento disponíveis."""
    return list(TAXAS_PAGAMENTO.keys())

def obter_info_pagamento(forma_pagamento):
    """Retorna informações de uma forma de pagamento específica."""
    return TAXAS_PAGAMENTO.get(forma_pagamento, {'parcelas': 1, 'taxa_percentual': 0.00})

def obter_taxa_percentual(forma_pagamento):
    """Retorna a taxa percentual de uma forma de pagamento."""
    info = TAXAS_PAGAMENTO.get(forma_pagamento, {})
    return info.get('taxa_percentual', 0.00)

def obter_num_parcelas(forma_pagamento):
    """Retorna o número de parcelas de uma forma de pagamento."""
    info = TAXAS_PAGAMENTO.get(forma_pagamento, {})
    return info.get('parcelas', 1)
