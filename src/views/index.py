import flet as ft
from flet import *

from router import Router
from navbar import NavBar

def main(page: ft.Page):
    #page.theme_mode = "dark"

    page.navigation_bar= NavBar(page, ft)
    myRoutes = Router(page,ft)

    page.on_route_change = myRoutes.route_change

    page.add(
        myRoutes.body
    )

    page.go("/galeria")







ft.app(target=main, assets_dir="assets")