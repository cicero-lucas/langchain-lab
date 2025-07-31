✅ O que é LangChain?
LangChain é um framework de código aberto que facilita a criação de aplicações que usam modelos de linguagem (LLMs) como o GPT-4, Claude ou outros, de forma mais estruturada e integrada com dados externos, ferramentas e fluxos complexos.

Ele permite que você crie sistemas como:

Chatbots com memória e contexto.

Agentes inteligentes que interagem com APIs e bancos de dados.

Buscadores inteligentes com RAG (Retrieval-Augmented Generation).

Workflows que combinam múltiplas etapas e LLMs.

🚀 Por que usar o LangChain?
Sem o LangChain, você teria que:

Montar sua lógica de chamada ao LLM na mão.

Criar cache, memória, histórico.

Lidar com ferramentas externas e integrar com vetores manualmente.

Com o LangChain, você pode fazer isso com componentes reutilizáveis e padronizados.

🔧 Componentes principais do LangChain:
Componente	O que faz
LLMs	Interface com modelos como OpenAI, Anthropic, HuggingFace etc.
Chains	Sequência de passos (ex: entrada → prompt → LLM → saída).
Agents	LLMs com autonomia para decidir que ferramentas usar (ex: Google Search).
Tools	Ferramentas que o agent pode usar (ex: calculadora, API, banco de dados).
Retrievers	Mecanismo para buscar informações em base vetorial (RAG).
Memory	Armazena contexto para conversas mais naturais e persistentes.
Embeddings	Vetores que representam significado de textos, usados em busca vetorial.


📚 Aplicações práticas
Chatbots com memória: lembram do que foi dito anteriormente.

Assistentes com plugins (tools): acessam calculadora, pesquisa, etc.

Pesquisa em documentos PDF ou sites: com embeddings + retrievers.

Fluxos empresariais: como atendimento, triagem de dados, resumo de relatórios.

1. Instrução direta (Zero-shot prompting)
Você dá um comando direto ao modelo.

text
Copiar código
Traduza o seguinte texto para inglês: "Eu gosto de programar".
No LangChain (Python):

python
Copiar código
PromptTemplate.from_template("Traduza o seguinte texto para inglês: \"{texto}\"")
2. One-shot / Few-shot prompting
Você dá um ou mais exemplos para o modelo seguir o padrão.

text
Copiar código
Exemplo:
Entrada: O céu está azul.
Saída: O céu está azul. (Português → Português)

Entrada: I am happy.
Saída: Eu estou feliz. (Inglês → Português)

Entrada: He is learning AI.
Saída:
Isso ajuda a dar contexto e formato ao modelo.

3. Chain of Thought (cadeia de raciocínio)
Você orienta o modelo a pensar passo a passo.

text
Copiar código
Pergunta: João tem 3 maçãs e compra mais 5. Quantas ele tem agora?
Vamos pensar passo a passo:
Isso melhora muito a capacidade lógica e matemática da LLM.

4. Prompt com papéis (role prompting)
Você define o papel do modelo para direcionar o estilo da resposta.

text
Copiar código
Você é um professor de história experiente. Explique a Revolução Francesa de forma simples para um aluno do ensino médio.
5. Prompt estruturado com variáveis (LangChain PromptTemplate)
python
Copiar código
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Você é um especialista em {area}. Responda à pergunta: {pergunta}"
)

print(prompt.format(area="medicina", pergunta="O que é diabetes?"))

