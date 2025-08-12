# 📦 FastAPI ML API com Docker (Python 3.12)

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

---

## 🛠️ Dockerfile (Python 3.12)

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

> ⚠️ **Importante:** Inclua `uvicorn` e `fastapi` no seu arquivo `requirements.txt` para que a API funcione.

Exemplo de `requirements.txt`:
```
fastapi
uvicorn
```

---

## 🐳 docker-compose.yml

```yaml
version: "3.9"
services:
  fastapi-ml:
    build: .
    container_name: ml-api
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    restart: unless-stopped
```

---

## ⚙️ Como Rodar

### Pré-requisitos
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Passos
1. Abra o terminal e navegue até a pasta do projeto
2. Execute:
```bash
docker-compose up --build
```
3. Para rodar em segundo plano:
```bash
docker-compose up -d --build
```
4. Para rodar a API:
```bash
Gerar o arquivo model.pkl e colocar na raiz do projeto
---
```

## 🌐 Acessando a API
Após iniciar, a API estará disponível em:
```
http://localhost:8000
```

---

## 📄 Documentação Swagger
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛑 Parar o Container
```bash
docker-compose down
```

---

## 🧩 Possíveis Melhorias
- Adicionar variáveis de ambiente (`.env`)
- Configurar rede Docker customizada
- Criar volume para persistência de dados
- Adicionar testes automatizados

---

