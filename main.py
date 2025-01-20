from PySide6 import QtWidgets
import sys
from MainWindow import Ui_MainWindow
from sqlalchemy import  MetaData, Table, select
from alchemy import Session, engine
from AddUser import Ui_Dialog_add
from datetime import datetime
from SeeInfo import Ui_Dialog_SeeInfo

class SeeInfo(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_SeeInfo()
        self.ui.setupUi(self)
        self.setWindowTitle('Информация о пользователе')
        self.setFixedSize(463, 702)
        self.ui.pushButton.clicked.connect(self.save)
        with Session() as session:
            metadata = MetaData()
            self.employee_table = Table('models_employee', metadata, autoload_with=engine)
            self.organization_table = Table('models_organization', metadata, autoload_with=engine)
            self.organizations = session.execute(select(self.organization_table)).all()
            self.organizations = sorted(self.organizations)
            self.position_table = Table('models_position', metadata, autoload_with=engine)
            self.positins = session.execute(select(self.position_table)).all()
            self.cabinet_table = Table('models_cabinet', metadata, autoload_with=engine)
            for i in self.organizations:
                self.ui.Organization.addItem(i.title)
            for i in self.positins:
                self.ui.Position.addItem(i.title)
        self.add_info()
        
        
    def add_info(self):
        with Session() as session:
            employee = session.execute(select(self.employee_table).where(self.employee_table.c.username==name)).all()
            for i in employee:
                org = session.execute(select(self.organization_table).where(self.organization_table.c.id==i.organization_id)).all()
                pos = session.execute(select(self.position_table).where(self.position_table.c.id==i.position_id_id)).all()
                org_index = self.ui.Organization.findText(org[0][1])
                pos_index = self.ui.Position.findText(pos[0][1])
                self.ui.Birthday.setText(str(i.birthday))
                self.ui.Cabinet.setText(str(i.cabinet_id_id))
                self.ui.Full_name.setText(str(i.username))
                self.ui.Mail.setText(str(i.email))
                self.ui.Mobile_phone.setText(str(i.personal_phone))
                self.ui.Organization.setCurrentIndex(org_index)
                self.ui.Position.setCurrentIndex(pos_index)
                self.ui.Password.setText(str(i.password))
                self.ui.Username.setText(str(i.username))
                self.ui.Work_phone.setText(str(i.work_phone))
    
    def save(self):
        pass
            
class AddUser(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_add()
        self.ui.setupUi(self)
        self.setWindowTitle('Добавление пользователя')
        self.setFixedSize(463, 702)
        self.ui.pushButton.clicked.connect(self.AddUsers)  
        with Session() as session:
            metadata = MetaData()
            self.organization_table = Table('models_organization', metadata, autoload_with=engine)
            self.organizations = session.execute(select(self.organization_table)).all()
            self.organizations = sorted(self.organizations)
            self.position_table = Table('models_position', metadata, autoload_with=engine)
            self.positins = session.execute(select(self.position_table)).all()
            self.position_table = Table('models_position', metadata, autoload_with=engine)
            self.positins = session.execute(select(self.position_table)).all()
            self.employee_table = Table('models_employee', metadata, autoload_with=engine)
            self.cabinet_table = Table('models_cabinet', metadata, autoload_with=engine)
        for i in self.organizations:
            self.ui.Organization.addItem(i.title)
        for i in self.positins:
            self.ui.Position.addItem(i.title)
    
    def AddUsers(self):
        with Session() as session:
            org_id = session.execute(select(self.organization_table).where(self.organization_table.c.title==self.ui.Organization.currentText())).all()[0]
            pos_id = session.execute(select(self.position_table).where(self.position_table.c.title==self.ui.Position.currentText())).all()[0]
            try:
                cab_id = session.execute(select(self.cabinet_table).where(self.cabinet_table.c.title==self.ui.Cabinet.text())).all()[0]
            except:
                new_cab = self.cabinet_table.insert().values(title=self.ui.Cabinet.text())
                session.execute(new_cab)
                session.commit()
                cab_id = session.execute(select(self.cabinet_table).where(self.cabinet_table.c.title==self.ui.Cabinet.text())).all()[0]
            try:
                new_employee = self.employee_table.insert().values(first_name=str(self.ui.Full_name.text()).split()[0], last_name=str(self.ui.Full_name.text()).split()[1], patronymic=str(self.ui.Full_name.text()).split()[2],
                                                    birthday=self.ui.Birthday.text(), personal_phone=self.ui.Mobile_phone.text(), cabinet_id_id=cab_id[0], email=self.ui.Mail.text(), position_id_id=pos_id[0],
                                                    username=self.ui.Username.text(), password=self.ui.Password.text(), is_superuser=False, is_staff=False, is_active=True, date_joined=datetime.now(), organization_id=org_id[0],
                                                    work_phone=self.ui.Work_phone.text())
                session.execute(new_employee)
                session.commit()
                dlg = QtWidgets.QMessageBox(self)
                dlg.setWindowTitle("Успешно")
                dlg.setText("Пользователь успешно добавлен")
                button = dlg.exec()
            except:
                dlg = QtWidgets.QMessageBox(self)
                dlg.setWindowTitle("Ошибка")
                dlg.setText("При создании пользователя произошла ошибка")
                button = dlg.exec()
            
        
        
class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.employee_add_button.clicked.connect(self.add)
        self.ui.listWidget.clicked.connect(self.seeinfo)
        with Session() as session:
            metadata = MetaData()
            self.organization_table = Table('models_organization', metadata, autoload_with=engine)
            self.organizations = session.execute(select(self.organization_table)).all()
            self.organizations = sorted(self.organizations)
            self.subdivision_table = Table('models_subdivision', metadata, autoload_with=engine)
            self.subdivisions = session.execute(select(self.subdivision_table)).all()
            self.subdivisions = sorted(self.subdivisions)
            self.organization_subdivision_table = Table('models_organization_subdivisions', metadata, autoload_with=engine)
            self.organization_subdivisions = session.execute(select(self.organization_subdivision_table)).all()
            self.employee_table = Table('models_employee', metadata, autoload_with=engine)
            self.all_employees = session.execute(select(self.employee_table)).all()
            self.subsubdivision_table = Table('models_subsubdivision', metadata, autoload_with=engine)
            self.subsubdivisions = session.execute(select(self.subsubdivision_table)).all()
            self.subsubdivisions = sorted(self.subsubdivisions)
            self.subdivision_subsubdivision_table = Table('models_subdivision_sub_sub_division', metadata, autoload_with=engine)
            self.subdivision_subsubdivisions = session.execute(select(self.subdivision_subsubdivision_table)).all()
        self.add_all()
        self.ui.treeWidget_departments.itemClicked.connect(self.click)
        
    def seeinfo(self, e):
        global name
        name = e.data()
        dlg = SeeInfo(self)
        dlg.exec()   
        
    def add_all(self):
        with Session() as session:
            for organization in self.organizations:
                root = QtWidgets.QTreeWidgetItem(self.ui.treeWidget_departments, [organization.title])                  
                subdiv_id = session.execute(select(self.organization_subdivision_table).where(self.organization_subdivision_table.c.organization_id == organization.id)).all() 
                for subdivision in subdiv_id:
                    subdiv = session.execute(select(self.subdivision_table).where(self.subdivision_table.c.id == subdivision.subdivision_id)).all()
                    child = QtWidgets.QTreeWidgetItem(root, [subdiv[0][1]])
                    subsubdiv_id = session.execute(select(self.subdivision_subsubdivision_table).where(self.subdivision_subsubdivision_table.c.subdivision_id == subdivision.subdivision_id)).all()        
                    for i in subsubdiv_id:
                        subsubdiv = session.execute(select(self.subsubdivision_table).where(self.subsubdivision_table.c.id == i[2])).all()
                        child2 = QtWidgets.QTreeWidgetItem(child, [subsubdiv[0][1]])
                             
                    
    def add(self):
        dlg = AddUser(self)
        dlg.exec()          
                        
            
    def click(self):
        self.ui.listWidget.clear()
        getSelected = self.ui.treeWidget_departments.selectedItems()
        if getSelected:
            name = getSelected[0].text(0)
        with Session() as session:
            try:
                org = Session().execute(select(self.organization_table).where(self.organization_table.c.title==name)).all()
                for i in Session().execute(select(self.employee_table).where(self.employee_table.c.organization_id == org[0][0])).all():
                    self.ui.listWidget.addItem(QtWidgets.QListWidgetItem(str(f"{i.last_name} {i.first_name} {i.patronymic}")))
            except:
                try:
                    subdiv = Session().execute(select(self.subdivision_table).where(self.subdivision_table.c.title==name)).all()
                    for i in Session().execute(select(self.employee_table).where(self.employee_table.c.subdivision_id == subdiv[0][0])).all():
                        self.ui.listWidget.addItem(QtWidgets.QListWidgetItem(str(f"{i.last_name} {i.first_name} {i.patronymic}")))
                except:
                    subsubdiv = Session().execute(select(self.subsubdivision_table).where(self.subsubdivision_table.c.title==name)).all()
                    for i in Session().execute(select(self.employee_table).where(self.employee_table.c.sub_sub_division_id == subsubdiv[0][0])).all():
                        self.ui.listWidget.addItem(QtWidgets.QListWidgetItem(str(f"{i.last_name} {i.first_name} {i.patronymic}")))
        
      
        


    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = UI()
    win.show()
    app.exec()