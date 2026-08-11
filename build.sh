#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

echo "=== DIAGNOSTICO ==="
pwd
ls -la
echo "=== Contenido de static/ ==="
ls -la static/ || echo "La carpeta static/ NO existe aqui"
echo "=== FIN DIAGNOSTICO ==="

python manage.py collectstatic --no-input

python manage.py migrate