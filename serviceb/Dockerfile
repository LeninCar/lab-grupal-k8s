# Usar imagen base de Node.js con Alpine
FROM node:14-alpine

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY servicio_b.js /app

# Instalar dependencias
RUN npm install express

# Exponer el puerto que usará la aplicación
EXPOSE 3002

# Comando para ejecutar la aplicación
CMD ["node", "servicio_b.js"]
