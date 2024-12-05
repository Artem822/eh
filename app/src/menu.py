import flet as ft
def name(e: ft.Page):
    e.clean()
    e.window.width = 500
    e.window.height = 500
    e.add(ft.Text('Hello', text_align=ft.TextAlign.CENTER))
    


