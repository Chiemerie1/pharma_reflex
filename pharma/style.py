import reflex as rx




# shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
# chat_margin = "20%"
# message_style = dict(
#     padding="1em",
#     border_radius="5px",
#     margin_y="0.5em",
#     box_shadow=shadow,
#     max_width="30em",
#     display="inline-block",
# )

hover_color = "ruby"

shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
input_style = dict(
    width="30em",
)

button_style = dict(
    width="30em",
    margin_left="10px",
    margin_right="10px",
    margin_bottom="10px",
    **{":hover":{
        "background-color":"#e10531",
        # "opacity": 0.5,
        "color": "#fff",
        }
    }
)