import logging
from typing import List, Dict, Any, Optional

# Configurar logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Cardápio Pizza Hut - Promoções e Produtos
PIZZAHUT_MENU = {
    "COMBOS": {
        "MY BOX INDIVIDUAL": {
            "nome_completo": "My Box Individual",
            "descricao": "Pizza Individual + Batata Country ou Cheesy Pops + Refrigerante Lata",
            "preco": 35.90,
            "sku": "MB001",
            "atributos_requeridos": {
                "opcao": {
                    "nome": "Escolha sua opção",
                    "opcoes": {
                        "Pizza Individual": {"id": "MB001A", "descricao": "1 Pizza Individual (qualquer sabor) + acompanhamento + refri"},
                        "Melt": {"id": "MB001B", "descricao": "1 Melt (qualquer sabor) + acompanhamento + refri"}
                    }
                },
                "acompanhamento": {
                    "nome": "Escolha seu acompanhamento",
                    "opcoes": {
                        "Batata Country": {"id": "BC001", "descricao": "Batata Country crocante"},
                        "Cheesy Pops": {"id": "CP001", "descricao": "Bolinhas de queijo"}
                    }
                },
                "bebida": {
                    "nome": "Escolha sua bebida",
                    "opcoes": {
                        "Coca-Cola Lata": {"id": "CC350", "descricao": "Coca-Cola 350ml"},
                        "Guaraná Antártica Lata": {"id": "GA350", "descricao": "Guaraná Antártica 350ml"}
                    }
                }
            },
            "categoria": "combo"
        },
        "DUPLA IMBATIVEL": {
            "nome_completo": "Dupla Imbatível",
            "descricao": "2 Pizzas Grandes (sabores Tradicionais ou Especiais)",
            "preco": 99.90,
            "sku": "DI002",
            "atributos_requeridos": {
                "pizza1": {
                    "nome": "Escolha o sabor da primeira pizza",
                    "opcoes": {
                        "Mussarela": {"id": "P001", "descricao": "Pizza clássica de mussarela"},
                        "Calabresa": {"id": "P002", "descricao": "Calabresa com cebola"},
                        "Marguerita": {"id": "P003", "descricao": "Molho, mussarela, tomate e manjericão"},
                        "Pepperoni": {"id": "P004", "descricao": "Pepperoni clássico"},
                        "Portuguesa": {"id": "P005", "descricao": "Presunto, ovos, cebola, pimentão"},
                        "Frango com Requeijão": {"id": "P006", "descricao": "Frango desfiado com requeijão"}
                    }
                },
                "pizza2": {
                    "nome": "Escolha o sabor da segunda pizza",
                    "opcoes": {
                        "Mussarela": {"id": "P001", "descricao": "Pizza clássica de mussarela"},
                        "Calabresa": {"id": "P002", "descricao": "Calabresa com cebola"},
                        "Marguerita": {"id": "P003", "descricao": "Molho, mussarela, tomate e manjericão"},
                        "Pepperoni": {"id": "P004", "descricao": "Pepperoni clássico"},
                        "Portuguesa": {"id": "P005", "descricao": "Presunto, ovos, cebola, pimentão"},
                        "Frango com Requeijão": {"id": "P006", "descricao": "Frango desfiado com requeijão"}
                    }
                }
            },
            "categoria": "combo"
        },
        "COMBO FAMILIA": {
            "nome_completo": "Combo Família",
            "descricao": "2 Pizzas Grandes + 1 Entrada + Refrigerante 2L",
            "preco": 159.90,
            "sku": "CF003",
            "atributos_requeridos": {
                "pizza1": {
                    "nome": "Escolha o sabor da primeira pizza",
                    "opcoes": {
                        "Mussarela": {"id": "P001", "descricao": "Pizza clássica de mussarela"},
                        "Calabresa": {"id": "P002", "descricao": "Calabresa com cebola"},
                        "Pepperoni": {"id": "P004", "descricao": "Pepperoni clássico"},
                        "Supreme": {"id": "P007", "descricao": "Pepperoni, presunto, pimentão, cogumelos"},
                        "Meat Lovers": {"id": "P008", "descricao": "Pepperoni, calabresa, presunto, bacon"},
                        "Cheese Lovers": {"id": "P009", "descricao": "4 queijos deliciosos"}
                    }
                },
                "pizza2": {
                    "nome": "Escolha o sabor da segunda pizza",
                    "opcoes": {
                        "Mussarela": {"id": "P001", "descricao": "Pizza clássica de mussarela"},
                        "Calabresa": {"id": "P002", "descricao": "Calabresa com cebola"},
                        "Pepperoni": {"id": "P004", "descricao": "Pepperoni clássico"},
                        "Supreme": {"id": "P007", "descricao": "Pepperoni, presunto, pimentão, cogumelos"},
                        "Meat Lovers": {"id": "P008", "descricao": "Pepperoni, calabresa, presunto, bacon"},
                        "Cheese Lovers": {"id": "P009", "descricao": "4 queijos deliciosos"}
                    }
                },
                "entrada": {
                    "nome": "Escolha sua entrada",
                    "opcoes": {
                        "Cheesy Pops": {"id": "CP002", "descricao": "8 unidades de bolinhas de queijo"},
                        "Batata Country": {"id": "BC002", "descricao": "Porção família de batata country"}
                    }
                },
                "bebida": {
                    "nome": "Escolha sua bebida",
                    "opcoes": {
                        "Coca-Cola 2L": {"id": "CC2000", "descricao": "Coca-Cola 2 litros"},
                        "Guaraná Antártica 2L": {"id": "GA2000", "descricao": "Guaraná Antártica 2 litros"}
                    }
                }
            },
            "categoria": "combo"
        }
    },
    "PIZZAS": {
        "PIZZA INDIVIDUAL": {
            "nome_completo": "Pizza Individual",
            "descricao": "Pizza individual 4 fatias - qualquer sabor",
            "preco": 34.90,
            "sku": "PI001",
            "atributos_requeridos": {
                "sabor": {
                    "nome": "Escolha o sabor",
                    "opcoes": {
                        "Mussarela": {"id": "P001", "descricao": "Pizza clássica de mussarela"},
                        "Calabresa": {"id": "P002", "descricao": "Calabresa com cebola"},
                        "Marguerita": {"id": "P003", "descricao": "Molho, mussarela, tomate e manjericão"},
                        "Pepperoni": {"id": "P004", "descricao": "Pepperoni clássico"},
                        "Portuguesa": {"id": "P005", "descricao": "Presunto, ovos, cebola, pimentão"},
                        "Frango com Requeijão": {"id": "P006", "descricao": "Frango desfiado com requeijão"}
                    }
                },
                "massa": {
                    "nome": "Escolha o tipo de massa",
                    "opcoes": {
                        "Pan Pizza": {"id": "PAN", "descricao": "Massa pan tradicional"},
                        "Thin & Crispy": {"id": "THIN", "descricao": "Massa fina e crocante"}
                    }
                }
            },
            "categoria": "pizza"
        },
        "PIZZA MEDIA": {
            "nome_completo": "Pizza Média",
            "descricao": "Pizza média 8 fatias",
            "preco": 69.90,
            "sku": "PM001",
            "atributos_requeridos": {
                "sabor": {
                    "nome": "Escolha o sabor",
                    "opcoes": {
                        "Mussarela": {"id": "P001", "descricao": "Pizza clássica de mussarela"},
                        "Calabresa": {"id": "P002", "descricao": "Calabresa com cebola"},
                        "Marguerita": {"id": "P003", "descricao": "Molho, mussarela, tomate e manjericão"},
                        "Pepperoni": {"id": "P004", "descricao": "Pepperoni clássico"},
                        "Portuguesa": {"id": "P005", "descricao": "Presunto, ovos, cebola, pimentão"},
                        "Frango com Requeijão": {"id": "P006", "descricao": "Frango desfiado com requeijão"},
                        "Supreme": {"id": "P007", "descricao": "Pepperoni, presunto, pimentão, cogumelos"},
                        "Meat Lovers": {"id": "P008", "descricao": "Pepperoni, calabresa, presunto, bacon"},
                        "Cheese Lovers": {"id": "P009", "descricao": "4 queijos deliciosos"}
                    }
                },
                "massa": {
                    "nome": "Escolha o tipo de massa",
                    "opcoes": {
                        "Pan Pizza": {"id": "PAN", "descricao": "Massa pan tradicional"},
                        "Thin & Crispy": {"id": "THIN", "descricao": "Massa fina e crocante"}
                    }
                },
                "borda": {
                    "nome": "Adicionar borda recheada? (opcional)",
                    "opcoes": {
                        "Sem Borda": {"id": "NOBORDA", "descricao": "Sem borda recheada"},
                        "Borda de Requeijão": {"id": "BORDAREQ", "descricao": "Borda recheada com requeijão (+R$ 12,90)"},
                        "Borda de Cheddar": {"id": "BORDACHED", "descricao": "Borda recheada com cheddar (+R$ 12,90)"},
                        "Cheesy Pop": {"id": "BORDACHEESY", "descricao": "Borda com bolinhas de queijo (+R$ 15,90)"}
                    }
                }
            },
            "categoria": "pizza"
        },
        "PIZZA GRANDE": {
            "nome_completo": "Pizza Grande",
            "descricao": "Pizza grande 12 fatias",
            "preco": 79.90,
            "sku": "PG001",
            "atributos_requeridos": {
                "sabor": {
                    "nome": "Escolha o sabor",
                    "opcoes": {
                        "Mussarela": {"id": "P001", "descricao": "Pizza clássica de mussarela"},
                        "Calabresa": {"id": "P002", "descricao": "Calabresa com cebola"},
                        "Marguerita": {"id": "P003", "descricao": "Molho, mussarela, tomate e manjericão"},
                        "Pepperoni": {"id": "P004", "descricao": "Pepperoni clássico"},
                        "Portuguesa": {"id": "P005", "descricao": "Presunto, ovos, cebola, pimentão"},
                        "Frango com Requeijão": {"id": "P006", "descricao": "Frango desfiado com requeijão"},
                        "Supreme": {"id": "P007", "descricao": "Pepperoni, presunto, pimentão, cogumelos"},
                        "Meat Lovers": {"id": "P008", "descricao": "Pepperoni, calabresa, presunto, bacon"},
                        "Cheese Lovers": {"id": "P009", "descricao": "4 queijos deliciosos"}
                    }
                },
                "massa": {
                    "nome": "Escolha o tipo de massa",
                    "opcoes": {
                        "Pan Pizza": {"id": "PAN", "descricao": "Massa pan tradicional"},
                        "Thin & Crispy": {"id": "THIN", "descricao": "Massa fina e crocante"}
                    }
                },
                "borda": {
                    "nome": "Adicionar borda recheada? (opcional)",
                    "opcoes": {
                        "Sem Borda": {"id": "NOBORDA", "descricao": "Sem borda recheada"},
                        "Borda de Requeijão": {"id": "BORDAREQ", "descricao": "Borda recheada com requeijão (+R$ 12,90)"},
                        "Borda de Cheddar": {"id": "BORDACHED", "descricao": "Borda recheada com cheddar (+R$ 12,90)"},
                        "Cheesy Pop": {"id": "BORDACHEESY", "descricao": "Borda com bolinhas de queijo (+R$ 15,90)"}
                    }
                }
            },
            "categoria": "pizza"
        }
    },
    "ENTRADAS": {
        "CHEESY POPS": {
            "nome_completo": "Cheesy Pops",
            "descricao": "8 unidades de bolinhas de queijo assadas",
            "preco": 19.90,
            "sku": "CP001",
            "atributos_requeridos": {},
            "categoria": "entrada"
        },
        "BATATA COUNTRY": {
            "nome_completo": "Batata Country",
            "descricao": "Porção de batata country crocante",
            "preco": 17.90,
            "sku": "BC001",
            "atributos_requeridos": {},
            "categoria": "entrada"
        },
        "BREADSTICKS": {
            "nome_completo": "Breadsticks",
            "descricao": "Palitos de massa com queijo",
            "preco": 22.90,
            "sku": "BS001",
            "atributos_requeridos": {},
            "categoria": "entrada"
        }
    },
    "SOBREMESAS": {
        "PIZZA DE BRIGADEIRO": {
            "nome_completo": "Pizza de Brigadeiro",
            "descricao": "Pizza doce individual de brigadeiro",
            "preco": 24.90,
            "sku": "PB001",
            "atributos_requeridos": {},
            "categoria": "sobremesa"
        },
        "HUT CUP": {
            "nome_completo": "Hut Cup",
            "descricao": "Sorvete cremoso",
            "preco": 12.90,
            "sku": "HC001",
            "atributos_requeridos": {
                "sabor": {
                    "nome": "Escolha o sabor",
                    "opcoes": {
                        "Baunilha": {"id": "SB001", "descricao": "Sorvete de baunilha"},
                        "Chocolate": {"id": "SC001", "descricao": "Sorvete de chocolate"},
                        "Morango": {"id": "SM001", "descricao": "Sorvete de morango"}
                    }
                }
            },
            "categoria": "sobremesa"
        },
        "CHURROS": {
            "nome_completo": "Churros com Doce de Leite",
            "descricao": "4 unidades de churros com doce de leite",
            "preco": 15.90,
            "sku": "CH001",
            "atributos_requeridos": {},
            "categoria": "sobremesa"
        }
    },
    "BEBIDAS": {
        "REFRIGERANTE LATA": {
            "nome_completo": "Refrigerante Lata",
            "descricao": "Refrigerante 350ml",
            "preco": 8.90,
            "sku": "RL001",
            "atributos_requeridos": {
                "sabor": {
                    "nome": "Escolha o sabor",
                    "opcoes": {
                        "Coca-Cola": {"id": "CC350", "descricao": "Coca-Cola 350ml"},
                        "Guaraná Antártica": {"id": "GA350", "descricao": "Guaraná Antártica 350ml"},
                        "Fanta Laranja": {"id": "FL350", "descricao": "Fanta Laranja 350ml"}
                    }
                }
            },
            "categoria": "bebida"
        },
        "REFRIGERANTE 2L": {
            "nome_completo": "Refrigerante 2 Litros",
            "descricao": "Refrigerante 2 litros",
            "preco": 14.90,
            "sku": "R2L001",
            "atributos_requeridos": {
                "sabor": {
                    "nome": "Escolha o sabor",
                    "opcoes": {
                        "Coca-Cola": {"id": "CC2000", "descricao": "Coca-Cola 2 litros"},
                        "Guaraná Antártica": {"id": "GA2000", "descricao": "Guaraná Antártica 2 litros"},
                        "Fanta Laranja": {"id": "FL2000", "descricao": "Fanta Laranja 2 litros"}
                    }
                }
            },
            "categoria": "bebida"
        },
        "AGUA MINERAL": {
            "nome_completo": "Água Mineral",
            "descricao": "Água mineral 500ml",
            "preco": 5.90,
            "sku": "AM001",
            "atributos_requeridos": {},
            "categoria": "bebida"
        }
    }
}

