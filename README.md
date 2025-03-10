# AI Chat Interface

Uma interface de chat IA com sistema multi-agente e modelos customizados (Mistral e Gemma).

## Características

- Sistema Multi-Agente com CEO, Analista e Coder
- Chat direto com modelos Mistral e Gemma
- Interface web moderna e responsiva
- Suporte a markdown e formatação de código
- Multilíngue (responde no mesmo idioma da pergunta)

## Requisitos

- Python 3.8 ou superior
- Ollama instalado e configurado
- Modelos Mistral e Gemma baixados no Ollama

## Instalação

```bash
pip install ai-chat-interface
```

## Uso

1. Inicie o serviço Ollama:
```bash
ollama serve
```

2. Inicie a interface de chat:
```bash
ai-chat
```

3. Acesse a interface web em: http://localhost:8000

## Desenvolvimento

Para desenvolver o projeto localmente:

```bash
git clone https://github.com/lulzactive/ai-chat-interface.git
cd ai-chat-interface
pip install -e .
```

## Licença

MIT License

## Autor

lulzactive
