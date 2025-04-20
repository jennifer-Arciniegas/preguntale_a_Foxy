import reflex as rx
import asyncio as asy

class State(rx.State):
    # The current question being asked.
    question: str = ""
    
    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]] = []

    def get_response(self, question: str) -> str:
        question = question.lower()
        
        if "hola" in question:
            return "¡Hola humano! 🦊"
        elif "cómo estás" in question or "como estas" in question:
            return "Estoy muy bien, gracias por preguntar 🌟"
        elif "no entiendo" in question or "no se" in question:
            return "Deberíamos estudiar más. (Tampoco sé, XD)"
        elif "quién eres" in question or "cómo te llamas" in question:
            return "Soy Foxy, tu asistente virtual peludo 🦊✨"
        elif "ayuda" in question or "me explicas" in question:
            return "Yo creo que Google u otra IA si puede saber, yo apenas estoy aprendiendo"
        elif "que haces" in question or "hacer" in question:
            return "Hacer no hacer, tengo pereza"
        elif "tengo este codigo" in question or "corrige" in question:
            return "Preguntale a un adulto responsable o a Google"
        elif "bye" in question or "chao" in question:
            return "¡Hasta luego! 🖐️"
        else:
            return "Hmm... no entendí eso. ¿Puedes intentarlo de otra forma?"

    async def answer(self) -> None:  # Añadido tipo de retorno
        # Obtener respuesta personalizada
        response = self.get_response(self.question)

        # Agregar pregunta y respuesta vacía al historial
        self.chat_history.append((self.question, ""))
        self.question = ""

        yield  # Permitir que el frontend se actualice

        # Escribir la respuesta letra por letra (efecto máquina de escribir)
        for i in range(len(response)):
            await asy.sleep(0.05)
            self.chat_history[-1] = (
                self.chat_history[-1][0], 
                response[:i + 1]
            )
            yield