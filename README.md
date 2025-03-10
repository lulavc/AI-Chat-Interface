# OBS: Essa foi uma primeira versão apenas por curiosidade. A limitação do notebook me impossibilita de explorar modelos mais robustos mas acredito que o conceito em sí ja é de grande valia pra galera testar as fronteiras da linguagem humana que muda com grande influência cultural e a linguagem artificial treinada com modelos distintos que muitas vezes provocam interpretações erradas.

- Mais pra frente pretendo "brincar" com a matemática porque acredito que ela fornece à IA a linguagem fundamental para representar, interpretar e otimizar intenções humanas. Sem esse arcabouço matemático, sistemas de IA teriam dificuldade em:

- Transformar diretivas vagas em objetivos computáveis
- Lidar com ambiguidades e incertezas inerentes à comunicação humana
- Generalizar intenções para contextos novos mas relacionados
- Balancear múltiplos objetivos potencialmente conflitantes

Quanto mais avançamos em sistemas de IA complexos, mais dependemos de estruturas matemáticas sofisticadas para garantir que esses sistemas interpretem corretamente o que desejamos e atuem de acordo com nossos valores e intenções reais.

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
