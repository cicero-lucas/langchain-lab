"""
Bubi Chatbot — AWS Bedrock Edition
===================================
Mesmo pipeline do bubiChatbot.ipynb, mas usando Amazon Bedrock (Claude 3)
como provider no lugar do Gemini.

Demonstra que a arquitetura LangChain é agnóstica de LLM provider.

Pré-requisitos:
  - AWS CLI configurado com permissão bedrock:InvokeModel
  - Acesso ao modelo habilitado no console do Amazon Bedrock
  - pip install langchain-aws faiss-cpu pandas python-dotenv
"""

import os
import pandas as pd
from dotenv import load_dotenv

from langchain_aws import ChatBedrock
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain, RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings

load_dotenv()

# ── 1. LLM via Amazon Bedrock (Claude 3 Sonnet) ──────────────────────────────

llm = ChatBedrock(
    model_id=os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-sonnet-20240229-v1:0"),
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1"),
    model_kwargs={"max_tokens": 512, "temperature": 0.7},
)

# ── 2. SequentialChain: Definição + Características do Produto ────────────────

prompt_definicao = PromptTemplate.from_template(
    "Explique de forma clara o produto chamado {produto} em até 50 palavras.",
)
chain_definicao = LLMChain(
    llm=llm,
    prompt=prompt_definicao,
    output_key="definicao",
)

prompt_caracteristicas = PromptTemplate.from_template(
    "Crie um título comercial atrativo para o produto {produto}. "
    "Destaque as principais características. Máximo 50 palavras.",
)
chain_caracteristicas = LLMChain(
    llm=llm,
    prompt=prompt_caracteristicas,
    output_key="caracteristicas",
)

pipeline_produto = SequentialChain(
    chains=[chain_definicao, chain_caracteristicas],
    input_variables=["produto"],
    output_variables=["definicao", "caracteristicas"],
    verbose=True,
)

# ── 3. RAG com FAISS — FAQ + Catálogo de Produtos ────────────────────────────

def build_vector_store(faq_path: str, csv_path: str) -> FAISS:
    """Indexa FAQ e catálogo de produtos em um vector store FAISS."""

    # Carrega FAQ
    faq_docs = TextLoader(faq_path, encoding="utf-8").load()

    # Converte CSV de produtos para texto e carrega
    df = pd.read_csv(csv_path)
    produtos_txt = csv_path.replace(".csv", "_temp.txt")
    with open(produtos_txt, "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            f.write(f"{row['nome']}: {row['descricao']}, R$ {row['preco']}\n")
    produto_docs = TextLoader(produtos_txt, encoding="utf-8").load()

    # Divide e indexa
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    docs = splitter.split_documents(faq_docs + produto_docs)

    embeddings = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v1",
        region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1"),
    )
    return FAISS.from_documents(docs, embeddings)


def build_rag_chain(vector_store: FAISS) -> RetrievalQA:
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        chain_type="stuff",
    )


# ── 4. Execução ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    BASE_DIR = os.path.join(os.path.dirname(__file__), "projeto", "dados")
    faq_path = os.path.join(BASE_DIR, "faq.txt")
    csv_path = os.path.join(BASE_DIR, "produto.csv")

    print("\n=== SequentialChain: Análise de Produto ===")
    resultado = pipeline_produto.invoke({"produto": "Mouse Gamer 7200DPI"})
    print(f"\nDefinição:\n{resultado['definicao']}")
    print(f"\nCaracterísticas:\n{resultado['caracteristicas']}")

    print("\n=== RAG: Atendimento Bubi (base FAQ + produtos) ===")
    vector_store = build_vector_store(faq_path, csv_path)
    rag_chain = build_rag_chain(vector_store)

    perguntas = [
        "Qual é a garantia dos produtos?",
        "Quais formas de pagamento vocês aceitam?",
        "Me fale sobre o Fone Bluetooth X200.",
    ]
    for pergunta in perguntas:
        resposta = rag_chain.invoke({"query": pergunta})
        print(f"\nPergunta: {pergunta}")
        print(f"Bubi: {resposta['result']}")
