# 🏗️ Diagrama de Arquitetura

## Visão Geral
┌─────────────────────────────────────────────────────────────────┐
│ │
│ 1. CLIENTE FAZ PEDIDO │
│ ┌──────────────────────┐ │
│ │ "Quero macarrão" │ │
│ └──────────────────────┘ │
│ │ │
│ ▼ │
│ 2. AWS STEP FUNCTIONS ORQUESTRA │
│ ┌──────────────────────────────────────────┐ │
│ │ CapturarPedido → ProcessarComBedrock │ │
│ │ → FiltrarRecomendacoes → Apresentar │ │
│ └──────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ 3. AWS LAMBDA CONECTA │
│ ┌──────────────────────────────────────────┐ │
│ │ Recebe pedido e invoca o Bedrock │ │
│ └──────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ 4. AMAZON BEDROCK PROCESS COM IA │
│ ┌──────────────────────────────────────────┐ │
│ │ Claude 3 Haiku gera recomendações: │ │
│ │ 🍷 Bebida: Vinho tinto │ │
│ │ 📍 Local: Restaurante Bella Italia │ │
│ │ 🎵 Experiência: Jazz ao vivo │ │
│ └──────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ 5. RESPOSTA FORMATADA │
│ ┌──────────────────────────────────────────┐ │
│ │ Recomendações personalizadas para o │ │
│ │ cliente │ │
│ └──────────────────────────────────────────┘ │
│ │
└─────────────────────────────────────────────────────────────────┘


## Componentes em Detalhe

### AWS Step Functions


ETAPA 1: CapturarPedido
├── Type: Pass
├── Função: Recebe o pedido do cliente
└── Saída: { pedido, contexto, timestamp }

ETAPA 2: ProcessarComBedrock
├── Type: Task (Lambda)
├── Função: Invoca Lambda para processar com IA
└── Saída: { resposta_bruta }

ETAPA 3: FiltrarRecomendacoes
├── Type: Pass
├── Função: Extrai recomendações do JSON
└── Saída: { bebida, local, experiencia }

ETAPA 4: ApresentarRecomendacoes
├── Type: Pass
├── Função: Formata resposta final
└── Saída: { mensagem, detalhes }


### AWS Lambda

```python
Lambda Function
├── Input: { pedido, contexto }
├── Processamento:
│   ├── Conecta ao Bedrock
│   ├── Invoca Claude 3 Haiku
│   └── Extrai recomendações
└── Output: { recomendacoes }

Amazon Bedrock
text
Modelo: Claude 3 Haiku
├── Prompt: Especialista gastronômico
├── Temperatura: 0.7
├── Tokens: 300
└── Saída: JSON com recomendações
Fluxo de Dados
text
Cliente
   │
   ▼
Step Functions
   │
   ▼
Lambda
   │
   ▼
Bedrock (Claude 3 Haiku)
   │
   ▼
Lambda (resposta processada)
   │
   ▼
Step Functions (formatação)
   │
   ▼
Cliente (resposta final)
Exemplo Completo
Entrada
json
{
  "pedido": "macarrão",
  "contexto": "jantar romântico"
}
Processamento
text
1. CapturarPedido: { pedido: "macarrão", contexto: "jantar romântico" }
2. Lambda: Invoca Bedrock com prompt especializado
3. Bedrock: Claude 3 Haiku gera recomendações
4. Filtragem: Extrai { bebida, local, experiencia }
5. Formatação: Cria mensagem amigável
Saída
json
{
  "mensagem": "🍽️ Para o seu macarrão, tenho algumas recomendações especiais:\n\n🍷 Vinho tinto suave (Chianti)\n📍 Restaurante Bella Italia - jantar romântico\n🎵 Música ambiente com jazz italiano",
  "detalhes": {
    "pedido": "macarrão",
    "contexto": "jantar romântico",
    "bebida": "Vinho tinto suave (Chianti)",
    "local": "Restaurante Bella Italia - jantar romântico",
    "experiencia": "Música ambiente com jazz italiano"
  }
}
Boas Práticas
✅ Step Functions:

Estados bem definidos

Tratamento de erros

Logging habilitado

✅ Lambda:

Timeout configurado

Memória adequada

Fallback para erros

✅ Bedrock:

Prompt engineering

Temperatura controlada

Tokens limitados
