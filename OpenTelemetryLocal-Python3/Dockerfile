# Usar la imagen oficial de Python 3
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el script Python al contenedor
COPY function.py /app/

# Instalar boto3
RUN pip3 install boto
RUN pip3 install boto3
RUN pip3 install opentelemetry-api
RUN pip3 install opentelemetry-sdk
RUN pip3 install opentelemetry-exporter-otlp
RUN pip3 install opentelemetry-instrumentation-boto

# Comando para ejecutar el script cuando el contenedor inicie
CMD ["python", "/app/function.py"]
