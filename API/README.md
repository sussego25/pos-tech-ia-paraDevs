# 📦 FastAPI ML API com Docker

Este projeto contém uma API em **FastAPI** preparada para rodar em contêiner Docker com **Python 3.12**.

## 🚀 Tecnologias
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- Python 3.12
- Docker e Docker Compose

---

## 📂 Estrutura do Projeto

```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
└── README.md
```

- **Dockerfile** → Define a imagem com Python 3.12 e instala dependências
- **docker-compose.yml** → Configuração para rodar a API com Docker
- **requirements.txt** → Lista de bibliotecas necessárias (`fastapi`, `uvicorn`, etc.)
- **main.py** → Arquivo principal da aplicação FastAPI

---

## ⚙️ Configuração

### 1️⃣ Pré-requisitos
Certifique-se de ter instalado:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

### 2️⃣ Criar o arquivo `requirements.txt`
Exemplo de conteúdo:
```
fastapi
uvicorn
```
Adicione também outras dependências que seu projeto utilizar.

---

### 3️⃣ Rodar o projeto

#### No Windows, Linux ou Mac:
```bash
docker-compose up --build
```

Para rodar em **segundo plano**:
```bash
docker-compose up -d --build
```

---

## 🌐 Acessando a API
Depois de subir o container, a API estará disponível em:
```
http://localhost:8000
```

---

## 📄 Documentação Automática (Swagger)
Acesse a documentação interativa no navegador:
```
http://localhost:8000/docs
```

Ou no formato **ReDoc**:
```
http://localhost:8000/redoc
```

---

## 🛠 Parar o container
Para parar a API:
```bash
docker-compose down
```

---

## 🧩 Possíveis melhorias
- Adicionar variáveis de ambiente (`.env`)
- Configurar rede Docker customizada
- Criar volume para persistir dados
- Adicionar testes automatizados

---

## 📜 Licença
Este projeto está sob a licença MIT.
