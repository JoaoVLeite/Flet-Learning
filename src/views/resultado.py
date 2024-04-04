import flet as ft

def Resultado(page, ft=ft):
    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Text(
                        "Você esta no Resultado",
                        size=50
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
    )

    return content