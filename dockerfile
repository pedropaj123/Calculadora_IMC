# Use uma imagem base que já tenha Python
FROM python:3.9-slim

# Instalar dependências do sistema para o Oracle Instant Client
RUN apt-get update && apt-get install -y \
    libaio1 \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Baixar e instalar o Oracle Instant Client
RUN mkdir -p /opt/oracle && \
    cd /opt/oracle && \
    curl -L -o instantclient.zip https://download.oracle.com/otn_software/linux/instantclient/210000/instantclient-basic-linux.x64-21.3.0.0.0.zip && \
    unzip instantclient.zip && \
    rm instantclient.zip

# Configurar as variáveis de ambiente
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_3:$LD_LIBRARY_PATH
ENV PATH=/opt/oracle/instantclient_21_3:$PATH

# Criar e configurar o diretório de trabalho
WORKDIR /app

# Copiar todos os arquivos do projeto para dentro do container
COPY . .

# Instalar as dependências Python do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta para o Flask
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "calculadora.py"]
