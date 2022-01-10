import os
import sys
from PySide2 import QtCore, QtWidgets, QtGui


sys.path.append(os.path.abspath('../UI/ui_rough_draft'))
from ui_rough_draft.ui import ui_test2
from ui_rough_draft.converted_ui import ui_add_task_type_pick
from ui_rough_draft.converted_ui import ui_add_task_superbasictask
import UIUtilities

sys.path.append(os.path.abspath('../basicCode'))
import TrackedTask


class MainWindow(QtWidgets.QMainWindow, ui_test2.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #self.assign_widgets()
        #self.retranslateUi(self)
        #self.show()
        self.window_functions()

    def window_functions(self):
        self.action_Add_Tasks.triggered.connect(self.open_add_tasks)

    def open_add_tasks(self):
        add_tasks = ui_add_task_type_pick.Ui_add_task_type_pick()
        self.window = QtWidgets.QDialog()
        add_tasks.setupUi(self.window)
        print(add_tasks.pushButton.isChecked())
        taskType = add_tasks.comboBox.currentText()
        if add_tasks.comboBox.currentIndexChanged:
            print("Hello")
        add_tasks.comboBox.currentIndexChanged.connect(lambda taskType: self.on_combobox_changed(add_tasks.comboBox))
        #taskType = self.on_combobox_changed(add_tasks.comboBox)
        print(taskType)
        add_tasks.pushButton.clicked.connect(lambda: self.open_add_task_type(taskType))

        #add_tasks.pushButton = QtWidgets.QPushButton(self.open_add_task_type(taskType))

        self.window.setModal(True)
        self.window.show()

    def on_combobox_changed(self, combo):
        print(combo.currentText())
        return combo.currentText()

    def open_add_task_type(self, taskType):
        print(taskType)
        new_task = UIUtilities.TaskTypeKVP[taskType]
        print(new_task)
        self.window = QtWidgets.QDialog()
        new_task.setupUi(self.window)
        self.window.setModal(True)
        self.window.show()



    def assign_widgets(self):
        my_list = self.annoying()
        self.calendarWidget.clicked['QDate'].connect(lambda: self.write_task(my_list))

    def write_task(self, a_list):
        for task in a_list:
            self.today_list.addItem(task.get_task_name())

    def annoying(self):
        sample_list = []
        basic_task = TrackedTask.TrackedTask()
        basic_task.set_task_name("sleep")
        basic_task.set_frequency("daily")
        basic_task.set_max_completions(1)
        basic_task.complete_task()
        sample_list.append(basic_task)
        print(basic_task.get_frequency())
        another_task = TrackedTask.TrackedTask()
        another_task.set_task_name("more sleep")
        another_task.set_status("completed")
        print(another_task.get_status())
        print(another_task.get_frequency())
        print(basic_task.get_number_of_completions())
        sample_list.append(another_task)
        return sample_list


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()
