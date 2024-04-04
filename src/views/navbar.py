import flet as ft

from flet import *

def NavBar(page, ft=ft):

    def changetab(e):
        my_index = e.control.selected_index
        pagina = page.go('/galeria') if my_index == 0 else False
        pagina = page.go('/resultado') if my_index == 1 else False
        pagina = page.go('/informacao') if my_index == 2 else False

        return pagina

    NavBar = ft.NavigationBar(
        on_change= lambda e:  page.go('/galeria') if e.control.selected_index == 0 else page.go('/resultado') if e.control.selected_index == 1 else page.go('/informacao') if e.control.selected_index == 2 else False, 
        destinations=[
            
            ft.NavigationDestination(icon = icons.IMAGE_SEARCH, label = "Galeria"),# button_click= lambda _: page.go('/galeria')),
            ft.NavigationDestination(icon = icons.FILE_OPEN, label = "Resultado"), #selected_icon_content= lambda _: page.go('/resultado')),
            ft.NavigationDestination(icon = icons.INFO_ROUNDED, label = "Informação"), #selected_icon_content= lambda _: page.go('/informacao')),
            # ft.NavigationDestination(icon = icons.IMAGE_SEARCH, on_click=lambda _: page.go('/')),
            # ft.NavigationDestination(icon = icons.FILE_OPEN, label = "Resultado"),
            # ft.NavigationDestination(icon = icons.INFO_ROUNDED, label="Informação"),
        ],
    )

    return NavBar
