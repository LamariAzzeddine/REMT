# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\data_viewer\Data_Viewer_ver2\Main_data_viewer_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 897)
        self.MainCard = CardWidget(Form)
        self.MainCard.setGeometry(QtCore.QRect(10, 10, 1061, 351))
        self.MainCard.setObjectName("MainCard")
        self.SubtitleLabel = SubtitleLabel(self.MainCard)
        self.SubtitleLabel.setGeometry(QtCore.QRect(10, 0, 161, 28))
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.MainCard)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 1041, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ElevatedCardWidget_7 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_7.setObjectName("ElevatedCardWidget_7")
        self.MachineName = BodyLabel(self.ElevatedCardWidget_7)
        self.MachineName.setGeometry(QtCore.QRect(10, 10, 151, 20))
        self.MachineName.setObjectName("MachineName")
        self.verticalLayout_2.addWidget(self.ElevatedCardWidget_7)
        self.ElevatedCardWidget_6 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_6.setObjectName("ElevatedCardWidget_6")
        self.MachineIP = BodyLabel(self.ElevatedCardWidget_6)
        self.MachineIP.setGeometry(QtCore.QRect(10, 10, 151, 19))
        self.MachineIP.setObjectName("MachineIP")
        self.verticalLayout_2.addWidget(self.ElevatedCardWidget_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.ElevatedCardWidget_5 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_5.setObjectName("ElevatedCardWidget_5")
        self.BodyLabel_3 = BodyLabel(self.ElevatedCardWidget_5)
        self.BodyLabel_3.setGeometry(QtCore.QRect(10, 10, 63, 19))
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.ElevatedCardWidget_5)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 161, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Uptime = SubtitleLabel(self.verticalLayoutWidget)
        self.Uptime.setObjectName("Uptime")
        self.verticalLayout.addWidget(self.Uptime, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.ElevatedCardWidget_5)
        self.ElevatedCardWidget_11 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_11.setObjectName("ElevatedCardWidget_11")
        self.BodyLabel_7 = BodyLabel(self.ElevatedCardWidget_11)
        self.BodyLabel_7.setGeometry(QtCore.QRect(10, 10, 101, 19))
        self.BodyLabel_7.setObjectName("BodyLabel_7")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.ElevatedCardWidget_11)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(0, 20, 161, 51))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.TotalDisk = SubtitleLabel(self.verticalLayoutWidget_7)
        self.TotalDisk.setObjectName("TotalDisk")
        self.verticalLayout_9.addWidget(self.TotalDisk, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.ElevatedCardWidget_11)
        self.ElevatedCardWidget_10 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_10.setObjectName("ElevatedCardWidget_10")
        self.BodyLabel_6 = BodyLabel(self.ElevatedCardWidget_10)
        self.BodyLabel_6.setGeometry(QtCore.QRect(10, 10, 91, 19))
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.ElevatedCardWidget_10)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 20, 161, 51))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.CpuCores = SubtitleLabel(self.verticalLayoutWidget_6)
        self.CpuCores.setObjectName("CpuCores")
        self.verticalLayout_8.addWidget(self.CpuCores, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.ElevatedCardWidget_10)
        self.ElevatedCardWidget_9 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_9.setObjectName("ElevatedCardWidget_9")
        self.BodyLabel_5 = BodyLabel(self.ElevatedCardWidget_9)
        self.BodyLabel_5.setGeometry(QtCore.QRect(10, 10, 91, 19))
        self.BodyLabel_5.setObjectName("BodyLabel_5")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.ElevatedCardWidget_9)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 20, 161, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.TotalRam = SubtitleLabel(self.verticalLayoutWidget_5)
        self.TotalRam.setObjectName("TotalRam")
        self.verticalLayout_7.addWidget(self.TotalRam, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.ElevatedCardWidget_9)
        self.ElevatedCardWidget_8 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_8.setObjectName("ElevatedCardWidget_8")
        self.BodyLabel_4 = BodyLabel(self.ElevatedCardWidget_8)
        self.BodyLabel_4.setGeometry(QtCore.QRect(10, 10, 101, 19))
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.ElevatedCardWidget_8)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 20, 161, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Nics = SubtitleLabel(self.verticalLayoutWidget_4)
        self.Nics.setObjectName("Nics")
        self.verticalLayout_6.addWidget(self.Nics, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.ElevatedCardWidget_8)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.MainCard)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 1041, 201))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ElevatedCardWidget = ElevatedCardWidget(self.horizontalLayoutWidget_2)
        self.ElevatedCardWidget.setObjectName("ElevatedCardWidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.ElevatedCardWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, -5, 341, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CPUusagering = ProgressRing(self.gridLayoutWidget_2)
        self.CPUusagering.setTextVisible(True)
        self.CPUusagering.setObjectName("CPUusagering")
        self.gridLayout_2.addWidget(self.CPUusagering, 1, 0, 1, 1)
        self.Diskusagering = ProgressRing(self.gridLayoutWidget_2)
        self.Diskusagering.setTextVisible(True)
        self.Diskusagering.setObjectName("Diskusagering")
        self.gridLayout_2.addWidget(self.Diskusagering, 1, 2, 1, 1)
        self.RAMusagering = ProgressRing(self.gridLayoutWidget_2)
        self.RAMusagering.setTextVisible(True)
        self.RAMusagering.setObjectName("RAMusagering")
        self.gridLayout_2.addWidget(self.RAMusagering, 1, 1, 1, 1)
        self.StrongBodyLabel = StrongBodyLabel(self.gridLayoutWidget_2)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.gridLayout_2.addWidget(self.StrongBodyLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.StrongBodyLabel_2 = StrongBodyLabel(self.gridLayoutWidget_2)
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")
        self.gridLayout_2.addWidget(self.StrongBodyLabel_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.StrongBodyLabel_3 = StrongBodyLabel(self.gridLayoutWidget_2)
        self.StrongBodyLabel_3.setObjectName("StrongBodyLabel_3")
        self.gridLayout_2.addWidget(self.StrongBodyLabel_3, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.ElevatedCardWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ElevatedCardWidget_13 = ElevatedCardWidget(self.horizontalLayoutWidget_2)
        self.ElevatedCardWidget_13.setObjectName("ElevatedCardWidget_13")
        self.gridLayoutWidget = QtWidgets.QWidget(self.ElevatedCardWidget_13)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 341, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.min1LoadRing = ProgressRing(self.gridLayoutWidget)
        self.min1LoadRing.setTextVisible(True)
        self.min1LoadRing.setObjectName("min1LoadRing")
        self.gridLayout.addWidget(self.min1LoadRing, 1, 0, 1, 1)
        self.StrongBodyLabel_4 = StrongBodyLabel(self.gridLayoutWidget)
        self.StrongBodyLabel_4.setObjectName("StrongBodyLabel_4")
        self.gridLayout.addWidget(self.StrongBodyLabel_4, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.min15LoadRing = ProgressRing(self.gridLayoutWidget)
        self.min15LoadRing.setTextVisible(True)
        self.min15LoadRing.setObjectName("min15LoadRing")
        self.gridLayout.addWidget(self.min15LoadRing, 1, 2, 1, 1)
        self.StrongBodyLabel_6 = StrongBodyLabel(self.gridLayoutWidget)
        self.StrongBodyLabel_6.setObjectName("StrongBodyLabel_6")
        self.gridLayout.addWidget(self.StrongBodyLabel_6, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.min5LoadRing = ProgressRing(self.gridLayoutWidget)
        self.min5LoadRing.setTextVisible(True)
        self.min5LoadRing.setObjectName("min5LoadRing")
        self.gridLayout.addWidget(self.min5LoadRing, 1, 1, 1, 1)
        self.StrongBodyLabel_5 = StrongBodyLabel(self.gridLayoutWidget)
        self.StrongBodyLabel_5.setObjectName("StrongBodyLabel_5")
        self.gridLayout.addWidget(self.StrongBodyLabel_5, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.ElevatedCardWidget_13)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.ElevatedCardWidget_2 = ElevatedCardWidget(self.horizontalLayoutWidget_2)
        self.ElevatedCardWidget_2.setObjectName("ElevatedCardWidget_2")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.ElevatedCardWidget_2)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(10, 10, 321, 31))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.TotalCachedMemory = BodyLabel(self.gridLayoutWidget_7)
        self.TotalCachedMemory.setObjectName("TotalCachedMemory")
        self.gridLayout_7.addWidget(self.TotalCachedMemory, 0, 1, 1, 1)
        self.StrongBodyLabel_11 = StrongBodyLabel(self.gridLayoutWidget_7)
        self.StrongBodyLabel_11.setObjectName("StrongBodyLabel_11")
        self.gridLayout_7.addWidget(self.StrongBodyLabel_11, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.ElevatedCardWidget_2)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 40, 321, 31))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.StrongBodyLabel_9 = StrongBodyLabel(self.gridLayoutWidget_5)
        self.StrongBodyLabel_9.setObjectName("StrongBodyLabel_9")
        self.gridLayout_5.addWidget(self.StrongBodyLabel_9, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.TotalSwap = BodyLabel(self.gridLayoutWidget_5)
        self.TotalSwap.setObjectName("TotalSwap")
        self.gridLayout_5.addWidget(self.TotalSwap, 0, 1, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.ElevatedCardWidget_2)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 70, 321, 31))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.AvailableSwap = BodyLabel(self.gridLayoutWidget_6)
        self.AvailableSwap.setObjectName("AvailableSwap")
        self.gridLayout_6.addWidget(self.AvailableSwap, 0, 1, 1, 1)
        self.StrongBodyLabel_10 = StrongBodyLabel(self.gridLayoutWidget_6)
        self.StrongBodyLabel_10.setObjectName("StrongBodyLabel_10")
        self.gridLayout_6.addWidget(self.StrongBodyLabel_10, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.HorizontalSeparator = HorizontalSeparator(self.ElevatedCardWidget_2)
        self.HorizontalSeparator.setGeometry(QtCore.QRect(10, 110, 321, 3))
        self.HorizontalSeparator.setObjectName("HorizontalSeparator")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.ElevatedCardWidget_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 120, 321, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.StrongBodyLabel_7 = StrongBodyLabel(self.gridLayoutWidget_3)
        self.StrongBodyLabel_7.setObjectName("StrongBodyLabel_7")
        self.gridLayout_3.addWidget(self.StrongBodyLabel_7, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.NetworkOut = BodyLabel(self.gridLayoutWidget_3)
        self.NetworkOut.setObjectName("NetworkOut")
        self.gridLayout_3.addWidget(self.NetworkOut, 0, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.ElevatedCardWidget_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 150, 321, 31))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.NetworkIn = BodyLabel(self.gridLayoutWidget_4)
        self.NetworkIn.setObjectName("NetworkIn")
        self.gridLayout_4.addWidget(self.NetworkIn, 0, 1, 1, 1)
        self.StrongBodyLabel_8 = StrongBodyLabel(self.gridLayoutWidget_4)
        self.StrongBodyLabel_8.setObjectName("StrongBodyLabel_8")
        self.gridLayout_4.addWidget(self.StrongBodyLabel_8, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.ElevatedCardWidget_2)
        self.TimestampLabel = CaptionLabel(self.MainCard)
        self.TimestampLabel.setGeometry(QtCore.QRect(160, 10, 70, 15))
        self.TimestampLabel.setObjectName("TimestampLabel")
        self.CardWidget = CardWidget(Form)
        self.CardWidget.setGeometry(QtCore.QRect(10, 370, 1061, 521))
        self.CardWidget.setObjectName("CardWidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.CardWidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.CardWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.LastHourTab = QtWidgets.QWidget()
        self.LastHourTab.setObjectName("LastHourTab")
        self.tabWidget.addTab(self.LastHourTab, "")
        self.Last24HoursTab = QtWidgets.QWidget()
        self.Last24HoursTab.setObjectName("Last24HoursTab")
        self.tabWidget.addTab(self.Last24HoursTab, "")
        self.CustomTab = QtWidgets.QWidget()
        self.CustomTab.setObjectName("CustomTab")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.CustomTab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 1041, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 0, 1, 1)
        self.TimePicker_4 = TimePicker(self.horizontalLayoutWidget_3)
        self.TimePicker_4.setObjectName("TimePicker_4")
        self.gridLayout_9.addWidget(self.TimePicker_4, 0, 2, 1, 1)
        self.CalendarPicker_3 = CalendarPicker(self.horizontalLayoutWidget_3)
        self.CalendarPicker_3.setObjectName("CalendarPicker_3")
        self.gridLayout_9.addWidget(self.CalendarPicker_3, 1, 1, 1, 1)
        self.CalendarPicker_4 = CalendarPicker(self.horizontalLayoutWidget_3)
        self.CalendarPicker_4.setObjectName("CalendarPicker_4")
        self.gridLayout_9.addWidget(self.CalendarPicker_4, 0, 1, 1, 1)
        self.TimePicker_3 = TimePicker(self.horizontalLayoutWidget_3)
        self.TimePicker_3.setObjectName("TimePicker_3")
        self.gridLayout_9.addWidget(self.TimePicker_3, 1, 2, 1, 1)
        self.PrimaryPushButton_2 = PrimaryPushButton(self.horizontalLayoutWidget_3)
        self.PrimaryPushButton_2.setObjectName("PrimaryPushButton_2")
        self.gridLayout_9.addWidget(self.PrimaryPushButton_2, 1, 3, 1, 1)
        self.LineEdit_6 = LineEdit(self.horizontalLayoutWidget_3)
        self.LineEdit_6.setObjectName("LineEdit_6")
        self.gridLayout_9.addWidget(self.LineEdit_6, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem1, 0, 4, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_9)
        self.tabWidget.addTab(self.CustomTab, "")
        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SubtitleLabel.setText(_translate("Form", "Machine details: "))
        self.MachineName.setText(_translate("Form", "Name"))
        self.MachineIP.setText(_translate("Form", "IP"))
        self.BodyLabel_3.setText(_translate("Form", "Uptime:"))
        self.Uptime.setText(_translate("Form", "None"))
        self.BodyLabel_7.setText(_translate("Form", "Total Disk:"))
        self.TotalDisk.setText(_translate("Form", "None"))
        self.BodyLabel_6.setText(_translate("Form", "Cpu cores:"))
        self.CpuCores.setText(_translate("Form", "None"))
        self.BodyLabel_5.setText(_translate("Form", "Total Ram:"))
        self.TotalRam.setText(_translate("Form", "None"))
        self.BodyLabel_4.setText(_translate("Form", "NICs:"))
        self.Nics.setText(_translate("Form", "None"))
        self.StrongBodyLabel.setText(_translate("Form", "CPU"))
        self.StrongBodyLabel_2.setText(_translate("Form", "RAM"))
        self.StrongBodyLabel_3.setText(_translate("Form", "Disk"))
        self.StrongBodyLabel_4.setText(_translate("Form", "1 Min load"))
        self.StrongBodyLabel_6.setText(_translate("Form", "15 Min load"))
        self.StrongBodyLabel_5.setText(_translate("Form", "5 Min load"))
        self.TotalCachedMemory.setText(_translate("Form", "Null"))
        self.StrongBodyLabel_11.setText(_translate("Form", "Total cached Memory:"))
        self.StrongBodyLabel_9.setText(_translate("Form", "Total swap:"))
        self.TotalSwap.setText(_translate("Form", "Null"))
        self.AvailableSwap.setText(_translate("Form", "Null"))
        self.StrongBodyLabel_10.setText(_translate("Form", "Available swap:"))
        self.StrongBodyLabel_7.setText(_translate("Form", "Network Out:"))
        self.NetworkOut.setText(_translate("Form", "Null"))
        self.NetworkIn.setText(_translate("Form", "Null"))
        self.StrongBodyLabel_8.setText(_translate("Form", "Network In:"))
        self.TimestampLabel.setText(_translate("Form", "   As of Null"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LastHourTab), _translate("Form", "Last Hour"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Last24HoursTab), _translate("Form", "Last 24 Hours"))
        self.CalendarPicker_3.setText(_translate("Form", "End Date"))
        self.CalendarPicker_4.setText(_translate("Form", "Start Date"))
        self.PrimaryPushButton_2.setText(_translate("Form", "Plot"))
        self.LineEdit_6.setPlaceholderText(_translate("Form", "Ticks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CustomTab), _translate("Form", "Custom"))
from qfluentwidgets import BodyLabel, CalendarPicker, CaptionLabel, CardWidget, ElevatedCardWidget, HorizontalSeparator, LineEdit, PrimaryPushButton, ProgressRing, StrongBodyLabel, SubtitleLabel, TimePicker
