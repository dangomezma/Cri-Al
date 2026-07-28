#!/bin/bash
set -euo pipefail

echo "Iniciando CriAl..."

# 1. Validar que estamos en la carpeta
if [ ! -f "manage.py" ]; then
    echo "❌ Error: No se encontró 'manage.py'. Asegúrate de ejecutar este script desde la carpeta del proyecto."
    exit 1
fi

# 2. Validar y activar el entorno virtual
if [ -d "venv" ]; then
    echo "Activando entorno virtual..."
    # shellcheck disable=SC1091
    source venv/bin/activate
else
    echo "❌ Error: No se encontró la carpeta 'venv'. Ejecuta primero 'setup.sh'."
    exit 1
fi

# 3. Lanzar la apertura del navegador en segundo plano
echo "🌐 Abriendo la aplicación en http://127.0.0.1:8000/ ..."
(sleep 2 && (xdg-open http://127.0.0.1:8000/ || open http://127.0.0.1:8000/ || true) >/dev/null 2>&1) &

# 4. Iniciar el servidor
echo "✨ Servidor en ejecución. Presiona Ctrl+C para detenerlo."
python manage.py runserver 0.0.0.0:8000