"""
@package vulnerable_app
Aplicación Flask vulnerable utilizada para pruebas de seguridad dentro del pipeline Jenkins.

Este servidor es intencionalmente inseguro. Se utiliza para:
- Auditorías con SonarQube
- Análisis de dependencias con Dependency-Check
- Ejecución del pipeline definido en Jenkinsfile
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    """
    @brief Ruta principal del servidor.
    @return Mensaje simple de bienvenida.
    """
    return "Welcome to the vulnerable app!"


@app.route('/hello', methods=['GET'])
def hello():
    """
    @brief Endpoint vulnerable a inyección por parámetros no validados.
    @param name Nombre recibido desde la URL (?name=valor)
    @return Cadena de saludo personalizada sin sanitizar.
    
    Vulnerabilidad:
    - No se sanitiza el parámetro "name".
    - Permite XSS (Cross-Site Scripting).
    """
    name = request.args.get('name')
    return f'Hello, {name}!'


if __name__ == '__main__':
    """
    @brief Ejecuta el servidor Flask vulnerable.
    @details
    El servidor se expone abiertamente en 0.0.0.0:5000 para que el Jenkinsfile
    pueda alcanzarlo en la etapa de análisis (TARGET_URL).
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
