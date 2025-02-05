from PySide6 import QtWidgets
import sys
from UI_py.MainWindow import Ui_MainWindow
from sqlalchemy import  MetaData, Table, select, update, delete
from alchemy import Session, engine
from UI_py.AddUser import Ui_Dialog_add
from datetime import datetime
from UI_py.SeeInfo import Ui_Dialog_SeeInfo
from sqlalchemy import asc
import pytz

class SeeInfo(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_SeeInfo()
        self.ui.setupUi(self)
        self.setWindowTitle('Информация о пользователе')
        self.ui.pushButton.clicked.connect(self.save)
        self.ui.pushButton_2.clicked.connect(self.delete)
        self.ui.comboBox.currentIndexChanged.connect(self.pupu)
        with Session() as session:
            metadata = MetaData()
            self.employee_table = Table('models_employee', metadata, autoload_with=engine)
            self.organization_table = Table('models_organization', metadata, autoload_with=engine)
            self.organizations = session.execute(select(self.organization_table)).all()
            self.organizations = sorted(self.organizations)
            self.position_table = Table('models_position', metadata, autoload_with=engine)
            self.positins = session.execute(select(self.position_table)).all()
            self.cabinet_table = Table('models_cabinet', metadata, autoload_with=engine)
            self.calendarskip_table = Table('models_calendarskip', metadata, autoload_with=engine)
            self.calendarskip_employees_table = Table('models_calendarskip_employees', metadata, autoload_with=engine)
            self.calendarvacation_table = Table('models_calendarvacation', metadata, autoload_with=engine)
            self.calendarvacation_employees_table = Table('models_calendarvacation_employees', metadata, autoload_with=engine)
            self.calendareducation_table = Table('models_calendareducation', metadata, autoload_with=engine)
            self.calendareducation_employees_table = Table('models_calendareducation_employees', metadata, autoload_with=engine)
            self.event_table = Table('models_event', metadata, autoload_with=engine)
            self.event_type_table = Table('models_eventtype', metadata, autoload_with=engine)
            
            for i in self.organizations:
                self.ui.Organization.addItem(i.title)
            for i in self.positins:
                self.ui.Position.addItem(i.title)
        self.add_info()
    
    def delete(self):
        with Session() as session:
            session.execute(delete(self.employee_table).where(self.employee_table.c.username==name))

            session.commit()
            self.close()
            
    def pupu(self, data):
        self.ui.tableWidget_2.setRowCount(0)
        with Session() as session:
            employee = session.execute(select(self.employee_table).where(self.employee_table.c.username==str(name))).first()
            educations = session.execute(select(self.calendareducation_employees_table).where(self.calendareducation_employees_table.c.employee_id==employee.id)).all()
            for i in educations:
                education = session.execute(select(self.calendareducation_table).where(self.calendareducation_table.c.id==i.calendareducation_id)).first()
                event = session.execute(select(self.event_table).where(self.event_table.c.id==education.event_id_id)).first()
                if data == 1 and event.date_until < pytz.UTC.localize(datetime.now()):
                    currentRowCount = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(currentRowCount)
                    self.ui.tableWidget_2.setItem(currentRowCount, 0, QtWidgets.QTableWidgetItem(str(event.id)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 1, QtWidgets.QTableWidgetItem(str(event.date_since)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 2, QtWidgets.QTableWidgetItem(str(event.date_until)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 3, QtWidgets.QTableWidgetItem(str(event.description)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 4, QtWidgets.QTableWidgetItem(str(event.status)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 5, QtWidgets.QTableWidgetItem(str(event.education_id_id)))
                    type = session.execute(select(self.event_type_table).where(self.event_type_table.c.id==event.event_type_id_id)).first()
                    self.ui.tableWidget_2.setItem(currentRowCount, 6, QtWidgets.QTableWidgetItem(str(type.title)))
                if data == 2 and event.date_since < pytz.UTC.localize(datetime.now()) < event.date_until:
                    currentRowCount = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(currentRowCount)
                    self.ui.tableWidget_2.setItem(currentRowCount, 0, QtWidgets.QTableWidgetItem(str(event.id)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 1, QtWidgets.QTableWidgetItem(str(event.date_since)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 2, QtWidgets.QTableWidgetItem(str(event.date_until)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 3, QtWidgets.QTableWidgetItem(str(event.description)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 4, QtWidgets.QTableWidgetItem(str(event.status)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 5, QtWidgets.QTableWidgetItem(str(event.education_id_id)))
                    type = session.execute(select(self.event_type_table).where(self.event_type_table.c.id==event.event_type_id_id)).first()
                    self.ui.tableWidget_2.setItem(currentRowCount, 6, QtWidgets.QTableWidgetItem(str(type.title)))
                if data == 3 and event.date_since > pytz.UTC.localize(datetime.now()):
                    currentRowCount = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(currentRowCount)
                    self.ui.tableWidget_2.setItem(currentRowCount, 0, QtWidgets.QTableWidgetItem(str(event.id)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 1, QtWidgets.QTableWidgetItem(str(event.date_since)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 2, QtWidgets.QTableWidgetItem(str(event.date_until)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 3, QtWidgets.QTableWidgetItem(str(event.description)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 4, QtWidgets.QTableWidgetItem(str(event.status)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 5, QtWidgets.QTableWidgetItem(str(event.education_id_id)))
                    type = session.execute(select(self.event_type_table).where(self.event_type_table.c.id==event.event_type_id_id)).first()
                    self.ui.tableWidget_2.setItem(currentRowCount, 6, QtWidgets.QTableWidgetItem(str(type.title)))
                if data == 0:
                    currentRowCount = self.ui.tableWidget_2.rowCount()
                    self.ui.tableWidget_2.insertRow(currentRowCount)
                    self.ui.tableWidget_2.setItem(currentRowCount, 0, QtWidgets.QTableWidgetItem(str(event.id)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 1, QtWidgets.QTableWidgetItem(str(event.date_since)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 2, QtWidgets.QTableWidgetItem(str(event.date_until)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 3, QtWidgets.QTableWidgetItem(str(event.description)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 4, QtWidgets.QTableWidgetItem(str(event.status)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 5, QtWidgets.QTableWidgetItem(str(event.education_id_id)))
                    type = session.execute(select(self.event_type_table).where(self.event_type_table.c.id==event.event_type_id_id)).first()
                    self.ui.tableWidget_2.setItem(currentRowCount, 6, QtWidgets.QTableWidgetItem(str(type.title)))
                    
                
            
        
    def add_info(self):
        with Session() as session:
            employee = session.execute(select(self.employee_table).where(self.employee_table.c.username==str(name))).all()
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
                
                skips = session.execute(select(self.calendarskip_employees_table).where(self.calendarskip_employees_table.c.employee_id==i.id)).all()
                for id in skips:
                    currentRowCount = self.ui.tableWidget.rowCount()
                    skip = session.execute(select(self.calendarskip_table).where(self.calendarskip_table.c.id==id.calendarskip_id)).first()
                    self.ui.tableWidget.insertRow(currentRowCount)
                    self.ui.tableWidget.setItem(currentRowCount, 0, QtWidgets.QTableWidgetItem(str(skip.id)))
                    self.ui.tableWidget.setItem(currentRowCount, 1, QtWidgets.QTableWidgetItem(str(skip.date_since)))
                    self.ui.tableWidget.setItem(currentRowCount, 2, QtWidgets.QTableWidgetItem(str(skip.date_until)))

                    
                vacations = session.execute(select(self.calendarvacation_employees_table).where(self.calendarvacation_employees_table.c.employee_id==i.id)).all()
                for id in vacations:
                    currentRowCount = self.ui.tableWidget_3.rowCount()
                    vacation = session.execute(select(self.calendarvacation_table).where(self.calendarvacation_table.c.id==id.calendarvacation_id)).first()
                    self.ui.tableWidget_3.insertRow(currentRowCount)
                    self.ui.tableWidget_3.setItem(currentRowCount, 0, QtWidgets.QTableWidgetItem(str(vacation.id)))
                    self.ui.tableWidget_3.setItem(currentRowCount, 1, QtWidgets.QTableWidgetItem(str(vacation.date_since)))
                    self.ui.tableWidget_3.setItem(currentRowCount, 2, QtWidgets.QTableWidgetItem(str(vacation.date_until)))
                
                educations = session.execute(select(self.calendareducation_employees_table).where(self.calendareducation_employees_table.c.employee_id==i.id)).all()
                for id in educations:
                    currentRowCount = self.ui.tableWidget_2.rowCount()
                    education = session.execute(select(self.calendareducation_table).where(self.calendareducation_table.c.id==id.calendareducation_id)).first()
                    event = session.execute(select(self.event_table).where(self.event_table.c.id==education.event_id_id)).first()
                    self.ui.tableWidget_2.insertRow(currentRowCount)
                    self.ui.tableWidget_2.setItem(currentRowCount, 0, QtWidgets.QTableWidgetItem(str(event.id)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 1, QtWidgets.QTableWidgetItem(str(event.date_since)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 2, QtWidgets.QTableWidgetItem(str(event.date_until)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 3, QtWidgets.QTableWidgetItem(str(event.description)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 4, QtWidgets.QTableWidgetItem(str(event.status)))
                    self.ui.tableWidget_2.setItem(currentRowCount, 5, QtWidgets.QTableWidgetItem(str(event.education_id_id)))
                    type = session.execute(select(self.event_type_table).where(self.event_type_table.c.id==event.event_type_id_id)).first()
                    self.ui.tableWidget_2.setItem(currentRowCount, 6, QtWidgets.QTableWidgetItem(str(type.title)))

                    
                    
                
    
    def save(self):
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
                engine.execute(update(self.employee_table).where(self.employee_table.c.username==name).values(first_name=str(self.ui.Full_name.text()).split()[1], last_name=str(self.ui.Full_name.text()).split()[0], patronymic=str(self.ui.Full_name.text()).split()[2],
                                                            birthday=self.ui.Birthday.text(), personal_phone=self.ui.Mobile_phone.text(), cabinet_id_id=cab_id[0], email=self.ui.Mail.text(), position_id_id=pos_id[0],
                                                            username=self.ui.Username.text(), password=self.ui.Password.text(), is_superuser=False, is_staff=False, is_active=True, date_joined=datetime.now(), organization_id=org_id[0],
                                                            work_phone=self.ui.Work_phone.text()))
                session.flush()
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
                new_employee = self.employee_table.insert().values(first_name=str(self.ui.Full_name.text()).split()[1], last_name=str(self.ui.Full_name.text()).split()[0], patronymic=str(self.ui.Full_name.text()).split()[2],
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