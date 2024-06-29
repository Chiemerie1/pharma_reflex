import reflex as rx
from . import style
from .sign_up_states import SignUp






color_scheme = "mint"

def sign_up() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.card(
                rx.form(
                    rx.vstack(
                        rx.text("Sign up", size="5", color_scheme="gray"),
                        rx.input(
                            color_scheme=color_scheme,
                            placeholder="Username",
                            name="username",
                            style=style.input_style, 
                        ),
                        rx.input(
                            color_scheme=color_scheme,
                            placeholder="Name of pharmacy",
                            name="pharmacy",
                            style=style.input_style,
                            
                        ),
                        rx.input(
                            color_scheme=color_scheme,
                            placeholder="Incorporation no",
                            name="incoporation_no",
                            style=style.input_style,
                            
                            
                        ),
                        rx.input(
                            color_scheme=color_scheme,
                            placeholder="Practice liscence",
                            name="liscence",
                            style=style.input_style,
                            
                        ),
                        rx.button(
                            "Register",
                            color_scheme=color_scheme,
                            style=style.button_style,
                            type="submit",
                        ),
                        rx.divider(),
                        rx.heading("Notification", size="3"),
                        spacing="5",
                        align="center",
                    ),
                    on_submit=SignUp.handle_submit,
                    reset_on_submit=True,
                )
                
            ),
            align="center",
            justify="center",
            height="100vh"
            
        )
    )