# Variáveis globais para armazenar pedidos em construção e seleções pendentes
pedidos_em_processo = {}
selecoes_pendentes = {}


def consultar_cardapio_pizzahut_tool(categoria: Optional[str] = None) -> Dict[str, Any]:
    """
    Consultar o cardápio completo da Pizza Hut ou por categoria específica.

    Args:
        categoria: Categoria específica (COMBOS, PIZZAS, ENTRADAS, SOBREMESAS, BEBIDAS)

    Returns:
        Informações do cardápio Pizza Hut
    """
    logger.info(f"Consultando cardápio Pizza Hut - categoria: {categoria}")
    
    if categoria and categoria.upper() in PIZZAHUT_MENU:
        return {
            "categoria": categoria.upper(),
            "produtos": PIZZAHUT_MENU[categoria.upper()],
            "mensagem": f"Aqui estão os produtos de {categoria.replace('_', ' ').title()}"
        }
    
    return {
        "cardapio_completo": PIZZAHUT_MENU,
        "categorias": ["COMBOS", "PIZZAS", "ENTRADAS", "SOBREMESAS", "BEBIDAS"],
        "mensagem": "Bem-vindo à Pizza Hut! Estas são nossas promoções e produtos especiais"
    }


def iniciar_selecao_produto_tool(session_id: str, nome_produto: str) -> Dict[str, Any]:
    """
    Iniciar o processo de seleção de um produto Pizza Hut com seus atributos.

    Args:
        session_id: ID da sessão do cliente
        nome_produto: Nome do produto Pizza Hut a configurar

    Returns:
        Primeira pergunta sobre atributos ou confirmação se não requer atributos
    """
    logger.info(f"Iniciando seleção de produto - Session: {session_id}, Produto: {nome_produto}")
    
    # Normalizar o nome do produto para busca (remover acentos e converter para maiúsculo)
    def normalizar_texto(texto: str) -> str:
        """Remove acentos e converte para maiúsculo para comparação"""
        import unicodedata
        texto_normalizado = unicodedata.normalize('NFD', texto)
        texto_sem_acentos = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
        return texto_sem_acentos.upper().strip()
    
    nome_normalizado = normalizar_texto(nome_produto)
    
    # Buscar o produto no cardápio
    produto_encontrado = None
    categoria_produto = None
    chave_produto = None
    
    # Primeiro tenta busca exata
    for categoria, produtos in PIZZAHUT_MENU.items():
        if nome_produto in produtos:
            produto_encontrado = produtos[nome_produto]
            categoria_produto = categoria
            chave_produto = nome_produto
            break
    
    # Se não encontrou, tenta busca normalizada
    if not produto_encontrado:
        for categoria, produtos in PIZZAHUT_MENU.items():
            for chave, produto_data in produtos.items():
                if (normalizar_texto(chave) == nome_normalizado or 
                    normalizar_texto(produto_data.get("nome_completo", "")) == nome_normalizado):
                    produto_encontrado = produto_data
                    categoria_produto = categoria
                    chave_produto = chave
                    break
            if produto_encontrado:
                break
    
    if not produto_encontrado:
        # Tentar busca parcial mais flexível
        for categoria, produtos in PIZZAHUT_MENU.items():
            for chave, produto_data in produtos.items():
                chave_norm = normalizar_texto(chave)
                nome_completo_norm = normalizar_texto(produto_data.get("nome_completo", ""))
                
                if (nome_normalizado in chave_norm or 
                    nome_normalizado in nome_completo_norm or
                    chave_norm in nome_normalizado):
                    produto_encontrado = produto_data
                    categoria_produto = categoria
                    chave_produto = chave
                    break
            if produto_encontrado:
                break
    
    if not produto_encontrado:
        # Listar produtos similares para ajudar o usuário
        sugestoes = []
        for categoria, produtos in PIZZAHUT_MENU.items():
            for chave, produto_data in produtos.items():
                sugestoes.append(f"• {produto_data.get('nome_completo', chave)}")
        
        return {
            "error": f"Produto '{nome_produto}' não encontrado no cardápio Pizza Hut",
            "sugestoes": sugestoes[:10],  # Limitar a 10 sugestões
            "mensagem": f"Não consegui encontrar '{nome_produto}'. Veja algumas opções disponíveis:"
        }
    
    # Inicializar seleção pendente
    if session_id not in selecoes_pendentes:
        selecoes_pendentes[session_id] = {}
    
    selecoes_pendentes[session_id] = {
        "produto": chave_produto,  # Usar a chave correta do produto
        "categoria": categoria_produto,
        "atributos_selecionados": {},
        "atributos_pendentes": list(produto_encontrado.get("atributos_requeridos", {}).keys()),
        "preco": produto_encontrado["preco"],
        "sku": produto_encontrado["sku"]
    }
    
    # Se não requer atributos, adicionar diretamente
    if not produto_encontrado.get("atributos_requeridos"):
        return adicionar_produto_finalizado_tool(session_id)
    
    # Obter primeiro atributo pendente
    primeiro_atributo = selecoes_pendentes[session_id]["atributos_pendentes"][0]
    atributo_info = produto_encontrado["atributos_requeridos"][primeiro_atributo]
    
    opcoes_texto = []
    for opcao, dados in atributo_info["opcoes"].items():
        opcoes_texto.append(f"• {opcao}: {dados['descricao']}")
    
    return {
        "produto": produto_encontrado.get("nome_completo", chave_produto),
        "categoria": categoria_produto,
        "preco": produto_encontrado["preco"],
        "atributo_atual": primeiro_atributo,
        "pergunta": atributo_info["nome"],
        "opcoes": list(atributo_info["opcoes"].keys()),
        "opcoes_detalhes": opcoes_texto,
        "mensagem": f"Perfeito! Você escolheu {produto_encontrado.get('nome_completo', chave_produto)} por R$ {produto_encontrado['preco']:.2f}. Agora preciso que escolha: {atributo_info['nome']}"
    }


