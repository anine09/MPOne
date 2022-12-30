import flet as ft


def build_card(title: str, subtitle: str) -> ft.Card:
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.COMPUTER),
                        title=ft.Text(title),
                        subtitle=ft.Text(subtitle),
                    ),
                    ft.Row(
                        [
                            ft.TextButton("Details"),
                            ft.TextButton("Settings"),
                            ft.TextButton("Reset"),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )


Tek = build_card(
    "Tektronix 2636B",
    "Keithley Instruments Inc., Model 2636B, 4308079, 3.2.2\n"
)

Wk = build_card(
    "WAYNE KERR 41100",
    "WAYNE KERR, 41100, 17411029, 4.143Z3\n"
)

Wk_1 = build_card(
    "WAYNE KERR 41100",
    "WAYNE KERR, 41100, 17411029, 4.143Z3\n"
)

content = ft.GridView(
    controls=[
        Tek,
        Wk,
        Wk_1,
        Tek
    ],
    max_extent=400,
    height=200
)


def create_content():
    return content
