# 🚀 LangChain Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-blueviolet)](https://python.langchain.com/)
<img src="https://img.shields.io/badge/AWS-232F3E?logo=amazon-aws&logoColor=white" alt="AWS" />
<img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/Node.js-339933?logo=nodedotjs&logoColor=white" alt="Node.js" />
<img src="https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB" alt="React" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=white" alt="MongoDB" />
<img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white" alt="MySQL" />

Bem-vindo ao **LangChain Lab**!  
Este repositório reúne exemplos práticos, experimentos e módulos para desenvolvimento de aplicações com [LangChain](https://python.langchain.com/), incluindo:

- 🔗 **Chains**: Composição de fluxos de LLMs
- 📚 **RAG**: Retrieval-Augmented Generation
- 🧠 **Memória**: Implementação de memória em chains
- 💡 **Exemplos e Notebooks**: Casos de uso e tutoriais

---

## 📦 Estrutura do Projeto

```
langChain/
├── src/
│   ├── chains/         # Chains customizadas
│   ├── rag/            # Módulos de RAG
│   └── memoria/        # Suporte à memória
├── exemplos/           # Scripts de exemplo
├── notebooks/          # Notebooks interativos
├── requirements.txt    # Dependências do projeto
├── .env.example        # Exemplo de variáveis de ambiente
└── README.md           # Este arquivo
```

---

## ⚙️ Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/langchain-lab.git
   cd langchain-lab
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente:
   - Copie `.env.example` para `.env` e preencha com suas chaves de API.

---

## 🚦 Como Usar

- Execute exemplos em `exemplos/`:
  ```sh
  python exemplos/exemplo_chain.py
  ```
- Explore os notebooks em `notebooks/` para tutoriais interativos.

---

## 🛡️ Segurança

- **NUNCA** compartilhe suas chaves de API.
- Arquivos sensíveis já estão no `.gitignore`.

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Abra uma issue ou envie um pull request.

---

## 📄 Licença

Este projeto está sob a licença MIT.  
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