def selecionar_atributo_tool(session_id: str, atributo: str, valor: str) -> Dict[str, Any]:
    """
    Selecionar um valor para um atributo do produto em configuração.

    Args:
        session_id: ID da sessão do cliente
        atributo: Nome do atributo (sabor, massa, borda, bebida)
        valor: Valor selecionado para o atributo

    Returns:
        Próxima pergunta de atributo ou confirmação final
    """
    logger.info(f"Selecionando atributo - Session: {session_id}, Atributo: {atributo}, Valor: {valor}")
    
    if session_id not in selecoes_pendentes:
        return {"error": "Não há produto em seleção. Primeiro escolha um produto."}
    
    selecao = selecoes_pendentes[session_id]
    produto_info = PIZZAHUT_MENU[selecao["categoria"]][selecao["produto"]]
    
    # Validar que o atributo existe e o valor é válido
    if atributo not in produto_info.get("atributos_requeridos", {}):
        return {"error": f"Atributo '{atributo}' não válido para este produto"}
    
    opcoes_validas = produto_info["atributos_requeridos"][atributo]["opcoes"]
    if valor not in opcoes_validas:
        return {"error": f"Opção '{valor}' não válida para {atributo}"}
    
    # Guardar seleção
    selecao["atributos_selecionados"][atributo] = valor
    
    # Remover dos pendentes
    if atributo in selecao["atributos_pendentes"]:
        selecao["atributos_pendentes"].remove(atributo)
    
    # Se restam atributos pendentes, perguntar o próximo
    if selecao["atributos_pendentes"]:
        proximo_atributo = selecao["atributos_pendentes"][0]
        atributo_info = produto_info["atributos_requeridos"][proximo_atributo]
        
        opcoes_texto = []
        for opcao, dados in atributo_info["opcoes"].items():
            opcoes_texto.append(f"• {opcao}: {dados['descricao']}")
        
        return {
            "atributo_salvo": f"{atributo}: {valor}",
            "atributo_atual": proximo_atributo,
            "pergunta": atributo_info["nome"],
            "opcoes": list(atributo_info["opcoes"].keys()),
            "opcoes_detalhes": opcoes_texto,
            "mensagem": f"Excelente! Você escolheu {valor}. Agora: {atributo_info['nome']}"
        }
    
    # Todos os atributos completados, adicionar ao pedido
    return adicionar_produto_finalizado_tool(session_id)


