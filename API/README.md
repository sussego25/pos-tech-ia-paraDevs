# FastAPI ML Inference API

Esta API fornece um endpoint GET para realizar inferência de um modelo de machine learning carregado via pickle.

## Requisitos

- Docker
- Arquivo `model.pkl` (pickle do modelo treinado)

## Como rodar localmente

1. Coloque o arquivo `model.pkl` na raiz do projeto.

2. Construa a imagem Docker:
   ```bash
   docker build -t fastapi-ml .