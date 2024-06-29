"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config

from database.mongo import db
from . import sign_up
from .component import color_scheme


# color_scheme = "mint"


class State(rx.State):
    """The app state."""
    def print_it(self):
        print("working")




def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Pharma", size="8", color_scheme="gray"),
            rx.text(
                "Your one-stop solution",
                # rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="2",
            ),
            rx.link(
                rx.button(
                    "Sign up",
                    color_scheme=color_scheme,
                ),
                href="sign-up",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
app.add_page(sign_up.sign_up, route="/sign-up")
