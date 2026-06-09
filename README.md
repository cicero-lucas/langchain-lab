# 🤖 LangChain Lab — AI Chatbot com RAG, Chains e Amazon Bedrock

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-blueviolet?logo=chainlink&logoColor=white)](https://python.langchain.com/)
[![AWS](https://img.shields.io/badge/AWS_Bedrock-Compatible-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/bedrock/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-blue)](https://faiss.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Repositório de estudos e projetos práticos com **LangChain**, explorando os principais conceitos de aplicações LLM modernas: **RAG**, **Chains**, **Memória**, **Embeddings** e integração com **AWS Amazon Bedrock**.

---

## 🏗️ Arquitetura do Projeto Principal — Bubi Chatbot

```
Usuário
   │
   ▼
PromptTemplate  ──►  LLM (Gemini / AWS Bedrock)
                              │
                  ┌───────────┘
                  │
            SequentialChain
           ┌──────┴──────┐
      Chain 1          Chain 2
  (Definição)      (Características)
                  
RAG Pipeline:
  FAQ.txt + produto.csv
       │
  TextLoader + CharacterTextSplitter
       │
  FAISS VectorStore (Embeddings)
       │
  RetrievalQA Chain  ──►  Resposta final
```

---

## ✨ Funcionalidades

| Feature | Descrição |
|--------|-----------|
| 🔗 **LLMChain** | Integração direta com LLMs via PromptTemplate |
| 🔄 **SequentialChain** | Pipelines encadeados com múltiplas chains |
| 🧠 **Memória (ConversationBufferMemory)** | Histórico de conversa persistente |
| 📚 **RAG com FAISS** | Busca vetorial em documentos (FAQ + catálogo de produtos) |
| 🗂️ **Output Parsers** | Saídas estruturadas com Pydantic |
| ☁️ **AWS Bedrock Ready** | Suporte a troca de provider para Amazon Bedrock (Claude, Titan) |

---

## 📁 Estrutura

```
langchain-lab/
├── bedrock_example.py         # ⭐ Bubi Chatbot rodando no AWS Bedrock
├── meu_projeto_langchain/
│   ├── chains.ipynb           # LLMChain e SequentialChain
│   ├── memory.ipynb           # ConversationBufferMemory
│   ├── model.ipynb            # Configuração do LLM
│   ├── promptTemplates.ipynb  # PromptTemplate e few-shot
│   ├── outputParser.ipynb     # Saídas estruturadas com Pydantic
│   └── requirements.txt
├── projeto/
│   ├── dados/
│   │   ├── faq.txt            # Base de conhecimento do chatbot
│   │   └── produto.csv        # Catálogo de produtos
│   ├── notebooks/
│   │   └── bubiChatbot.ipynb  # Projeto principal: chatbot com RAG
│   └── requirements.txt
├── docs/
│   └── documentacao.md        # Conceitos e referências do LangChain
└── .env.example
```

---

## ☁️ AWS Amazon Bedrock Integration

Este projeto foi estruturado para ser **facilmente migrado para Amazon Bedrock**, substituindo o provider do LLM:

```python
# Usando Gemini (padrão do projeto)
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

# Migrando para AWS Bedrock (Claude 3)
from langchain_aws import ChatBedrock
llm = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    region_name="us-east-1"
)
```

> A arquitetura de Chains, RAG e Memória permanece **100% igual** — apenas o provider muda.

Veja o exemplo completo funcionando em [`bedrock_example.py`](./bedrock_example.py):

```bash
python bedrock_example.py
```

```
=== SequentialChain: Análise de Produto ===

Definição:
Mouse Gamer 7200DPI é um mouse de alta precisão com sensor ajustável
de até 7200 DPI e botões programáveis, ideal para jogos competitivos.

Características:
🎯 Mouse Gamer 7200DPI — Precisão Total no Seu Controle
Sensor ajustável, botões programáveis e design ergonômico. R$ 79,90

=== RAG: Atendimento Bubi (base FAQ + produtos) ===

Pergunta: Qual é a garantia dos produtos?
Bubi: Todos os nossos produtos possuem garantia de 1 ano contra defeitos de fabricação.

Pergunta: Me fale sobre o Fone Bluetooth X200.
Bubi: O Fone Bluetooth X200 é um fone sem fio com cancelamento de ruído, por R$ 199,90.
```

**Serviços AWS relevantes neste contexto:**
- **Amazon Bedrock** — LLMs gerenciados (Claude, Titan, Llama)
- **Amazon S3** — armazenamento da base de conhecimento (documentos para RAG)
- **AWS Lambda** — deploy serverless da chain
- **Amazon OpenSearch Serverless** — alternativa ao FAISS em produção

---

## 🚀 Como Executar

**1. Clone o repositório:**
```bash
git clone https://github.com/<seu-usuario>/langchain-lab.git
cd langchain-lab
```

**2. Crie o ambiente virtual e instale as dependências:**
```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r projeto/requirements.txt
```

**3. Configure as variáveis de ambiente:**
```bash
cp .env.example .env
# Edite o .env com suas chaves
```

**4. Execute os notebooks:**
```bash
cd projeto/notebooks
jupyter notebook bubiChatbot.ipynb
```

---

## 🧪 Projeto Principal: Bubi Chatbot

O **Bubi** é um chatbot de atendimento para uma loja de acessórios tech, construído com:

- **SequentialChain** para gerar descrição + título do produto automaticamente
- **RAG com FAISS** indexando FAQ e catálogo de produtos em CSV
- **PromptTemplate** com variáveis parciais para controle de resposta
- Base de dados local (FAQ + CSV) convertida em **vector store** para busca semântica

---

## 📦 Principais Dependências

```
langchain==0.3.27
langchain-google-genai==2.1.8  # provider padrão (Gemini)
langchain-aws                  # Amazon Bedrock (bedrock_example.py)
faiss-cpu==1.11.0
pandas==2.3.1
python-dotenv==1.1.1
```

---

## 🔐 Segurança

- Chaves de API armazenadas em `.env` (nunca commitadas)
- `.gitignore` configurado para ignorar arquivos sensíveis
- `.env.example` como template sem valores reais

---

## 📄 Licença

MIT License — veja [LICENSE](LICENSE) para detalhes.
