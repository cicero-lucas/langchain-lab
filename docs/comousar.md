🔧 Passo 1: Instalar o Python

 Passo 3: Criar e ativar um ambiente virtual

Crie uma pasta para o projeto:

No terminal do VS Code, navegue até a pasta onde você quer o projeto e crie uma nova pasta:


# Projeto LangChain - Setup Inicial

## 📁 Criar diretório do projeto

```bash
mkdir meu_projeto_langchain
cd meu_projeto_langchain

#cria um abiente vitual

python -m venv venv

#ativar o abiente vitual
.\venv\Scripts\activate

No Windows:

python -m venv venv

```

Gere o requirements.txt:

Após instalar todas as dependências necessárias, você pode gerar o arquivo requirements.txt com o seguinte comando:

````bash
Copiar código
pip freeze > requirements.txt

```

# 📌 LLMs e LangChain Core
langchain==0.1.16
langchain-community==0.0.33
langchain-google-genai
huggingface_hub==0.22.2
transformers==4.39.3
sentence-transformers==2.7.0
lark

# 🧠 Bases vetoriais
langchain-chroma
faiss-cpu

# 📄 Manipulação de arquivos
pypdf==4.2.0

# 📺 YouTube e Áudio
yt_dlp==2024.4.9
pydub==0.25.1
beautifulsoup4==4.12.3

# ⚙️ Ambiente e utilitários
python-dotenv
jinja2==3.1.3
ipykernel

# ❗ ffmpeg e ffprobe não são do pip!
# Instale no sistema:
# - Windows: https://www.gyan.dev/ffmpeg/builds/
# - Ubuntu: sudo apt install ffmpeg
# - Mac: brew install ffmpeg

pip install -r requirements.txt --user

# Núcleo e execução
ipykernel
python-dotenv
# para widows
# LangChain e ecossistema
langchain==0.1.16
langchain-community==0.0.33
langchain-google-genai
langchain-core==0.1.51

# Gemini
google-generativeai==0.5.4

# Hugging Face e Transformers
huggingface_hub==0.22.2
transformers==4.39.3
sentence-transformers==2.7.0

# Utilidades de texto e PDF
pypdf==4.2.0
beautifulsoup4==4.12.3
jinja2==3.1.3

# Downloads e mídia
yt_dlp==2024.4.9
pydub==0.25.1

# Vetores e busca semântica
# faiss-cpu==1.7.4 esse não 
langchain-chroma

# Outros necessários
lark==1.1.9
