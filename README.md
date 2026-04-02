# 🍕 Pizza Hut Live Agent - Assistente Pizza Hut

Um agente de atendimento ao cliente impulsionado por IA para a **Pizza Hut**, com o **Assistente Pizza Hut** - um assistente virtual especializado que ajuda os clientes a fazerem seus pedidos de pizzas e combos de maneira interativa e em português.

## 🌟 Características

### 🎯 Assistente Conversacional Pizza Hut
- **Assistente Pizza Hut** - Especialista em pizzas artesanais e massas exclusivas
- Conversação em **português (pt-BR)** com foco na experiência Pizza Hut
- Sugestões proativas de combos (My Box, Dupla Imbatível) e upselling
- Manejo inteligente de seleção de atributos (sabores, massas, bordas)

### 🍕 Sistema de Pedidos Pizza Hut
- Cardápio interativo completo com **Pizzas, Combos, Entradas e Sobremesas**
- **Produtos Reais**: My Box, Dupla Imbatível, Combo Família
- **Atributos Complexos**: Sabores (Mussarela, Pepperoni, Supreme, etc.), Massas (Pan, Thin & Crispy), Bordas (Requeijão, Cheddar, Cheesy Pop)
- Preços em **reais (R$)** com ofertas especiais
- Gestão de pedidos em tempo real com SKUs

### 🎨 Interface de Usuário Pizza Hut
- **Branding oficial Pizza Hut**: Cores vermelho e branco, design temático
- **Layout de 3 colunas**: Cardápio | Chat | Pedido Atual
- Design temático com elementos visuais atraivos
- Cardápio clicável que pré-preenche o campo de texto
- Atualização em tempo real do pedido e total acumulado

### 🔊 Capacidades Avançadas
- **Chat de texto** com respostas em streaming
- **Suporte de voz** bidirecional em português (voz "Leda")
- **WebSocket** para comunicação em tempo real de baixa latência
- **API REST** para gestão de sessões e pedidos
- **Fluxo conversacional inteligente** para configuração de produtos

## 🚀 Implantação no Cloud Run

### Implantação com Um Único Comando
```bash
# Tornar o script executável
chmod +x deploy.sh

# Implantar no Google Cloud Run
./deploy.sh
```

O script automaticamente:
- ✅ Valida seu arquivo `.env` com `GOOGLE_API_KEY`
- ✅ Autentica no Google Cloud
- ✅ Configura o projeto (se necessário)
- ✅ Habilita as APIs requeridas
- ✅ Implanta com configurações otimizadas (2Gi RAM, 2 CPUs)

### Configuração do Cloud Run
- **Serviço**: `pizzahut-live-agent`
- **Região**: `us-central1`
- **Memória**: 2Gi
- **CPU**: 2 cores
- **Acesso**: Público (sem autenticação)
- **Auto-escalonamento**: 0-10 instâncias

📖 **Guia completo**: Veja [DEPLOYMENT.md](DEPLOYMENT.md)

## 🏃‍♂️ Desenvolvimento Local

### Pré-requisitos
- Python 3.11+
- Chave de API do Google Gemini (ou acesso ao Vertex AI)

### Instalação Local

1. **Clonar o repositório**
```bash
git clone https://github.com/duboc/live-food-agent.git
cd live-food-agent
```

2. **Configurar o ambiente virtual**
```bash
chmod +x setup_venv.sh
./setup_venv.sh
```

3. **Configurar as variáveis de ambiente**
```bash
# Criar arquivo .env com sua API key
echo "GOOGLE_API_KEY=sua_api_key_aqui" > .env
```

4. **Executar a aplicação**
```bash
source venv/bin/activate
cd app
uvicorn main:app --reload
```

5. **Abrir no navegador**
```
http://localhost:8000
```

## 📁 Estrutura do Projeto

```
pizzahut-agent/
├── app/
│   ├── main.py              # Servidor FastAPI e WebSocket
│   ├── food/
│   │   ├── agent.py         # Configuração do Assistente Pizza Hut
│   │   └── tools/
│   │       ├── prompts.py   # Personalidade e estratégias Pizza Hut
│   │       └── tools.py     # Sistema de cardápio e pedidos Pizza Hut
│   └── static/
│       ├── index.html       # Interface Pizza Hut com 3 colunas
│       └── js/
│           └── app.js       # Lógica do cliente WebSocket
├── Dockerfile               # Configuração para Cloud Run
├── deploy.sh               # Script de implantação automatizada
├── requirements.txt        # Dependências de Python
└── README.md              # Este arquivo
```

