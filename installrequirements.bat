@echo off
:: Instalador automático para el proyecto

:: Verificar si Python está instalado
where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python no está instalado. Descargándolo...
    start https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe
    echo Por favor, instala Python y ejecuta este script de nuevo.
    exit /b
)

:: Crear entorno virtual
if not exist venv (
    echo Creando entorno virtual...
    python -m venv venv
)

:: Activar entorno virtual
call venv\Scripts\activate

:: Instalar dependencias
if exist requirements.txt (
    echo Instalando dependencias...
    pip install --upgrade pip
    pip install -r requirements.txt
) else (
    echo No se encontró requirements.txt
)

:: Verificar conexión a MySQL
if exist test_connection.py (
    echo Probando conexión a MySQL...
    python test_connection.py
) else (
    echo No se encontró test_connection.py
)

echo Instalación completa. Presiona cualquier tecla para salir.
pause