def adicionar_produto_finalizado_tool(session_id: str) -> Dict[str, Any]:
    """
    Adicionar o produto completamente configurado ao pedido.

    Args:
        session_id: ID da sessão do cliente

    Returns:
        Confirmação do produto adicionado ao pedido
    """
    logger.info(f"Finalizando adição de produto - Session: {session_id}")
    
    if session_id not in selecoes_pendentes:
        return {"error": "Não há produto configurado para adicionar"}
    
    selecao = selecoes_pendentes[session_id]
    
    # Inicializar pedido se não existe
    if session_id not in pedidos_em_processo:
        pedidos_em_processo[session_id] = {
            "items": [],
            "total": 0.0
        }
    
    # Criar nome completo do produto com atributos
    nome_completo = selecao["produto"]
    if selecao["atributos_selecionados"]:
        detalhes = []
        for atributo, valor in selecao["atributos_selecionados"].items():
            detalhes.append(f"{valor}")
        nome_completo += f" ({', '.join(detalhes)})"
    
    # Adicionar ao pedido
    novo_item = {
        "produto": nome_completo,
        "produto_base": selecao["produto"],
        "atributos": selecao["atributos_selecionados"],
        "quantidade": 1,
        "preco_unitario": selecao["preco"],
        "subtotal": selecao["preco"],
        "sku": selecao["sku"],
        "categoria": selecao["categoria"]
    }
    
    pedidos_em_processo[session_id]["items"].append(novo_item)
    
    # Recalcular total
    pedidos_em_processo[session_id]["total"] = sum(
        item["subtotal"] for item in pedidos_em_processo[session_id]["items"]
    )
    
    # Limpar seleção pendente
    del selecoes_pendentes[session_id]
    
    return {
        "item_adicionado": novo_item,
        "pedido_atual": pedidos_em_processo[session_id],
        "mensagem": f"Perfeito! Adicionei {nome_completo} por R$ {selecao['preco']:.2f} ao seu pedido."
    }


