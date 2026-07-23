# School Portal Django

Portal institucional para gestión escolar desarrollado con Python, Django y PostgreSQL. Este proyecto nace como una solución integral para instituciones educativas, actualmente en desarrollo para el CBTA 108 (Santiago Ixcuintla, Nayarit).

## 🚀 Características

- [ ] Gestión de usuarios y roles (administrativos, docentes, alumnos)
- [ ] Módulo de noticias y avisos institucionales
- [ ] Panel administrativo personalizado
- [ ] Diseño responsivo
- [ ] Autenticación segura

> Esta sección se irá actualizando conforme el proyecto avance.

## 🛠️ Tecnologías

- **Backend:** Python 3.x, Django 5.x
- **Base de datos:** PostgreSQL
- **Control de versiones:** Git / GitHub

## 📋 Requisitos previos

- Python 3.10 o superior
- PostgreSQL instalado y corriendo
- pip / venv

## ⚙️ Instalación local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/school-portal-django.git
   cd school-portal-django
   ```

2. Crea y activa el entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno (crea un archivo `.env` en la raíz):
   ```
   SECRET_KEY=tu_clave_secreta
   DEBUG=True
   DATABASE_NAME=nombre_bd
   DATABASE_USER=usuario
   DATABASE_PASSWORD=contraseña
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

5. Aplica las migraciones:
   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

7. Levanta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## 📁 Estructura del proyecto

```
school-portal-django/
├── config/          # Configuración principal del proyecto Django
├── core/            # App principal
├── static/          # Archivos estáticos
├── templates/       # Plantillas HTML
├── manage.py
├── requirements.txt
└── README.md
```

## 🗺️ Roadmap

- [x] Configuración inicial del proyecto
- [ ] Módulo de autenticación
- [ ] Módulo de noticias/avisos
- [ ] Panel administrativo
- [ ] Despliegue en producción

## 🤝 Contribuciones

Este es un proyecto personal en desarrollo activo. Si tienes sugerencias, siéntete libre de abrir un issue.

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

## 👤 Autor

**Edgar Omar Palacios Manjarrez** — Ingeniero en Sistemas Computacionales / Ingeniero Agrónomo
Docente y Subdirector Académico, CBTA 108
