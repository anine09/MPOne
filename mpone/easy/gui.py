import flet as ft


def main(page: ft.Page):
    page.title = "MPOne"
    page.window_width = 1100
    page.window_height = 720

    
    main_AppBar = ft.AppBar(
        # leading=ft.Image(
        #     src="logo7.png",
        #     width=50,
        #     height=10,
        #     fit=ft.ImageFit.SCALE_DOWN,
        # ),
        leading=ft.Icon(name=ft.icons.LOGO_DEV),
        leading_width=60,
        title=ft.Text("MPOne Easy GUI Project"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )
    page.appbar = main_AppBar

    main_NavigationRai = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.LAN, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.INFO_OUTLINE,
                selected_icon=ft.icons.INFO,
                label="Info",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.INSERT_CHART_OUTLINED,
                selected_icon=ft.icons.INSERT_CHART,
                label="Chart",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.TABLE_CHART_OUTLINED,
                selected_icon=ft.icons.TABLE_CHART,
                label="Tabular",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.HELP_OUTLINE,
                selected_icon=ft.icons.HELP,
                label="Help",
            )
        ],
    )


    page.add(
        ft.Row(
            [
                main_NavigationRai,
                ft.VerticalDivider(width=1),
            ],
            expand=True,
        ),
    )


ft.app(
    target=main,
    assets_dir="assets",

)