import flet as ft

def Informacao(page, ft=ft):
    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Text(
                        "Você esta na Informacao",
                        size=50
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
    )

    return content