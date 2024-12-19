# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** (model.joblib y vectorizer.joblib)
- **Plataforma de despliegue:** (fats API con Railway)
- **Requisitos técnicos:** (Python 3.8 o superior y todos almacenado en el archivo reqirements.txt)
- **Requisitos de seguridad:** (Ninguno)
- **Diagrama de arquitectura:** (Todo se encuentra en el notebook que se utilizo para generar todo lo relacionado al despliegue)

## Código de despliegue

- **Archivo principal:** (El archivo inicial del despliegue es el Dockerfil y pyproyect.toml que utiliza railway para realiar el despliegue de la aplicacion)
- **Rutas de acceso a los archivos:** (todos los archivos necesarios para el despliegue se encuentran en la carpeta src y el archivo Dockerfile y el pyproject.toml ya mencionados)
- **Variables de entorno:** (Ninguna)

## Documentación del despliegue

- **Instrucciones de instalación:** (Crear un nuevo servicio en railway con este repositorio)
- **Instrucciones de configuración:** (No se requiere ninguna configuracion adicional, este reporsitorio contiene todos los archivos de configuracion necesaria para railway y dejar disponible, los unico que debe verificarse es que en railway quede configurado el puerto 8080)
- **Instrucciones de uso:** (desde un notebook puede realizar la peticion de post a la url con la noticia que se desea vedrificar si es falsa o verdadera)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
