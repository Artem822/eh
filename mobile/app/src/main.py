import flet as ft
from alchemy import News, Session, Events, Employees
from datetime import datetime
event_index = 1
news_index = 1

def main(page: ft.Page):
    page.title = "💀"
    main_content = ft.Column()
    page.padding = 0
    with Session() as session:
        global news_title1, news_title2, news_title3,news_desc1,news_desc2,news_desc3,news_date1,news_date2,news_date3,event_title,event_desc,event_date,event_author
        news_title1 = ft.Text(value=session.query(News).where(News.id==news_index).first().title)
        news_title2 = ft.Text(session.query(News).where(News.id==news_index+1).first().title)
        news_title3 = ft.Text(session.query(News).where(News.id==news_index+2).first().title)
        news_desc1 = ft.Text(session.query(News).where(News.id==news_index).first().description)
        news_desc2 = ft.Text(session.query(News).where(News.id==news_index+1).first().description)
        news_desc3 = ft.Text(session.query(News).where(News.id==news_index+2).first().description)
        news_date1 = ft.Text(session.query(News).where(News.id==news_index).first().date)
        news_date2 = ft.Text(session.query(News).where(News.id==news_index+1).first().date)
        news_date3 = ft.Text(session.query(News).where(News.id==news_index+2).first().date)
        event_employee_id = session.query(Events).where(Events.id==event_index).first().main_employee_id
        event_title = ft.Text(value=session.query(Events).where(Events.id==event_index).first().title, size=18)
        event_desc= ft.Text(value=session.query(Events).where(Events.id==event_index).first().description)
        event_date = ft.Text(value=  session.query(Events).where(News.id==event_index).first().date_since.date())
        event_author = ft.Text(session.query(Employees).where(Employees.id==event_employee_id).first().username, no_wrap=True)
    
    def click(e):
        # e.control.content.value
        print(news_index)
 
    def down(e):
        with Session() as session:
            global news_index
            news_index += 3
            try:
                news_title1.value = session.query(News).where(News.id==news_index).first().title
                news_desc1.value = session.query(News).where(News.id==news_index).first().description
                news_date1.value = session.query(News).where(News.id==news_index).first().date
                try:
                    news_title2.value = session.query(News).where(News.id==news_index+1).first().title
                    news_desc2.value = session.query(News).where(News.id==news_index+1).first().description
                    news_date2.value = session.query(News).where(News.id==news_index+1).first().date
                    news_2.visible = True
                    try:
                        news_title3.value = session.query(News).where(News.id==news_index+2).first().title
                        news_desc3.value = session.query(News).where(News.id==news_index+2).first().description
                        news_date3.value = session.query(News).where(News.id==news_index+2).first().date
                        news_3.visible = True
                    except:
                        news_3.visible=False
                        down_arrow.visible=False
                except:
                    news_2.visible=False
                    news_3.visible=False
                    down_arrow.visible=False
            except:
                news_1.visible=False
                news_2.visible=False
                news_3.visible=False
                down_arrow.visible=False
            up_arrow.visible = True
            try:
                session.query(News).where(News.id==news_index+3).first().title
            except:
                down_arrow.visible=False
            page.update()
        
    def up(e):
        with Session() as session:
            global news_index
            news_index -= 3
            try:
                news_title1.value = session.query(News).where(News.id==news_index).first().title
                news_desc1.value = session.query(News).where(News.id==news_index).first().description
                news_date1.value = session.query(News).where(News.id==news_index).first().date
                try:
                    news_title2.value = session.query(News).where(News.id==news_index+1).first().title
                    news_desc2.value = session.query(News).where(News.id==news_index+1).first().description
                    news_date2.value = session.query(News).where(News.id==news_index+1).first().date
                    news_2.visible = True
                    try:
                        news_title3.value = session.query(News).where(News.id==news_index+2).first().title
                        news_desc3.value = session.query(News).where(News.id==news_index+2).first().description
                        news_date3.value = session.query(News).where(News.id==news_index+2).first().date
                        news_3.visible = True
                    except:
                        news_3.visible=False
                        down_arrow.visible=False
                except:
                    news_2.visible=False
                    news_3.visible=False
                    down_arrow.visible=False
            except:
                news_1.visible=False
                news_2.visible=False
                news_3.visible=False
                down_arrow.visible=False
            try:
                session.query(News).where(News.id==news_index-1).first().title
            except:
                up_arrow.visible=False
            page.update()
            down_arrow.visible = True   
            page.update()
            
    def right(e):
        with Session() as session:
            global event_index
            event_index += 1
            left_arrow.visible = True
            try:
                session.query(Events).where(Events.id==event_index+1).first().title
            except:
                right_arrow.visible=False
            
            event_title.value = session.query(Events).where(Events.id==event_index).first().title
            event_desc.value = session.query(Events).where(Events.id==event_index).first().description
            event_date.value = session.query(Events).where(Events.id==event_index).first().date_since.date()
            event_employee_id = session.query(Events).where(Events.id==event_index).first().main_employee_id
            event_author.value = session.query(Employees).where(Employees.id==event_employee_id).first().username
            page.update()
        
    
    def left(e):
        with Session() as session:
            global event_index
            event_index -= 1
            right_arrow.visible = True
            try:
                session.query(Events).where(Events.id==event_index-1).first().title
            except:
                left_arrow.visible=False
            
            event_title.value = session.query(Events).where(Events.id==event_index).first().title
            event_desc.value = session.query(Events).where(Events.id==event_index).first().description
            event_date.value = session.query(Events).where(Events.id==event_index).first().date_since.date()
            event_employee_id = session.query(Events).where(Events.id==event_index).first().main_employee_id
            event_author.value = session.query(Employees).where(Employees.id==event_employee_id).first().username
            page.update()
            
    add_1 = ft.GestureDetector(content=ft.Text('+'), on_tap=click)
    add_2 = ft.GestureDetector(content=ft.Text('+'), on_tap=click)
    add_3 = ft.GestureDetector(content=ft.Text('+'), on_tap=click)
    minus_1 = ft.GestureDetector(content=ft.Text('-'), on_tap=click)
    minus_2 = ft.GestureDetector(content=ft.Text('-'), on_tap=click)
    minus_3 =ft.GestureDetector(content=ft.Text('-'), on_tap=click)
    up_arrow =ft.IconButton(icon=ft.icons.ARROW_UPWARD, visible=False, on_click=up)
    down_arrow = ft.IconButton(icon=ft.icons.ARROW_DOWNWARD, on_click=down)
    right_arrow =ft.IconButton(icon=ft.icons.ARROW_FORWARD, on_click=right)
    left_arrow = ft.IconButton(icon=ft.icons.ARROW_BACK, visible=False, on_click=left)
    news_1 = ft.Container(ft.Row(controls=[ft.Image(src=f"e.jpg", height=50, width=50), ft.Column([news_title1, ft.Column([news_desc1], scroll=True,height=50,width=200, expand=False,), ft.Container(ft.Row([ft.Container(ft.Row([add_1, ft.Text('10'),minus_1])), news_date1]))])]), bgcolor=ft.colors.GREEN, width=300, adaptive=True, border_radius=ft.border_radius.all(10))
    news_2 = ft.Container(ft.Row(controls=[ft.Image(src=f"e.jpg", height=50, width=50), ft.Column([news_title2, ft.Column([news_desc2], scroll=True,height=50,width=200, expand=False,), ft.Container(ft.Row([ft.Container(ft.Row([add_2, ft.Text('10'),minus_2])), news_date2]))])]), bgcolor=ft.colors.GREEN, width=300, adaptive=True,border_radius=ft.border_radius.all(10))
    news_3 = ft.Container(ft.Row(controls=[ft.Image(src=f"e.jpg", height=50, width=50), ft.Column([news_title3, ft.Column([news_desc3], scroll=True,height=50,width=200, expand=False,), ft.Container(ft.Row([ft.Container(ft.Row([add_3, ft.Text('10'),minus_3])), news_date3]))])]), bgcolor=ft.colors.GREEN, width=300, adaptive=True,border_radius=ft.border_radius.all(10))
    event = ft.Container(ft.Row([left_arrow,ft.Container(ft.Column([event_title, event_desc, ft.Row([event_date, event_author],scroll=True, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)], alignment=ft.MainAxisAlignment.CENTER),border_radius=ft.border_radius.all(10), bgcolor=ft.colors.GREEN, width=200, height=250), right_arrow], width=400))


    def change_tab1(e):
        main_content.controls = [ft.Container(ft.Column(controls=[up_arrow,news_1, news_2, news_3, down_arrow]), adaptive=True)]
        news_button.bgcolor = ft.colors.RED
        events_button.bgcolor = ft.colors.YELLOW
        page.update()
   
    def change_tab2(e):
        main_content.controls = [ft.Container(ft.Column(controls=[event]))]
        news_button.bgcolor = ft.colors.YELLOW
        events_button.bgcolor = ft.colors.RED
        page.update()
   
    news_button =  ft.ElevatedButton("Новости", on_click=change_tab1, bgcolor=ft.colors.YELLOW)
    events_button = ft.ElevatedButton("События", on_click=change_tab2, bgcolor=ft.colors.YELLOW) 
    tab_buttons = ft.Container(ft.Row(
        controls=[
            news_button,
            events_button,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
    ))
    def page_add():
        page.add(ft.Container(
            ft.Column(
                controls=[ft.Container(tab_buttons, padding=10),
                    ft.Container(main_content, alignment=ft.alignment.center, adaptive=True),  
                ],
                expand=True
            
            ), bgcolor='#e7fed9',expand=True      
        ))
    page_add()
ft.app(target=main)