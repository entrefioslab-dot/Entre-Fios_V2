# -*- coding: utf-8 -*-
"""
Lógica de Cálculos de Orçamento
Módulo que contém todas as funções matemáticas para cálculo de orçamentos.
"""

import math
from data.estampas import (
    obter_custo_estampa,
    calcular_lucro_mao_obra,
    calcular_custos_fixos
)
from data.pagamentos import (
    obter_taxa_percentual,
    obter_num_parcelas
)

def calcular_frete_fornecedor(base, curva, quantidade):
    """
    Calcula o frete estimado do fornecedor com base nos parâmetros BASE e CURVA.
    
    Fórmula: Frete Total = BASE + (CURVA * Quantidade)
    Frete Unitário = Frete Total / Quantidade
    
    Args:
        base (float): Valor base do frete
        curva (float): Coeficiente de curvatura
        quantidade (int): Quantidade de peças
        
    Returns:
        float: Frete unitário
    """
    if quantidade <= 0:
        return 0.0
    frete_total = base + (curva * quantidade)
    return frete_total / quantidade

def calcular_desconto_progressivo(quantidade):
    """
    Calcula o desconto progressivo com base na quantidade.
    
    Fórmula: Desconto = MIN(QUOCIENTE(Quantidade, 10) * 0.03, 0.20)
    Ou seja: 3% a cada 10 unidades, máximo 20%
    
    Args:
        quantidade (int): Quantidade total de peças
        
    Returns:
        float: Percentual de desconto (0.0 a 0.20)
    """
    desconto = min((quantidade // 10) * 0.03, 0.20)
    return desconto

def calcular_pacotes_envio(itens_orcamento):
    """
    Calcula a quantidade de pacotes necessários para o envio ao cliente.
    
    Lógica:
    - Cada produto tem uma PACOTE_CAPACIDADE que indica quantas unidades cabem em um pacote.
    - O "volume" de um item é calculado como: quantidade / PACOTE_CAPACIDADE
    - O total de pacotes é o arredondamento para cima do volume total.
    
    Args:
        itens_orcamento (list): Lista de itens do orçamento
        
    Returns:
        tuple: (número de pacotes, peso total em kg)
    """
    if not itens_orcamento:
        return 0, 0.0
    
    volume_total = 0.0
    peso_total = 0.0
    
    for item in itens_orcamento:
        capacidade = item['produto_info']['pacote_capacidade']
        quantidade = item['quantidade']
        peso_unitario = item['produto_info']['peso']
        
        volume_item = quantidade / capacidade
        volume_total += volume_item
        peso_total += quantidade * peso_unitario
    
    num_pacotes = math.ceil(volume_total)
    return num_pacotes, peso_total

def calcular_custo_item(item, forma_pagamento):
    """
    Calcula todos os custos e valores de um item específico.
    
    Args:
        item (dict): Dicionário com informações do item
        forma_pagamento (str): Forma de pagamento selecionada
        
    Returns:
        dict: Dicionário com custos e valores calculados
    """
    quantidade = item['quantidade']
    produto_info = item['produto_info']
    estampa_frente = item['estampa_frente']
    estampa_costas = item['estampa_costas']
    
    # Calcular frete do fornecedor (por unidade)
    frete_unitario = calcular_frete_fornecedor(
        produto_info['base_frete'],
        produto_info['curva_frete'],
        quantidade
    )
    
    # Calcular custo de estampa
    custo_estampa_frente = obter_custo_estampa(estampa_frente)
    custo_estampa_costas = obter_custo_estampa(estampa_costas)
    custo_estampa_total_unitario = custo_estampa_frente + custo_estampa_costas
    
    # Custos fixos de produção (por unidade)
    custos_fixos_unitario = calcular_custos_fixos()
    
    # Custo real unitário (produto + frete + estampa + custos fixos)
    custo_unitario_real = (
        produto_info['valor'] +
        frete_unitario +
        custo_estampa_total_unitario +
        custos_fixos_unitario
    )
    
    # Lucro + Mão de Obra (por unidade)
    lucro_mao_obra_unitario = calcular_lucro_mao_obra()
    
    # Valor de venda unitário (custo real + lucro + mão de obra)
    valor_venda_unitario = custo_unitario_real + lucro_mao_obra_unitario
    
    # Totais para o item
    custo_total_item = custo_unitario_real * quantidade
    valor_venda_total_item = valor_venda_unitario * quantidade
    
    return {
        'frete_unitario': frete_unitario,
        'custo_estampa_frente': custo_estampa_frente,
        'custo_estampa_costas': custo_estampa_costas,
        'custo_estampa_total_unitario': custo_estampa_total_unitario,
        'custos_fixos_unitario': custos_fixos_unitario,
        'custo_unitario_real': custo_unitario_real,
        'lucro_mao_obra_unitario': lucro_mao_obra_unitario,
        'valor_venda_unitario': valor_venda_unitario,
        'custo_total_item': custo_total_item,
        'valor_venda_total_item': valor_venda_total_item,
    }

def calcular_resumo_orcamento(itens_orcamento, forma_pagamento):
    """
    Calcula o resumo completo do orçamento com todos os valores finais.
    
    Fórmulas:
    - Valor de venda base: Soma de (valor_venda_unitário * quantidade) para cada item
    - Desconto progressivo: Aplicado sobre o valor de venda base
    - Valor após desconto: Valor de venda base - Desconto
    - Taxa de pagamento: Aplicada sobre o valor após desconto
    - Valor final com taxa: Valor após desconto / (1 - taxa_percentual/100)
    - Lucro total: (Lucro + Mão de Obra) * Quantidade Total
    - Custo total: Valor final com taxa - Lucro total
    
    Args:
        itens_orcamento (list): Lista de itens do orçamento
        forma_pagamento (str): Forma de pagamento selecionada
        
    Returns:
        dict: Dicionário com resumo completo do orçamento
    """
    if not itens_orcamento:
        return None
    
    # Calcular custos de cada item
    itens_calculados = []
    for item in itens_orcamento:
        custos = calcular_custo_item(item, forma_pagamento)
        item_completo = {**item, **custos}
        itens_calculados.append(item_completo)
    
    # Totais gerais
    total_quantidade = sum(item['quantidade'] for item in itens_calculados)
    valor_venda_base = sum(item['valor_venda_total_item'] for item in itens_calculados)
    
    # Desconto progressivo
    percentual_desconto = calcular_desconto_progressivo(total_quantidade)
    valor_desconto = valor_venda_base * percentual_desconto
    valor_apos_desconto = valor_venda_base - valor_desconto
    
    # Taxa de pagamento
    taxa_percentual = obter_taxa_percentual(forma_pagamento)
    num_parcelas = obter_num_parcelas(forma_pagamento)
    taxa_decimal = taxa_percentual / 100.0
    
    # Valor final com taxa
    if (1 - taxa_decimal) != 0:
        valor_final_com_taxa = valor_apos_desconto / (1 - taxa_decimal)
    else:
        valor_final_com_taxa = valor_apos_desconto
    
    valor_taxa = valor_final_com_taxa - valor_apos_desconto
    
    # Lucro e Custo para uso interno
    lucro_mao_obra_unitario = calcular_lucro_mao_obra()
    lucro_total = lucro_mao_obra_unitario * total_quantidade
    custo_total = valor_final_com_taxa - lucro_total
    
    # Valor por parcela
    valor_parcela = valor_final_com_taxa / num_parcelas if num_parcelas > 0 else 0
    
    # Margem de lucro
    margem_percentual = (lucro_total / valor_final_com_taxa * 100) if valor_final_com_taxa > 0 else 0
    
    # Pacotes de envio
    num_pacotes, peso_total = calcular_pacotes_envio(itens_calculados)
    
    return {
        'itens': itens_calculados,
        'total_quantidade': total_quantidade,
        'valor_venda_base': valor_venda_base,
        'percentual_desconto': percentual_desconto,
        'valor_desconto': valor_desconto,
        'valor_apos_desconto': valor_apos_desconto,
        'taxa_percentual': taxa_percentual,
        'taxa_decimal': taxa_decimal,
        'valor_taxa': valor_taxa,
        'valor_final_com_taxa': valor_final_com_taxa,
        'forma_pagamento': forma_pagamento,
        'num_parcelas': num_parcelas,
        'valor_parcela': valor_parcela,
        'lucro_total': lucro_total,
        'custo_total': custo_total,
        'margem_percentual': margem_percentual,
        'num_pacotes': num_pacotes,
        'peso_total': peso_total,
    }
