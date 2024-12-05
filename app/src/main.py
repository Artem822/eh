import flet as ft
from menu import name

def main(page: ft.Page):

    def test(e):
        if login_entery.value != '1' or password_entery.value != '1':
            error_text.value = 'Введены не корректные данные'
            login_entery.border_color = ft.colors.RED
            password_entery.border_color = ft.colors.RED
            page.update()
        else:
            page.clean()
            page.title = ':)'
            page.window.width = 195
            page.window.height = 200
            username = ft.Text('Здравствуйте: admin', weight='bold')
            history_button = ft.ElevatedButton('Просмотреть отчеты')
            tests_button = ft.ElevatedButton('Тестирование')
            statistics_button = ft.ElevatedButton('Статистика')
            page.add(ft.Column([username,history_button,tests_button,statistics_button], alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER))


    page.title = 'Вход в аккаунт'
    page.window.height= 310
    page.window.width = 360
    page.window.resizable = False
    page.window.maximizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    login_text = ft.Text('Вход',weight='bold', size=24)
    login_entery = ft.TextField(label='Логин',width=300)
    password_entery = ft.TextField(label='Пароль',width=300, password=True, can_reveal_password=True)
    login_button=ft.ElevatedButton('Войти', width=300, on_click=test, color=ft.colors.WHITE60)
    error_text = ft.Text('', color=ft.colors.RED)
    page.add(ft.Row(
        [
            ft.Column([login_text, login_entery, password_entery ,error_text, login_button])
        ], alignment=ft.MainAxisAlignment.CENTER)
    )
    


ft.app(main)
