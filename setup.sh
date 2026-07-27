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
    echo "📚 Instalando dependencias desde requirements.txt..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi

echo "El entorno virtual está activo y estás listo para trabajar."