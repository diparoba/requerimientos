# PhysioCare - App de Fisioterapia

Esta aplicación fue generada automáticamente a partir de los requerimientos para un centro de fisioterapia avanzada. Incluye un backend robusto con FastAPI y un frontend moderno y responsivo.

## Estructura del Proyecto

- `backend/`: Código del servidor FastAPI, modelos de datos y base de datos.
- `frontend/`: Interfaz de usuario con HTML, CSS y JavaScript.

## Requisitos Previos

- Python 3.x
- Node.js y npm

## Configuración del Entorno Virtual (VENV)

Para inicializar tu entorno de trabajo cada vez que empieces, sigue estos pasos:

### 1. Activar el Entorno Virtual
En la raíz del proyecto, ejecuta:

```powershell
# En Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

### 2. Instalar Dependencias del Backend
```bash
pip install -r backend/requirements.txt
```

### 3. Inicializar la Base de Datos
```bash
python backend/init_db.py
```

### 4. Ejecutar el Servidor Backend
```bash
cd backend
uvicorn main:app --reload
```

## Configuración del Frontend

### 1. Instalar dependencias
```bash
cd frontend
npm install
```

### 2. Ejecutar el Frontend
```bash
npm start
```

## Características Implementadas
- **Backend:** FastAPI con base de datos SQLite (preparado para PostgreSQL).
- **Modelos:** Ejercicios de rehabilitación y tipos de tratamientos.
- **Frontend:** Diseño premium con Glassmorphism, responsivo y dinámico.
- **Chat:** Widget de chat integrado para comunicación rápida.