def consultar_pedido_atual_tool(session_id: str) -> Dict[str, Any]:
    """
    Consultar o estado atual do pedido em construção.

    Args:
        session_id: ID da sessão do cliente

    Returns:
        Estado atual do pedido
    """
    logger.info(f"Consultando pedido atual - Session: {session_id}")
    
    if session_id not in pedidos_em_processo:
        return {
            "pedido_vazio": True,
            "mensagem": "Você não tem produtos no seu pedido atual"
        }
    
    pedido = pedidos_em_processo[session_id]
    
    # Formatar resumo do pedido
    resumo_items = []
    for item in pedido["items"]:
        resumo_items.append(f"• {item['produto']} - R$ {item['subtotal']:.2f}")
    
    return {
        "pedido_vazio": False,
        "pedido": pedido,
        "resumo": resumo_items,
        "total_formatado": f"R$ {pedido['total']:.2f}",
        "quantidade_items": len(pedido["items"]),
        "mensagem": f"Seu pedido atual tem {len(pedido['items'])} produtos por um total de R$ {pedido['total']:.2f}"
    }


def sugerir_complementos_pizzahut_tool(produtos_atuais: List[str]) -> Dict[str, Any]:
    """
    Sugerir produtos adicionais baseados no pedido atual.

    Args:
        produtos_atuais: Lista de produtos já no pedido

    Returns:
        Sugestões de produtos adicionais
    """
    logger.info(f"Gerando sugestões Pizza Hut para produtos: {produtos_atuais}")
    
    tem_pizza = any("PIZZA" in prod for prod in produtos_atuais)
    tem_combo = any("COMBO" in prod or "MY BOX" in prod or "DUPLA" in prod for prod in produtos_atuais)
    
    sugestoes = []
    
    if tem_pizza and not tem_combo:
        sugestoes.extend([
            "Que tal adicionar nossa famosa borda recheada? Temos opções de requeijão, cheddar e Cheesy Pop!",
            "Para acompanhar, recomendo nossos Cheesy Pops ou Batata Country crocante."
        ])
    
    if not tem_pizza and not tem_combo:
        sugestoes.extend([
            "Recomendo nosso My Box Individual por R$ 35,90 - pizza + acompanhamento + bebida!",
            "Nossa Dupla Imbatível por R$ 99,90 é perfeita para compartilhar - 2 pizzas grandes!"
        ])
    
    if len(produtos_atuais) == 0:
        sugestoes.extend([
            "Bem-vindo à Pizza Hut! Recomendo começar com nossos combos especiais.",
            "Que tal experimentar nossa Pizza Grande com borda Cheesy Pop? É a favorita dos clientes!"
        ])
    
    # Sempre sugerir sobremesas e bebidas
    if not any("HUT CUP" in prod or "BRIGADEIRO" in prod or "CHURROS" in prod for prod in produtos_atuais):
        sugestoes.append("Para finalizar, temos deliciosas sobremesas como Pizza de Brigadeiro e Hut Cup!")
    
    if not any("REFRIGERANTE" in prod or "AGUA" in prod for prod in produtos_atuais):
        sugestoes.append("Não esqueça da bebida! Temos refrigerantes e água mineral geladinha.")
    
    return {
        "tem_pizza": tem_pizza,
        "tem_combo": tem_combo,
        "sugestoes": sugestoes,
        "mensagem": "Gostaria de adicionar algo mais ao seu pedido Pizza Hut?"
    }


