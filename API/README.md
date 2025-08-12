Dockerfile com Python 3.12
 
FROM python:3.12-slim WORKDIR /app COPY requirements.txt . RUN pip install --no-cache-dir -r requirements.txt COPY . . CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
 
 
Certifique-se de incluir uvicorn e fastapi no seu requirements.txt para que a API funcione corretamente.
 
 
🐳 docker-compose.yml
 
version: "3.9" services:   fastapi-ml:     build: .     container_name: ml-api     ports:       - "8000:8000"     volumes:       - .:/app     restart: unless-stopped
 
 
Tudo pronto para rodar no Windows! Basta abrir o terminal, navegar até a pasta e executar:
 
docker-compose up --build
 
Se quiser que a API rode em segundo plano:
 
docker-compose up -d --build
 
Precisa de algo extra, como variáveis de ambiente, rede customizada ou suporte a Swagger? É só dizer e eu adapto rapidinho 🤖
