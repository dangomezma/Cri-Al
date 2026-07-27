#!/bin/bash
set -euo pipefail

# ==========================================
# CONFIGURACIÓN
# ==========================================
REPO_URL="https://github.com/dangomezma/Cri-Al"
FOLDER_NAME=""

# ==========================================
# VALIDACIONES
# ==========================================

command -v git >/dev/null 2>&1 || { echo "Error: git no está instalado."; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "Error: python3 no está instalado."; exit 1; }

# ==========================================
# FLUJO
# ==========================================
if [ -z "$FOLDER_NAME" ]; then
    FOLDER_NAME=$(basename "$REPO_URL" .git)
fi

if [ -d "$FOLDER_NAME" ]; then
    echo "❌ Error: La carpeta '$FOLDER_NAME' ya existe."
    exit 1
fi

echo "Clonando repositorio..."
if ! git clone "$REPO_URL" "$FOLDER_NAME"; then
    echo "❌ Error: No se pudo clonar el repositorio."
    exit 1
fi

cd "$FOLDER_NAME" || { echo "❌ Error: No se pudo ingresar a la carpeta $FOLDER_NAME"; exit 1; }

echo "Creando el entorno virtual..."
if ! python3 -m venv venv; then
    echo "❌ Error: No se pudo crear el entorno virtual (¿falta python3-venv?)."
    exit 1
fi

echo "Activando el entorno virtual..."
# shellcheck disable=SC1091
source venv/bin/activate

if [ -f "requirements.txt" ]; then
    echo "Instalando dependencias desde requirements.txt..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi

if [ -f "manage.py" ]; then
    echo "🌐 Preparando apertura del navegador en http://127.0.0.1:8000/ ..."
    # Subshell en segundo plano con '|| true' para que no rompa la regla de 'set -e'
    (sleep 2 && (xdg-open http://127.0.0.1:8000/ || open http://127.0.0.1:8000/ || true) >/dev/null 2>&1) &

    echo "Servidor iniciado. Presiona Ctrl+C para detener el servidor."
    python manage.py runserver 0.0.0.0:8000
else
    echo "⚠️ No se encontró manage.py. El proyecto está listo pero el servidor no se inició."
fi