import logging
from google.adk.agents import Agent
from food.tools.prompts import top_level_prompt
from food.tools.tools import (
    consultar_cardapio_pizzahut_tool,
    iniciar_selecao_produto_tool,
    selecionar_atributo_tool,
    adicionar_produto_finalizado_tool,
    consultar_pedido_atual_tool,
    sugerir_complementos_pizzahut_tool,
    finalizar_pedido_pizzahut_tool,
    remover_item_pedido_tool,
    limpar_pedido_tool,
    calcular_preco_produtos_pizzahut_tool,
    finalize_order_tool
)

logger = logging.getLogger(__name__)

root_agent = Agent(
    model="gemini-live-2.5-flash-preview",
    #model="gemini-2.5-flash-preview-native-audio-dialog",
    name="AssistentePizzaHut",
    description="Assistente Pizza Hut - Especialista em pizzas deliciosas e combos irresistíveis",
    instruction=top_level_prompt,
    tools=[
        consultar_cardapio_pizzahut_tool,
        iniciar_selecao_produto_tool,
        selecionar_atributo_tool,
        adicionar_produto_finalizado_tool,
        consultar_pedido_atual_tool,
        sugerir_complementos_pizzahut_tool,
        finalizar_pedido_pizzahut_tool,
        remover_item_pedido_tool,
        limpar_pedido_tool,
        calcular_preco_produtos_pizzahut_tool,
        finalize_order_tool
    ],
)

logger.info(f"Initialized {root_agent.name}")
