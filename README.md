# 🚀 Assistente de Delivery com AWS Step Functions e Bedrock

## 📌 Sobre o Projeto

Assistente inteligente de delivery que utiliza:

- **AWS Step Functions** para orquestrar o fluxo de recomendações
- **Amazon Bedrock** (Claude 3 Haiku) para gerar sugestões personalizadas
- **AWS Lambda** para conectar Step Functions ao Bedrock

## 🎯 Funcionalidades

✅ Captura o pedido do cliente (ex: "macarrão")
✅ Processa com IA via Amazon Bedrock
✅ Gera recomendações de:
- Bebida ideal para harmonização
- Local/restaurante recomendado
- Experiência complementar
✅ Resposta estruturada e personalizada

## 🏗️ Arquitetura

Cliente → Step Functions → Lambda → Bedrock → Resposta


### Componentes:

| Componente | Função |
|------------|--------|
| AWS Step Functions | Orquestrador do fluxo de trabalho |
| AWS Lambda | Conecta Step Functions ao Bedrock |
| Amazon Bedrock | IA generativa (Claude 3 Haiku) |

## 📊 Estrutura do Projeto

assistente-delivery-aws/
├── README.md # Documentação
├── state-machine.asl.json # Definição do Step Functions
└── lambda-function.py # Função Lambda


## 📋 Fluxo de Trabalho

1. **Cliente** faz um pedido (ex: "macarrão")
2. **Step Functions** inicia o fluxo
3. **Lambda** envia o pedido ao Bedrock
4. **Bedrock (Claude 3 Haiku)** processa e gera recomendações
5. **Step Functions** formata a resposta
6. **Cliente** recebe recomendações personalizadas

## 🔧 Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| AWS Step Functions | Orquestração do fluxo |
| Amazon Bedrock | IA Generativa (Claude 3 Haiku) |
| AWS Lambda | Integração entre serviços |
| Python 3.12 | Linguagem da Lambda |

## 📈 Exemplo de Resposta

**Entrada:** `{ "pedido": "macarrão" }`

**Saída:**
```json
{
  "mensagem": "🍽️ Para o seu macarrão, recomendo:\n🍷 Vinho tinto suave (Chianti)\n📍 Restaurante Bella Italia\n🎵 Música ambiente com jazz italiano",
  "detalhes": {
    "pedido": "macarrão",
    "bebida": "Vinho tinto suave (Chianti)",
    "local": "Restaurante Bella Italia",
    "experiencia": "Música ambiente com jazz italiano"
  }
}

🧠 Como Funciona o Step Functions
O Step Functions orquestra o fluxo em etapas:

CapturarPedido → Recebe o pedido do cliente

ProcessarComBedrock → Invoca o Bedrock via Lambda

FiltrarRecomendacoes → Extrai as recomendações do JSON

ApresentarRecomendacoes → Formata a resposta final

🎯 Aprendizados
Orquestração de workflows com AWS Step Functions

Integração com modelos de IA no Amazon Bedrock

Uso de AWS Lambda como conector entre serviços

Definição de máquinas de estado em ASL

👤 Autor
Janilucia Gomes

GitHub: https://github.com/Jhanydev

LinkedIn: linkedin.com/in/janilucia-gomes-82369b2a7

Desenvolvido para o Bootcamp da DIO - Digital Innovation One

