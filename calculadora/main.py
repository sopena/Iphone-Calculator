import flet as ft

class CalculatorApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.number_style = ft.ButtonStyle(bgcolor= "#2A2A2C", )
        self.operators_style = ft.ButtonStyle(bgcolor= "#FF9F0A")
        self.extra_style = ft.ButtonStyle(bgcolor= "#5C5C5F")
        self.display = ft.Container(
            content= ft.Text("0", text_align="end", weight="bold", size="40"),
            width=260,
            height=100,
            alignment=ft.alignment.bottom_right

        )
        self.controls = [
            ft.Row(
                controls = [
                    self.display
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Column(
                controls = [
                    ft.Row(
                        controls= [
                            ft.ElevatedButton("AC", style=self.extra_style, width=70),
                            ft.ElevatedButton("+/-", style=self.extra_style, width=70),
                            ft.ElevatedButton("%", style=self.extra_style, width=70),
                            ft.ElevatedButton("/", style=self.operators_style, width=70),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls= [
                            ft.ElevatedButton("7", style=self.number_style, width=70),
                            ft.ElevatedButton("8", style=self.number_style, width=70),
                            ft.ElevatedButton("9", style=self.number_style, width=70),
                            ft.ElevatedButton("X", style=self.operators_style, width=70),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls= [
                            ft.ElevatedButton("4", style=self.number_style, width=70),
                            ft.ElevatedButton("5", style=self.number_style, width=70),
                            ft.ElevatedButton("6", style=self.number_style, width=70),
                            ft.ElevatedButton("-", style=self.operators_style, width=70),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls= [
                            ft.ElevatedButton("1", style=self.number_style, width=70),
                            ft.ElevatedButton("2", style=self.number_style, width=70),
                            ft.ElevatedButton("3", style=self.number_style, width=70),
                            ft.ElevatedButton("+", style=self.operators_style, width=70),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        controls= [
                            ft.IconButton(icon=ft.icons.CALCULATE, style=self.number_style, width=70),
                            ft.ElevatedButton("0", style=self.number_style, width=70),
                            ft.ElevatedButton(",", style=self.number_style, width=70),
                            ft.ElevatedButton(text="=", style=self.operators_style, width=70),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
            ),
        ]


def main(page: ft.Page):
    page.title = "Scientific Calculator"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 400
    page.window.height = 800
    page.update()

    App = CalculatorApp()
    
    page.add(App)

if __name__=="__main__":
    ft.app(main)