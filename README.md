# Pregúntale a Foxy

**Pregúntale a Foxy** es una aplicación web de chat construida con [Reflex](https://reflex.dev/), 
en la que puedes interactuar con un simpático asistente virtual. Aunque originalmente se planteó como un chatbot con Inteligencia Artificial, actualmente responde con lógica condicional en Python... ¡pero con mucha personalidad!

---

## 🚀 ¿Qué hace esta app?

- Simula un chat con un personaje (Foxy 🦊).
- Detecta palabras clave en tus preguntas.
- Devuelve respuestas divertidas, escritas con un efecto de “máquina de escribir”.
- Se puede ejecutar 100% offline y sin necesidad de conexión a una API externa (como OpenAI).
- Tiene una interfaz interactiva construida con componentes de Reflex.

---

## 🧠 Tecnologías y habilidades aplicadas

| Herramienta / Habilidad | Aplicación en el proyecto |
|--------------------------|---------------------------|
| **Python**              | Lógica del chat, control de estados y respuestas. |
| **Reflex**              | Framework para crear apps web en Python (sin necesidad de JS). |
| **Async/Await**         | Simulación del efecto “tipo máquina de escribir” en el chat. |
| **Manejo de estado**    | Historial de conversación y entradas del usuario. |
| **Condicionales (`if`)**| Generación de respuestas personalizadas. |
| **Estilos personalizados** | Aplicación de temas y diseño visual con Reflex. |

---

## 🧩 Estructura del proyecto
```
preguntale_a_Foxy/
│
├── preguntale_a_Foxy/
│   ├── __init__.py
│   ├── preguntale_a_Foxy.py   # Componente principal del app
│   ├── state.py               # Lógica del estado y respuestas
│   ├── style.py               # Estilos del chat
│
├── assets/                    # Recursos adicionales (logos)
├── requirements.txt           # Dependencias del proyecto
├── Dockerfile                 # Configuración para contenedor Docker
├── rxconfig.py                # Configuración Reflex
└── README.md                  # Documentación del proyecto
```

# Requisitos para ejecutarlo
-  Instalar Reflex
- pip install reflex

# Ejecutar el proyecto
- reflex run
# Posibilidades de mejora
- Integrar API de IA (como OpenAI) para respuestas inteligentes.
- Añadir animaciones o stickers de Foxy.
# ✨ Autor
- Jennifer Paola Arciniegas Arciniegas
