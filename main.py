import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Propinas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    monto = ft.TextField(label="Monto de la cuenta", width=200)
    propina = ft.Text(value="Propina: $0")
    total = ft.Text(value="Total: $0")

    def calcular(e):
        try:
            montOO = float(monto.value)
            propinAA = slider.value
            propinaCalculada = montOO * (propinAA / 100)
            totalCalculado = montOO + propinaCalculada
            propina.value = "Propina: $" + str(round(propinaCalculada, 2))
            total.value = "Total: $" + str(round(totalCalculado, 2))
            page.update()
        except:
            propina.value = "Error"
            total.value = ""
            page.update()

    slider = ft.Slider(min=5, max=40, divisions=7, value=10, label="{value}%", on_change=calcular)

    page.add(
        ft.Column(
            [
                monto,
                ft.Text("Porcentaje de propina:"),
                slider,
                propina,
                total,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)