def finalizar_pedido_pizzahut_tool(session_id: str) -> Dict[str, Any]:
    """
    Finalizar o pedido Pizza Hut e preparar os dados para processar.

    Args:
        session_id: ID da sessão do cliente

    Returns:
        Dados do pedido para processar
    """
    logger.info(f"Finalizando pedido Pizza Hut - Session: {session_id}")
    
    if session_id not in pedidos_em_processo:
        return {
            "error": "Não há pedido para finalizar",
            "mensagem": "Primeiro você precisa adicionar produtos ao seu pedido"
        }
    
    pedido = pedidos_em_processo[session_id]
    
    if not pedido["items"]:
        return {
            "error": "Pedido vazio",
            "mensagem": "Não há produtos no pedido para finalizar"
        }
    
    # Preparar orderItems para finalizeOrder
    order_items = []
    for item in pedido["items"]:
        order_items.append({
            "productName": item["produto"],
            "productBase": item["produto_base"],
            "attributes": item.get("atributos", {}),
            "quantity": item["quantidade"],
            "sku": item.get("sku", ""),
            "unitPrice": item["preco_unitario"]
        })
    
    # Limpar o pedido depois de finalizar
    del pedidos_em_processo[session_id]
    
    return {
        "success": True,
        "orderItems": order_items,
        "total": pedido["total"],
        "resumo_pedido": pedido,
        "mensagem": "Pedido Pizza Hut pronto para processar"
    }


