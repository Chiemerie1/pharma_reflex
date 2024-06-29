import reflex as rx
from . import style

color_scheme = "mint"

def custom_dialog(
    title: str,
    trigger: str,
    desc: str,
    cancel: str,
    action: str,
    on_click=None

) -> rx.components:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                trigger,
                color_scheme=color_scheme,
                style=style.button_style,
                type="submit",

            )
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(title),
            rx.divider(),
            rx.alert_dialog.description(
                desc
            ),
            rx.divider(),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button(cancel, color_scheme=color_scheme)
                ),
                rx.alert_dialog.action(
                    rx.button(action, color_scheme=color_scheme, on_click=on_click)
                ),
                spacing="5",
                justify="between",
            )
        )

    )