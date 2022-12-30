import flet as ft
from .Layout.responsive_menu_layout import (
    ResponsiveMenuLayout as Layout,
    toggle_menu_width,
    toggle_icons_only
)
from .Page import (
    Instrument_info,
    Plot_Chart,
    Tabular_View,
    Settings,
    Help_Information
)


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
            Instrument_info.create_content()
        ),
        (
            dict(
                icon=ft.icons.INSERT_CHART_OUTLINED,
                selected_icon=ft.icons.INSERT_CHART,
                label="Plot Chart",
                route="plot-chart"
            ),
            Plot_Chart.create_content()
        ),
        (
            dict(
                icon=ft.icons.TABLE_CHART_OUTLINED,
                selected_icon=ft.icons.TABLE_CHART,
                label="Tabular View",
                route="tabular-view"
            ),
            Tabular_View.create_content()
        ),
        (
            dict(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
                label="Settings",
                route="settings"
            ),
            Settings.create_content()
        ),
        (
            dict(
                icon=ft.icons.HELP_OUTLINE,
                selected_icon=ft.icons.HELP,
                label="Help Information",
                route="help-information"
            ),
            Help_Information.create_content()
        )
    ]

    menu_layout = Layout(page, pages)

    page.appbar.actions = [
        ft.Row(
            [
                ft.Text("Minimize\nto icons"),
                ft.Switch(on_change=lambda e: toggle_icons_only(menu_layout)),
                ft.Text("Menu\nwidth"),
                ft.Switch(
                    value=True, on_change=lambda e: toggle_menu_width(menu_layout)),
            ]
        )
    ]

    menu_layout.navigation_rail.leading = ft.ElevatedButton(
        "Add", icon=ft.icons.LAN,
    )

    page.add(menu_layout)

    menu_button.on_click = lambda e: menu_layout.toggle_navigation()


ft.app(target=main)
