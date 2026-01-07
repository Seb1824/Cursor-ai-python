# Gestor de Issues - Aplicación Flask

Aplicación web desarrollada con Flask para gestionar issues (tareas, bugs y mejoras) de proyectos de software. Permite crear, listar y marcar issues como completados de manera intuitiva.

## 📋 Descripción

Esta aplicación permite a los desarrolladores y equipos de trabajo gestionar sus issues de manera organizada. Cada issue puede tener:
- **ID único**: Identificador automático
- **Título**: Nombre descriptivo del issue
- **Descripción**: Detalles sobre el issue
- **Prioridad**: Alta, Media o Baja
- **Estado**: Pendiente o Completado

La aplicación incluye una interfaz web moderna y responsive que facilita la gestión visual de los issues.

## ✨ Características

- ✅ Crear nuevos issues con formulario intuitivo
- 📋 Listar todos los issues en tarjetas visuales
- ✓ Marcar issues como completados
- 🎨 Interfaz moderna y responsive
- 💡 Ejemplos interactivos para guiar al usuario
- 🔔 Mensajes de confirmación y notificaciones
- 🎯 Sistema de prioridades con colores distintivos

## 🏗️ Estructura del Proyecto

```
flask_app/
├── app.py                 # Aplicación principal Flask
├── issues.py              # Módulo con clases Issue y GestorIssues
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
├── static/
│   └── style.css         # Estilos CSS de la aplicación
└── templates/
    ├── base.html         # Template base con navegación
    ├── index.html        # Página principal (lista de issues)
    └── add_issue.html    # Formulario para agregar issues
```

## 🚀 Instalación

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Navegar al directorio del proyecto:**
   ```bash
   cd flask_app
   ```

2. **Crear un entorno virtual (recomendado):**
   ```bash
   # En Windows
   python -m venv venv
   venv\Scripts\activate

   # En Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

   Esto instalará Flask y todas sus dependencias necesarias.

4. **Verificar la instalación:**
   ```bash
   python -c "import flask; print('Flask instalado:', flask.__version__)"
   ```

## ▶️ Ejecución

1. **Asegúrate de estar en el directorio `flask_app`:**
   ```bash
   cd flask_app
   ```

2. **Activa el entorno virtual (si lo creaste):**
   ```bash
   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Ejecuta la aplicación:**
   ```bash
   python app.py
   ```

4. **Abre tu navegador y visita:**
   ```
   http://127.0.0.1:5000
   ```

   O alternativamente:
   ```
   http://localhost:5000
   ```

## 📖 Uso de la Aplicación

### Página Principal (Lista de Issues)

- **Ver todos los issues**: La página principal muestra todas las tarjetas de issues creados
- **Ejemplos interactivos**: En la parte superior encontrarás ejemplos de cómo crear issues
- **Agregar nuevo issue**: Haz clic en el botón "+ Agregar Nuevo Issue" para crear uno nuevo

### Crear un Issue

1. Haz clic en "Agregar Issue" en el menú de navegación o en el botón principal
2. Completa el formulario:
   - **Título**: Un nombre descriptivo (ej: "Corregir bug en login")
   - **Descripción**: Detalles del issue (ej: "El botón no responde en móviles")
   - **Prioridad**: Selecciona Alta, Media o Baja
3. Haz clic en "Agregar Issue"

### Marcar Issue como Completado

- En la tarjeta del issue, haz clic en el botón "Marcar como Completado"
- Confirma la acción en el diálogo
- El issue cambiará su estado y se mostrará con un indicador visual

## 🛠️ Tecnologías Utilizadas

- **Flask**: Framework web de Python
- **Python 3**: Lenguaje de programación
- **HTML5**: Estructura de las páginas
- **CSS3**: Estilos y diseño responsive
- **Jinja2**: Motor de plantillas (incluido con Flask)

## 📝 Notas Importantes

- ⚠️ **Almacenamiento en memoria**: Los issues se almacenan en memoria, por lo que se perderán al reiniciar el servidor. Para persistencia, considera agregar una base de datos.

- 🔒 **Clave secreta**: En producción, cambia la `secret_key` en `app.py` por una clave segura.

- 🐛 **Modo debug**: La aplicación está configurada con `debug=True` para desarrollo. En producción, desactívalo.

## 🤝 Contribuciones

Esta aplicación fue creada con asistencia de inteligencia artificial usando el IDE Cursor.

## 📄 Licencia

Este proyecto es de uso educativo y demostrativo.

---

**Desarrollado usando Flask y Python**
