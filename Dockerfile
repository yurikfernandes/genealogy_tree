FROM python:3.11-slim

WORKDIR /app

# Instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta que o servidor utilizará
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["python", "main.py"]