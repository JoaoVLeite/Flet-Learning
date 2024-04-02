import flet

from flet import *
from functools import partial
import time

# Sidebar Class
class MenuNavBar(UserControl):
    def __init__(self):
        super().__init__()

    # Adiciona foco em qual item do menu esta
    def HighLight(self, e):
        if e.data == "true":
            e.control.bgcolor = "white10"
            e.control.update()

            #Altera a cor do icone e text
            e.control.content.controls[0].icon_color = "white"

            e.control.content.controls[1].color = "white"
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()

            e.control.content.controls[0].icon_color = "white54"

            e.control.content.controls[1].color = "white54"
            e.control.content.update()

    def LogoEmpresa(self, logo: str):
        return Container(
            
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor='bluegrey900',
                        alignment=alignment.center,
                        border_radius=8,
                        content=Image(
                            src=logo,
                        )
                    ),
                ]
            )
        )
    
    def IconesPages(self, icon_name: str, text: str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color="white54",
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={
                                "": "transparent"
                            },

                        ),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]
            ),
        )
    
    def build(self):
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                horizontal_alignment="center",
                controls=[
                    self.LogoEmpresa("d:/GitHub/Flet-Learning/src/imagens/logo.png"),
                    # add a divider
                    Divider(height=5, color="transparent"),
                    self.IconesPages(icons.IMAGE_SEARCH, "Analisar Imagem"),
                    self.IconesPages(icons.FILE_OPEN, "Resultado"),
                    self.IconesPages(icons.SAVE, "Salvar"),

                ]
            ),
            )


#main function
def main(page: Page):
    #title
    page.title = "Menu"

    #alignemnts
    page.horizontal_alignment='left'
    page.vertical_alignment='center'

    #Animação NavBar
    # def AnimateNavBar(e):

    #     if page.controls[0].width != 62:
    #         for item in(
    #             page.controls[0]

    #             .content.controls[0]
    #             .content.controls[0]
    #             .content.controls[0]
    #             .content.controls[0]
    #             .controls[:]
    #         ):
    #             item.opacity = (0)
    #             item.update()
                
    #         for items in page.controls[0].content.controls[3:]:
    #             if isinstance(items, Container):
    #                 item.content.controls[1].opacity = 0
    #                 item.content.update()
    #         pass

    #     pass     
        
    #add class to page
    page.add(
        Container(
            width = 200,
            # height = 580,
            bgcolor = 'black',
            border_radius = 10,
            animate=animation.Animation(500, 'decelerate'),
            alignment= alignment.center,
            padding=10,
            content = MenuNavBar(),
        )
    )

    page.update()

if __name__ == "__main__":
    flet.app(target=main)


