import flet as ft
from utils.responsive_menu_layout import ResponsiveMenuLayout as Layout, \
    create_page, \
    toggle_menu_width, toggle_icons_only


def main(page: ft.Page, title="MPOne Easy GUI Project"):
    page.title = title
    page.window_width = 1280
    page.window_height = 720

    menu_button = ft.IconButton(ft.icons.MENU)

    page.appbar = ft.AppBar(
        leading=menu_button,
        leading_width=40,
    )

    pages = [
        (
            dict(
                icon=ft.icons.INFO_OUTLINED,
                selected_icon=ft.icons.INFO,
                label="Instrument Info"
            ),
            ft.FilledButton()
        ),
        (
            dict(
                icon=ft.icons.INSERT_CHART_OUTLINED,
                selected_icon=ft.icons.INSERT_CHART,
                label="Plot Chart",
                route="plot-chart"
            ),
            ft.Switch()
        ),
        (
            dict(
                icon=ft.icons.TABLE_CHART_OUTLINED,
                selected_icon=ft.icons.TABLE_CHART,
                label="Tabular View",
                route="tabular-view"
            ),
            ft.Slider(value=0.3)
        ),
        (
            dict(
                icon=ft.icons.HELP_OUTLINE,
                selected_icon=ft.icons.HELP,
                label="Help Information",
                route="help-information"
            ),
            ft.TextField(label="Standard")
        )
    ]
    menu_layout = Layout(page, pages)

    page.appbar.actions = [
        ft.Row(
            [
                ft.Text("Minimize\nto icons"),
                ft.Switch(on_change=lambda e: toggle_icons_only(menu_layout)),
                ft.Text("Menu\nwidth"),
                ft.Switch(value=True, on_change=lambda e: toggle_menu_width(menu_layout)),
            ]
        )
    ]

    menu_layout.navigation_rail.leading = ft.ElevatedButton(
        "Add", icon=ft.icons.LAN,
    )

    page.add(menu_layout)

    menu_button.on_click = lambda e: menu_layout.toggle_navigation()


ft.app(target=main)
