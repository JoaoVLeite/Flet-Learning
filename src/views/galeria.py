import flet as ft

def Galeria(page, ft=ft):
    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Text(
                        "Você esta na galeria",
                        size=50
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
    )

    return content