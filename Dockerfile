# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app
WORKDIR /app/src
# Copia el archivo pyproject.toml al contenedor
COPY pyproject.toml /app/

# Instala las dependencias necesarias
RUN pip install --upgrade pip setuptools wheel
#RUN pip install .

# Copia el código fuente al contenedor
COPY src/ /app/src/

# Expone el puerto si es necesario
EXPOSE 8080

# Establece el comando por defecto para ejecutar el contenedor
CMD ["python", "app/src/main.py"]
