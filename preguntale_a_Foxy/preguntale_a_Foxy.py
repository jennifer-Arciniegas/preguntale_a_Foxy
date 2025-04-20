import reflex as rx
from preguntale_a_Foxy import style
from preguntale_a_Foxy.state import State

def header() -> rx.Component:
    """Cabecera de la aplicación con título y botón de modo oscuro."""
    return rx.flex(
        rx.heading("Pregúntale a Foxy", size="8"),  # Cambiado "lg" por tamaño numérico válido
        rx.color_mode.button(position="top-right"),
        justify="between",
        align="center",
        width="100%",
        padding="1em"
    )

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
        width="100%",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Preguntame",
            on_change=State.set_question,
           # on_key_down=lambda e: State.answer() if e.key =="Enter" else None,
            style=style.input_style,
        ),
        rx.button(
            "Da click",
            on_click=State.answer,
            style=style.button_style,
        ),
    )

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            chat(),
            action_bar(),
            align="center",
        )
    )

app = rx.App()
app.add_page(index)