# -*- coding: utf-8 -*-
"""
Dados de Fornecedores e Produtos
Módulo que centraliza todos os dados de fornecedores, produtos e suas características.
"""

FORNECEDORES = {
    'Usmark': {
        'produtos': [
            {'nome': 'Street Wear', 'valor': 23.87, 'peso': 0.185, 'base_frete': 18.40, 'curva_frete': 0.99, 'pacote_capacidade': 10},
            {'nome': 'Básica Masculina Regular Fit', 'valor': 22.85, 'peso': 0.185, 'base_frete': 21.32, 'curva_frete': 0.64, 'pacote_capacidade': 10},
            {'nome': 'Dry Fit UV', 'valor': 14.88, 'peso': 0.155, 'base_frete': 20.61, 'curva_frete': 0.60, 'pacote_capacidade': 12},
            {'nome': 'Gola Polo', 'valor': 33.42, 'peso': 0.250, 'base_frete': 27.84, 'curva_frete': 1.14, 'pacote_capacidade': 8},
            {'nome': 'Básica Oversized Malhão', 'valor': 34.44, 'peso': 0.270, 'base_frete': 23.33, 'curva_frete': 1.08, 'pacote_capacidade': 7},
            {'nome': 'Básica Plus Size', 'valor': 30.52, 'peso': 0.220, 'base_frete': 25.05, 'curva_frete': 0.82, 'pacote_capacidade': 9},
            {'nome': 'Básica Infantil', 'valor': 15.81, 'peso': 0.125, 'base_frete': 20.28, 'curva_frete': 0.58, 'pacote_capacidade': 16},
            {'nome': 'Bermuda Tactel', 'valor': 27.62, 'peso': 0.180, 'base_frete': 19.48, 'curva_frete': 0.89, 'pacote_capacidade': 10},
            {'nome': 'Moletom Canguru com Capuz', 'valor': 61.94, 'peso': 0.650, 'base_frete': 17.60, 'curva_frete': 2.00, 'pacote_capacidade': 3},
            {'nome': 'Moletom Gola Careca 3 Cabos', 'valor': 54.05, 'peso': 0.650, 'base_frete': 27.19, 'curva_frete': 1.34, 'pacote_capacidade': 3},
            {'nome': 'Básica Feminina', 'valor': 19.18, 'peso': 0.170, 'base_frete': 21.31, 'curva_frete': 0.56, 'pacote_capacidade': 11},
        ]
    },
    'Qualiju': {
        'produtos': [
            {'nome': 'Básica algodão', 'valor': 12.00, 'peso': 0.160, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 12},
            {'nome': 'Poliviscose', 'valor': 17.20, 'peso': 0.150, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 12},
            {'nome': 'Poliéster', 'valor': 13.40, 'peso': 0.150, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 12},
            {'nome': 'Poliviscose manga longa', 'valor': 18.90, 'peso': 0.190, 'base_frete': 16.52, 'curva_frete': 0.95, 'pacote_capacidade': 10},
            {'nome': 'Manga longa UV', 'valor': 31.90, 'peso': 0.210, 'base_frete': 16.53, 'curva_frete': 1.50, 'pacote_capacidade': 9},
            {'nome': 'Dry Fit', 'valor': 13.00, 'peso': 0.155, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 12},
            {'nome': 'Oversized 165g', 'valor': 22.90, 'peso': 0.230, 'base_frete': 16.53, 'curva_frete': 1.15, 'pacote_capacidade': 8},
            {'nome': 'Oversized 220g', 'valor': 31.90, 'peso': 0.260, 'base_frete': 16.53, 'curva_frete': 1.15, 'pacote_capacidade': 7},
            {'nome': 'Cropped Femino', 'valor': 14.50, 'peso': 0.145, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 13},
            {'nome': 'Baby Look Feminina', 'valor': 14.80, 'peso': 0.145, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 13},
            {'nome': 'Básica algodão infantil', 'valor': 12.90, 'peso': 0.110, 'base_frete': 16.52, 'curva_frete': 0.79, 'pacote_capacidade': 18},
            {'nome': 'Regata básica', 'valor': 16.60, 'peso': 0.140, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 14},
            {'nome': 'Baby Look Gola V Feminina', 'valor': 14.80, 'peso': 0.145, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 13},
            {'nome': 'Manga Longa Algodão', 'valor': 18.90, 'peso': 0.190, 'base_frete': 16.52, 'curva_frete': 0.95, 'pacote_capacidade': 10},
        ]
    },
    'MN Polos': {
        'produtos': [
            {'nome': 'Gola Polo Masculina', 'valor': 25.00, 'peso': 0.210, 'base_frete': 16.52, 'curva_frete': 0.95, 'pacote_capacidade': 9},
            {'nome': 'Gola Polo Feminina Baby Look', 'valor': 40.00, 'peso': 0.180, 'base_frete': 16.52, 'curva_frete': 0.70, 'pacote_capacidade': 10},
            {'nome': 'Básica Algodão', 'valor': 14.00, 'peso': 0.175, 'base_frete': 16.52, 'curva_frete': 0.90, 'pacote_capacidade': 11},
            {'nome': 'Dry Fit', 'valor': 15.00, 'peso': 0.160, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 12},
            {'nome': 'Dry Fit Grão de Arroz', 'valor': 15.00, 'peso': 0.160, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 12},
        ]
    },
    "Herker's": {
        'produtos': [
            {'nome': 'Básica Algodão', 'valor': 12.00, 'peso': 0.160, 'base_frete': 16.52, 'curva_frete': 0.90, 'pacote_capacidade': 12},
            {'nome': 'Básica Algodão Plus Size', 'valor': 19.00, 'peso': 0.230, 'base_frete': 16.52, 'curva_frete': 0.90, 'pacote_capacidade': 8},
            {'nome': 'Regata Unissex', 'valor': 18.90, 'peso': 0.145, 'base_frete': 16.52, 'curva_frete': 0.90, 'pacote_capacidade': 13},
            {'nome': 'Moletom Unissex', 'valor': 42.00, 'peso': 0.620, 'base_frete': 16.52, 'curva_frete': 1.00, 'pacote_capacidade': 3},
            {'nome': 'Básica algodão infantil', 'valor': 12.00, 'peso': 0.110, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 18},
            {'nome': 'Over Sized', 'valor': 23.00, 'peso': 0.240, 'base_frete': 16.52, 'curva_frete': 0.90, 'pacote_capacidade': 8},
            {'nome': 'Dry Fit', 'valor': 13.00, 'peso': 0.160, 'base_frete': 16.52, 'curva_frete': 0.80, 'pacote_capacidade': 12},
        ]
    }
}

def obter_fornecedores():
    """Retorna lista de nomes de fornecedores."""
    return list(FORNECEDORES.keys())

def obter_produtos_fornecedor(fornecedor):
    """Retorna lista de produtos de um fornecedor específico."""
    if fornecedor in FORNECEDORES:
        return [p['nome'] for p in FORNECEDORES[fornecedor]['produtos']]
    return []

def obter_produto_info(fornecedor, nome_produto):
    """Retorna informações completas de um produto específico."""
    if fornecedor in FORNECEDORES:
        for produto in FORNECEDORES[fornecedor]['produtos']:
            if produto['nome'] == nome_produto:
                return produto
    return None