def remover_item_pedido_tool(session_id: str, indice_item: int) -> Dict[str, Any]:
    """
    Remover um item específico do pedido pelo índice.

    Args:
        session_id: ID da sessão do cliente
        indice_item: Índice do item a ser removido (baseado em 1, não 0)

    Returns:
        Confirmação da remoção do item
    """
    logger.info(f"Removendo item {indice_item} do pedido Pizza Hut - Session: {session_id}")
    
    if session_id not in pedidos_em_processo:
        return {
            "error": "Não há pedido ativo para remover itens",
            "mensagem": "Você não tem produtos no seu pedido para remover"
        }
    
    pedido = pedidos_em_processo[session_id]
    
    if not pedido["items"] or len(pedido["items"]) == 0:
        return {
            "error": "Pedido vazio",
            "mensagem": "Não há produtos no pedido para remover"
        }
    
    # Converter índice de 1-based para 0-based
    indice_real = indice_item - 1
    
    if indice_real < 0 or indice_real >= len(pedido["items"]):
        return {
            "error": "Índice inválido",
            "mensagem": f"Item {indice_item} não existe no pedido. Você tem {len(pedido['items'])} itens."
        }
    
    # Remover o item específico
    item_removido = pedido["items"].pop(indice_real)
    
    # Recalcular total
    pedido["total"] = sum(item["subtotal"] for item in pedido["items"])
    
    return {
        "success": True,
        "item_removido": item_removido,
        "pedido_atual": pedido,
        "mensagem": f"Removido: {item_removido['produto']}. Restam {len(pedido['items'])} itens no pedido."
    }


