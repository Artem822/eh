import flet as ft

def main(page: ft.Page):
    page.title = "💀"
    main_content = ft.Column()
    page.padding = 0
    event_index = 1
    global news_index
    news_index = 1
    
    def click1(e):
        # e.control.content.value
        print(news_index)
    def click2(e):
        print(news_index+1)
    def click3(e):
        print(news_index+2)
    add_1 = ft.GestureDetector(content=ft.Text('+'), on_tap=click1)
    add_2 = ft.GestureDetector(content=ft.Text('+'), on_tap=click2)
    add_3 = ft.GestureDetector(content=ft.Text('+'), on_tap=click3)
    minus_1 = ft.GestureDetector(content=ft.Text('-'), on_tap=click1)
    minus_2 = ft.GestureDetector(content=ft.Text('-'), on_tap=click2)
    minus_3 =ft.GestureDetector(content=ft.Text('-'), on_tap=click3)
    up_arrow =ft.IconButton(icon=ft.icons.ARROW_UPWARD, visible=False)
    down_arrow = ft.IconButton(icon=ft.icons.ARROW_DOWNWARD,visible=False)
    right_arrow =ft.IconButton(icon=ft.icons.ARROW_FORWARD,visible=False)
    left_arrow = ft.IconButton(icon=ft.icons.ARROW_BACK, visible=False)
    news_1 = ft.Container(ft.Row(controls=[ft.Image(src=f"e.jpg", height=50, width=50), ft.Column([ft.Text('Название новости'), ft.Column([ft.Text('Пример описания')], scroll=True,height=50,width=200, expand=False,), ft.Container(ft.Row([ft.Container(ft.Row([add_1, ft.Text('10'),minus_1])), ft.Text('16.02.2025')]))])]), bgcolor=ft.colors.GREEN, width=300, adaptive=True, border_radius=ft.border_radius.all(10))
    news_2 = ft.Container(ft.Row(controls=[ft.Image(src=f"e.jpg", height=50, width=50), ft.Column([ft.Text('Название новости'), ft.Column([ft.Text('Пример описания')], scroll=True,height=50,width=200, expand=False,), ft.Container(ft.Row([ft.Container(ft.Row([add_2, ft.Text('10'),minus_2])), ft.Text('16.02.2025')]))])]), bgcolor=ft.colors.GREEN, width=300, adaptive=True,border_radius=ft.border_radius.all(10))
    news_3 = ft.Container(ft.Row(controls=[ft.Image(src=f"e.jpg", height=50, width=50), ft.Column([ft.Text('Название новости'), ft.Column([ft.Text('Пример описания')], scroll=True,height=50,width=200, expand=False,), ft.Container(ft.Row([ft.Container(ft.Row([add_3, ft.Text('10'),minus_3])), ft.Text('16.02.2025')]))])]), bgcolor=ft.colors.GREEN, width=300, adaptive=True,border_radius=ft.border_radius.all(10))
    event = ft.Container(ft.Row([left_arrow,ft.Container(ft.Column([ft.Text('Наименование', size=20), ft.Text('Краткий текст'), ft.Row([ft.Text('Дата'), ft.Text('Автор')], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)], alignment=ft.MainAxisAlignment.CENTER),border_radius=ft.border_radius.all(10), bgcolor=ft.colors.GREEN, width=300, height=250), right_arrow], width=400))


    def change_tab1(e):
        main_content.controls = [ft.Container(ft.Column(controls=[up_arrow,news_1, news_2, news_3,down_arrow]), adaptive=True)]
        news_button.bgcolor = ft.colors.RED
        events_button.bgcolor = ft.colors.YELLOW
        page.update()
   
    def change_tab2(e):
        main_content.controls = [ft.Container(ft.Column(controls=[event]))]
        news_button.bgcolor = ft.colors.YELLOW
        events_button.bgcolor = ft.colors.RED
        page.update()
   
    news_button =  ft.ElevatedButton("Новости", on_click=change_tab1, bgcolor=ft.colors.RED)
    events_button = ft.ElevatedButton("События", on_click=change_tab2, bgcolor=ft.colors.YELLOW) 
    tab_buttons = ft.Container(ft.Row(
        controls=[
            news_button,
            events_button,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
    ))
    
    page.add(ft.Container(
        ft.Column(
            controls=[ft.Container(tab_buttons, padding=10),
                ft.Container(main_content, alignment=ft.alignment.center, adaptive=True),  
            ],
            expand=True
        
        ), bgcolor='#e7fed9',expand=True      
    ))

ft.app(target=main)