## 🍕 Cardápio Pizza Hut Disponível

### 📦 Combos e Promoções
- **My Box Individual** - R$ 35,90 (Pizza/Melt + Acompanhamento + Bebida)
- **Dupla Imbatível** - R$ 99,90 (2 Pizzas Grandes)
- **Combo Família** - R$ 159,90 (2 Pizzas Grandes + Entrada + Refri 2L)

### 🍕 Pizzas (Grande/Média/Individual)
- **Sabores Tradicionais**: Mussarela, Calabresa, Marguerita
- **Sabores Especiais**: Pepperoni, Portuguesa, Frango com Requeijão
- **Hut Lovers**: Supreme, Meat Lovers, Cheese Lovers

### 🎯 Opções de Personalização
- **Massas**: Pan Pizza (fofinha), Thin & Crispy (fina e crocante)
- **Bordas Recheadas**: Requeijão, Cheddar (+R$ 12,90), Cheesy Pop (+R$ 15,90)
- **Acompanhamentos**: Cheesy Pops, Batata Country, Breadsticks
- **Sobremesas**: Pizza de Brigadeiro, Hut Cup, Churros

## 🛠️ Ferramentas do Sistema

O Assistente Pizza Hut utiliza as seguintes ferramentas especializadas:

1. **consultar_cardapio_pizzahut_tool** - Mostra o cardápio disponível
2. **iniciar_selecao_produto_tool** - Inicia configuração de um produto
3. **selecionar_atributo_tool** - Gerencia seleção de sabor/massa/borda/bebida
4. **adicionar_produto_finalizado_tool** - Adiciona produto configurado ao pedido
5. **consultar_pedido_actual_tool** - Verifica o pedido atual do cliente
6. **sugerir_complementos_pizzahut_tool** - Sugere upsell baseado no pedido
7. **finalizar_pedido_pizzahut_tool** - Prepara o pedido para processamento
8. **finalize_order_tool** - Processa o pedido final no sistema
9. **remover_item_pedido_tool** - Remove um item específico do pedido
10. **limpar_pedido_tool** - Cancela o pedido atual completamente

## 💬 Exemplos de Uso

### Fluxo típico de conversação:
```
Usuário: "Oi"
Assistente Pizza Hut: "Pizza Hut, boa noite! Qual o seu pedido?"

Usuário: "Quero uma My Box"
Assistente Pizza Hut: "Excelente escolha! Você prefere a Pizza Individual ou o Melt?"

Usuário: "Pizza de Pepperoni"
Assistente Pizza Hut: "Perfeito! E qual o tipo de massa: Pan ou Thin & Crispy?"

Usuário: "Massa Pan"
Assistente Pizza Hut: "Certo! Qual acompanhamento: Batata Country ou Cheesy Pops?"

Usuário: "Batata"
Assistente Pizza Hut: "E para beber, qual refrigerante em lata?"

Usuário: "Coca Cola"
Assistente Pizza Hut: "Pronto! Adicionei sua My Box (Pizza Pepperoni Pan, Batata Country e Coca-Cola) por R$ 35,90."
```

## 🔧 API Endpoints

- `GET /` - Interface web principal
- `WebSocket /ws/{session_id}` - Conexão de chat/voz em tempo real
- `GET /api/pedido/{session_id}` - Obter pedido atual
- `GET /debug/pedidos` - Ver todos os pedidos em processo
- `GET /debug/menu` - Ver cardápio completo (JSON)

## 🎯 Características Técnicas

- **Framework**: FastAPI com WebSocket
- **LLM**: Google Gemini 2.5 Flash Live
- **Áudio**: PCM streaming bidirecional em português
- **Frontend**: HTML5, CSS3, JavaScript Vanilla (sem frameworks pesados)
- **Estado**: In-memory (gerenciado por sessões), escalável
- **Implantação**: Docker em Google Cloud Run com auto-escalonamento

## 🤝 Contribuições

Contribuições são bem-vindas. Por favor:
1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingPizzaFeature`)
3. Commit seus detalhes (`git commit -m 'Add some Pizza Hut feature'`)
4. Push para a branch (`git push origin feature/AmazingPizzaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a Licença Apache 2.0 - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

Aproveite sua experiência com o **Assistente Pizza Hut**! 🍕✨

**Pronto para implantar?** Execute `./deploy.sh` e tenha seu Assistente Pizza Hut na nuvem em minutos.