def limpar_pedido_tool(session_id: str) -> Dict[str, Any]:
    """
    Limpar/cancelar o pedido atual e seleções pendentes completamente.

    Args:
        session_id: ID da sessão do cliente

    Returns:
        Confirmação da limpeza
    """
    logger.info(f"Limpando pedido Pizza Hut completamente - Session: {session_id}")
    
    # Limpar pedido
    pedido_limpo = False
    if session_id in pedidos_em_processo:
        del pedidos_em_processo[session_id]
        pedido_limpo = True
    
    # Limpar seleções pendentes
    selecao_limpa = False
    if session_id in selecoes_pendentes:
        del selecoes_pendentes[session_id]
        selecao_limpa = True
    
    if pedido_limpo or selecao_limpa:
        return {"success": True, "mensagem": "Seu pedido foi cancelado completamente"}
    
    return {"success": True, "mensagem": "Não havia pedido para cancelar"}


def calcular_preco_produtos_pizzahut_tool(produtos: List[str]) -> Dict[str, Any]:
    """
    Calcular o preço total de uma lista de produtos Pizza Hut.

    Args:
        produtos: Lista de nomes de produtos

    Returns:
        Cálculo de preços individuais e total
    """
    logger.info(f"Calculando preços Pizza Hut para produtos: {produtos}")
    
    resultados = []
    total = 0.0
    
    for produto in produtos:
        preco = None
        categoria_encontrada = None
        sku = None
        
        for categoria, items in PIZZAHUT_MENU.items():
            if produto in items:
                preco = items[produto]["preco"]
                categoria_encontrada = categoria
                sku = items[produto]["sku"]
                break
        
        if preco is not None:
            resultados.append({
                "produto": produto,
                "categoria": categoria_encontrada,
                "preco": preco,
                "sku": sku,
                "preco_formatado": f"R$ {preco:.2f}"
            })
            total += preco
        else:
            resultados.append({
                "produto": produto,
                "error": "Produto não encontrado no cardápio Pizza Hut"
            })
    
    return {
        "produtos": resultados,
        "total": total,
        "total_formatado": f"R$ {total:.2f}"
    }


def finalize_order_tool(order_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Processar o pedido final da Pizza Hut.

    Args:
        order_items: Lista de items do pedido com formato estendido para Pizza Hut

    Returns:
        Resultado do processamento do pedido
    """
    import random
    import time
    
    logger.info(f"Processando pedido final Pizza Hut com items: {order_items}")
    
    # Validar formato de order_items
    if not isinstance(order_items, list):
        return {
            "status": "ERROR",
            "error": "order_items deve ser uma lista",
            "message": "Formato de pedido inválido"
        }
    
    for item in order_items:
        if not isinstance(item, dict) or "productName" not in item or "quantity" not in item:
            return {
                "status": "ERROR",
                "error": "Cada item deve ter productName e quantity",
                "message": "Formato de item inválido"
            }
    
    # Simular tempo de processamento
    time.sleep(0.5)
    
    # Simular sucesso em 95% dos casos
    if random.random() < 0.95:
        order_id = f"PIZZAHUT-{random.randint(100000, 999999)}"
        total_items = sum(item["quantity"] for item in order_items)
        
        logger.info(f"Pedido Pizza Hut processado com sucesso - ID: {order_id}")
        
        return {
            "status": "SUCCESS",
            "orderId": order_id,
            "message": "Pedido Pizza Hut processado com sucesso!",
            "items": order_items,
            "totalItems": total_items,
            "estimatedTime": "30-40 minutos",
            "restaurant": "Pizza Hut"
        }
    else:
        logger.warning("Simulando erro no processamento de pedido Pizza Hut")
        
        return {
            "status": "ERROR",
            "error": "Erro no sistema de pedidos Pizza Hut",
            "message": "Por favor tente novamente em alguns momentos"
        }
