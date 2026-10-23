# Usa uma imagem base leve oficial do Python 3.11
FROM python:3.11-slim

# Define a pasta de trabalho central dentro do container
WORKDIR /app

# Garante que os logs do Python sejam exibidos imediatamente no terminal
ENV PYTHONUNBUFFERED=1

# Copia a pasta src contendo o código da aplicação para dentro do container
COPY src/ /app/src/

# Define o comando padrão para executar a aplicação CLI
CMD ["python", "src/main.py"]