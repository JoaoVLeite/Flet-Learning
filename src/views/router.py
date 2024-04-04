import flet as ft
from flet import *

# Views

from galeria import Galeria
from resultado import Resultado
from informacao import Informacao

class Router:

    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/galeria": Galeria(page),
            "/resultado": Resultado(page),
            "/informacao": Informacao(page)
        }
        self.body = ft.Container(content=self.routes['/galeria'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
