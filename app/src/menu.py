import flet as ft
def name(e: ft.Page):
    e.clean()
    e.title = 'Панель'
    e.window.width = 500
    e.window.height = 500
    history_button = ft.ElevatedButton('Просмотреть отчеты')
    tests_button = ft.ElevatedButton('Тестирование')
    statistics_button = ft.ElevatedButton('Статистика')
    e.add(ft.Column([history_button,tests_button,statistics_button], alignment=ft.MainAxisAlignment.CENTER))
    


