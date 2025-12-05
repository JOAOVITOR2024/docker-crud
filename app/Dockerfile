# Use imagem oficial do python
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copia requirements e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia app
COPY . .

# Exponha porta
EXPOSE 5000

# Comando para rodar
CMD ["python", "app.py"]
