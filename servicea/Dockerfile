# Usar imagen base de Python con Alpine
FROM python:3.9-alpine

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY servicio_a.py /app

# Instalar dependencias de Flask
RUN pip install --no-cache-dir Flask

# Exponer el puerto que usará la aplicación
EXPOSE 3001

# Comando para ejecutar la aplicación
CMD ["python", "servicio_a.py"]
