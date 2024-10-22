# Usar imagen base de Python con Alpine
FROM python:3.9-alpine

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY orquestador.py /app

# Instalar dependencias
RUN pip install --no-cache-dir fastapi uvicorn httpx

# Exponer el puerto que usará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "orquestador:app", "--host", "0.0.0.0", "--port", "8000"]
