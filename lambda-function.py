# ============================================
# Lambda Function - Assistente de Delivery
# Conexão entre AWS Step Functions e Bedrock
# ============================================

import json
import boto3
import re
import os
from typing import Dict, Any

# Cliente do Bedrock
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Função Lambda que recebe o pedido do Step Functions
    e invoca o Amazon Bedrock para gerar recomendações
    """
    
    # 1. Extrair dados do evento
    pedido = event.get('pedido', '')
    contexto = event.get('contexto', '')
    
    # Validar entrada
    if not pedido:
        return {
            'statusCode': 400,
            'error': 'Pedido não fornecido'
        }
    
    try:
        # 2. Construir prompt para o Bedrock
        recomendacoes = gerar_recomendacoes(pedido, contexto)
        
        # 3. Retornar resposta formatada
        return {
            'statusCode': 200,
            'pedido': pedido,
            'contexto': contexto,
            'recomendacoes': recomendacoes
        }
        
    except Exception as e:
        # Fallback: recomendações padrão
        return {
            'statusCode': 500,
            'pedido': pedido,
            'contexto': contexto,
            'recomendacoes': {
                'bebida': 'Sugestão personalizada para seu pedido',
                'local': 'Local ideal para sua ocasião',
                'experiencia': 'Experiência complementar especial'
            },
            'error': str(e)
        }


def gerar_recomendacoes(pedido: str, contexto: str) -> Dict[str, str]:
    """
    Gera recomendações usando Amazon Bedrock (Claude 3 Haiku)
    """
    
    # Construir prompt
    prompt = f"""
    Você é um sommelier e especialista em experiências gastronômicas.
    
    O cliente pediu: {pedido}
    Contexto: {contexto if contexto else 'jantar casual'}
    
    Por favor, sugira:
    1. Uma bebida que harmonize perfeitamente com {pedido}
    2. Um local/restaurante ideal para esta ocasião
    3. Uma experiência complementar
    
    Responda APENAS com um JSON válido no formato:
    {{
        "bebida": "Sua sugestão de bebida",
        "local": "Sugestão de local ou restaurante",
        "experiencia": "Experiência complementar sugerida"
    }}
    """
    
    # Invocar modelo Claude 3 Haiku no Bedrock
    response = bedrock_runtime.invoke_model(
        modelId='anthropic.claude-3-haiku-20240307-v1:0',
        contentType='application/json',
        accept='application/json',
        body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': 300,
            'temperature': 0.7,
            'messages': [
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        })
    )
    
    # Processar resposta
    response_body = json.loads(response['body'].read())
    resposta_texto = response_body['content'][0]['text']
    
    # Extrair JSON da resposta
    try:
        # Buscar JSON na resposta
        json_match = re.search(r'\{.*\}', resposta_texto, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            # Fallback
            return {
                'bebida': 'Vinho tinto suave',
                'local': 'Restaurante italiano',
                'experiencia': 'Jantar à luz de velas'
            }
    except:
        return {
            'bebida': 'Vinho tinto suave',
            'local': 'Restaurante italiano',
            'experiencia': 'Jantar à luz de velas'
        }


# ============================================
# Função de teste local (para validação)
# ============================================

if __name__ == '__main__':
    # Teste com exemplo
    test_event = {
        'pedido': 'macarrão',
        'contexto': 'jantar romântico'
    }
    
    resultado = lambda_handler(test_event, None)
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
