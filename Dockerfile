# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo pyproject.toml al contenedor
COPY pyproject.toml /app/

# Instala las dependencias necesarias
RUN pip install --upgrade pip setuptools wheel
RUN pip install .

# Copia el código fuente al contenedor
COPY src/ /app/src/

# Establece el comando por defecto para ejecutar el contenedor
CMD ["python", "src/main.py"]
