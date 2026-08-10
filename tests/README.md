
NFA TO DFA Servidor online

Servidor web online que convierte un autómata finito no determinista(NFA) en su autómata finito determinista(DFA) equivalente, usando el algoritmo de Subset Construction

Equipo

- Laura Sofia Zarazo
- Santiago Molano

Herramientas:

Windows 11.
Python3.14.3
Framework web: FastAPI 0.141.1 ( recomendado por IA y profundizado en youtube)
Servidor:(Uvicorn.052)
Validación de datos: Pydantic 2.13.4(recomendador por IA)
IDE: Visual studio code.

Orden de ejecución del proyecto:
Clonar el repositorio:
   git clone https://github.com/Santiagom09/LenguajesFormales.git
   cd LenguajesFormales
   
Crear y activar un entorno virtual:
   python -m venv venv
   .\venv\Scripts\activate      # Windows
   
Instalar dependencias:
   pip install -r requirements.txt
   
Levantar el servidor:
   uvicorn Project.app.main:app --reload

Probar la API desde el navegador (documentación interactiva automática)http://127.0.0.1:8000/docs

Arquitectura 
El proyecto sigue una arquitectura por capas, cada una con una única
responsabilidad:
HTTP Request → Controller → Gateway → Functions → HTTP Response

Controller: PYDANTIC Recibe las peticiones HTTP, valida la forma del input mediante modelos Pydantic, y retorna las respuestas con el código HTTP correspondiente.

Gateway: coordina la ejecución
del algoritmo y valida reglas de negocio como por ejemplo, que el estado
inicial y los estados de aceptación existan dentro de la lista de
estados.

Function: contiene la implementación pura del algoritmo

Models: modelos Pydantic que definen la forma de los datos de entrada y salida.

Endpoint:
POST/CONVERT: Recibe la definción de un NFA y retorna el DFA equivalente a NFA

json:
{
    "states": [0,1,2,3,4,5,6,7,8],
    "alphabet": ["a","b"],
    "initial": 0,
    "accepting": [8],
    "transitions": [
        {"from": 0, "symbol": "a", "to": [1,3,7]}
    ]
}
```
Output:
```json
{
    "dfaStates": ["0","137","12","7","8","∅"],
    "transitions": [
        {"from": "0", "symbol": "a", "to": "137"}
    ],
    "acceptingStates": ["8"],
    "initial": "0"
}



POST/SIMULATE Recibe un DFA y una cadena de entrada, y retorna el camino recorrido verificando si la cadena fue aceptada o no.

json:

{
    "dfa": { "...": "el DFA generado por /convert" },
    "input": "ab"
}
```
Output:
```json
{
    "path": ["0", "137", "8"],
    "accepted": true
}






Uso de IA 
Se utilizó Claude (Anthropic) como asistente de aprendizaje y depuración
durante el desarrollo de este proyecto, específicamente para:
Explicación conceptual del algoritmo de Subset Construction.
Guía en el diseño de la arquitectura Controller/Gateway/Functions.
Depuración de errores de entorno (configuración de Python/pip/venv en
Windows, PATH, alias de Microsoft Store).
Corrección de errores de indentación y sintaxis durante el desarrollo.
Generación de código boilerplate de FastAPI (definición de rutas,
manejo de excepciones HTTP) en `nfa_controller.py` y `main.py`.
Revisión y corrección de la lógica implementada por el estudiante en
`subset_construction.py` y `nfa_gateway.py`.
El algoritmo central (Subset Construction) y su implementación en
`mover()`, `construir_dfa_por_subconjuntos()` y las validaciones del
Gateway fueron escritos y comprendidos por el estudiante, con
correcciones guiadas de IA.


















## Uso de IA
Se utilizó Claude (Anthropic) como asistente para:
- Explicación del algoritmo Subset Construction (conceptos de Kozen, lecturas 3/5/6)
- Guía en el diseño de la arquitectura Controller/Gateway/Functions
- Depuración de errores de entorno (Python/pip en Windows)
- Generación de boilerplate de FastAPI (router, HTTPException) en nfa_controller.py
- Revisión y corrección de código escrito por el estudiante en subset_construction.py y nfa_gateway.py
