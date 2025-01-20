# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog_SeeInfo(object):
    def setupUi(self, Dialog_add):
        if not Dialog_add.objectName():
            Dialog_add.setObjectName(u"Dialog_add")
        Dialog_add.resize(463, 702)
        Dialog_add.setStyleSheet(u"QWidget{\n"
"background-color:rgb(211, 211, 211)}")
        self.verticalLayout = QVBoxLayout(Dialog_add)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog_add)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color:white}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setStyleSheet(u"font: 600 24pt \"Segoe UI\";\n"
"color:black;\n"
"font-weight:bold")

        self.verticalLayout_3.addWidget(self.label)

        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        font = QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)

        self.verticalLayout_3.addWidget(self.label_25)

        self.Full_name = QLineEdit(self.frame_2)
        self.Full_name.setObjectName(u"Full_name")

        self.verticalLayout_3.addWidget(self.Full_name)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.verticalLayout_3.addWidget(self.label_19)

        self.Mobile_phone = QLineEdit(self.frame_2)
        self.Mobile_phone.setObjectName(u"Mobile_phone")

        self.verticalLayout_3.addWidget(self.Mobile_phone)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.verticalLayout_3.addWidget(self.label_21)

        self.Birthday = QLineEdit(self.frame_2)
        self.Birthday.setObjectName(u"Birthday")

        self.verticalLayout_3.addWidget(self.Birthday)

        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.verticalLayout_3.addWidget(self.label_20)

        self.Organization = QComboBox(self.frame_2)
        self.Organization.setObjectName(u"Organization")

        self.verticalLayout_3.addWidget(self.Organization)

        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.verticalLayout_3.addWidget(self.label_26)

        self.Position = QComboBox(self.frame_2)
        self.Position.setObjectName(u"Position")

        self.verticalLayout_3.addWidget(self.Position)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.label_2)

        self.Cabinet = QLineEdit(self.frame_2)
        self.Cabinet.setObjectName(u"Cabinet")

        self.verticalLayout_3.addWidget(self.Cabinet)

        self.label_27 = QLabel(self.frame_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.verticalLayout_3.addWidget(self.label_27)

        self.Work_phone = QLineEdit(self.frame_2)
        self.Work_phone.setObjectName(u"Work_phone")

        self.verticalLayout_3.addWidget(self.Work_phone)

        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.verticalLayout_3.addWidget(self.label_24)

        self.Mail = QLineEdit(self.frame_2)
        self.Mail.setObjectName(u"Mail")

        self.verticalLayout_3.addWidget(self.Mail)

        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.verticalLayout_3.addWidget(self.label_22)

        self.Username = QLineEdit(self.frame_2)
        self.Username.setObjectName(u"Username")

        self.verticalLayout_3.addWidget(self.Username)

        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.verticalLayout_3.addWidget(self.label_23)

        self.Password = QLineEdit(self.frame_2)
        self.Password.setObjectName(u"Password")

        self.verticalLayout_3.addWidget(self.Password)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

#if QT_CONFIG(shortcut)
        self.label_25.setBuddy(self.Full_name)
        self.label_19.setBuddy(self.Mobile_phone)
        self.label_21.setBuddy(self.Birthday)
        self.label_20.setBuddy(self.Position)
        self.label_26.setBuddy(self.Organization)
        self.label_2.setBuddy(self.Cabinet)
        self.label_27.setBuddy(self.Password)
        self.label_24.setBuddy(self.Username)
        self.label_22.setBuddy(self.Work_phone)
        self.label_23.setBuddy(self.Mail)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog_add)

        QMetaObject.connectSlotsByName(Dialog_add)
    # setupUi

    def retranslateUi(self, Dialog_add):
        Dialog_add.setWindowTitle(QCoreApplication.translate("Dialog_add", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog_add", u"Просмотр информации", None))
        self.label_25.setText(QCoreApplication.translate("Dialog_add", u"\u0424.\u0418.\u041e \u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430", None))
        self.label_19.setText(QCoreApplication.translate("Dialog_add", u"\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_21.setText(QCoreApplication.translate("Dialog_add", u"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u0435", None))
        self.label_20.setText(QCoreApplication.translate("Dialog_add", u"\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u043d\u043e\u0435 \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435 ", None))
        self.label_26.setText(QCoreApplication.translate("Dialog_add", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_add", u"\u041a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.label_27.setText(QCoreApplication.translate("Dialog_add", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_24.setText(QCoreApplication.translate("Dialog_add", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430 ", None))
        self.label_22.setText(QCoreApplication.translate("Dialog_add", u"Username", None))
        self.label_23.setText(QCoreApplication.translate("Dialog_add", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_add", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

