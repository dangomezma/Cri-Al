# Cri-Al 🔐

Aplicación web para cifrar y descifrar texto. Implementa los algoritmos de **Cifrado César**, **Vigenère** y **XOR**, con backend en Django y una interfaz web sencilla.

## Requisitos previos

- **Sistema operativo:** Linux (los scripts usan `xdg-open` para abrir el navegador).
- **bash**
- **git**
- **python3** (con el módulo `venv` disponible; en algunas distribuciones puede requerir instalar `python3-venv`)

No es necesario instalar Django ni ninguna otra dependencia manualmente: el script `setup.sh` se encarga de crear el entorno virtual e instalar todo lo indicado en `requirements.txt`.

## 🚀 Primera vez: instalación y ejecución

Solo necesitas **descargar el archivo `setup.sh`** (no es necesario clonar el repositorio a mano). Este script clona el repositorio, crea el entorno virtual, instala las dependencias y levanta el servidor automáticamente.

```bash
# 1. Descargar el script
curl -O https://raw.githubusercontent.com/dangomezma/Cri-Al/main/setup.sh
# (o con wget)
wget https://raw.githubusercontent.com/dangomezma/Cri-Al/main/setup.sh

# 2. Dar permisos de ejecución
chmod +x setup.sh

# 3. Ejecutar
./setup.sh
```

El script realizará automáticamente:

1. Verificación de que `git` y `python3` estén instalados.
2. Clonado del repositorio en una carpeta llamada `Cri-Al`.
3. Creación del entorno virtual (`venv`).
4. Instalación de las dependencias desde `requirements.txt`.
5. Apertura automática del navegador en `http://127.0.0.1:8000/`.
6. Inicio del servidor de desarrollo de Django.

Para detener el servidor, presiona `Ctrl+C` en la terminal.

> ⚠️ Si la carpeta `Cri-Al` ya existe en el directorio donde ejecutas `setup.sh`, el script se detendrá con un error para evitar sobrescribir datos. Esto es intencional: `setup.sh` está pensado para usarse **una sola vez** (la primera instalación).

## 🔁 Siguientes veces: usar `starter.sh`

Una vez que el proyecto ya fue instalado con `setup.sh`, **no vuelvas a ejecutar `setup.sh`**. Para las siguientes ejecuciones (o si quieres probar la aplicación de nuevo), usa `starter.sh`, que ya se encuentra dentro de la carpeta del proyecto clonado.

```bash
cd Cri-Al
./starter.sh
```

Este script:

1. Verifica que estés dentro de la carpeta del proyecto (busca `manage.py`).
2. Activa el entorno virtual ya creado (`venv`).
3. Abre el navegador automáticamente en `http://127.0.0.1:8000/`.
4. Inicia el servidor de desarrollo de Django.

Para detener el servidor, presiona `Ctrl+C`.

## 📂 Estructura del proyecto

```
Cri-Al/
├── setup.sh              # Instalación inicial (clonar + entorno + dependencias + ejecutar)
├── starter.sh             # Ejecución rápida en usos posteriores
├── manage.py               # Punto de entrada de Django
├── requirements.txt        # Dependencias del proyecto
├── crial_backend/          # Configuración del proyecto Django
└── cifrados/                # App con la lógica de cifrado/descifrado (César, Vigenère, XOR)
```

## 🧩 Funcionalidades

La aplicación permite, desde una interfaz web, cifrar y descifrar texto con:

- **Cifrado César** (incluye modo *fuerza bruta* probando los 26 desplazamientos posibles).
- **Cifrado Vigenère**.
- **Cifrado XOR**.

## Resolución de problemas

- **`Error: git no está instalado.` / `Error: python3 no está instalado.`**: instala los paquetes faltantes con el gestor de paquetes de tu distribución (por ejemplo `sudo apt install git python3 python3-venv` en Ubuntu/Debian) y vuelve a ejecutar el script.
- **`No se pudo crear el entorno virtual (¿falta python3-venv?)`**: instala el paquete `python3-venv` (`sudo apt install python3-venv` en Ubuntu/Debian) y vuelve a intentarlo.
- **`No se encontró la carpeta 'venv'. Ejecuta primero 'setup.sh'.`**: significa que intentaste ejecutar `starter.sh` sin haber corrido antes `setup.sh`. Ejecuta primero `setup.sh` para hacer la instalación inicial.
- **`❌ Error: La carpeta 'Cri-Al' ya existe.`**: elimina o renombra la carpeta existente antes de volver a ejecutar `setup.sh`, o simplemente entra a ella y ejecuta `starter.sh`.
- **El navegador no se abre automáticamente**: puedes ingresar manualmente a [http://127.0.0.1:8000/](http://127.0.0.1:8000/) mientras el servidor esté en ejecución.
