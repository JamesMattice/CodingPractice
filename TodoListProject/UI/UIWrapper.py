import os
import sys
from PySide2 import QtCore, QtWidgets, QtGui
import datetime


sys.path.append(os.path.abspath('../UI/ui_rough_draft'))
from ui_rough_draft.ui import ui_test2
from ui_rough_draft.converted_ui import ui_add_task_type_pick
from ui_rough_draft.converted_ui import ui_add_task_superbasictask
from ui_rough_draft.converted_ui import ui_new_tasklist
import UIUtilities

sys.path.append(os.path.abspath('../basicCode'))
import TrackedTask
import SuperBasicTask
import TimedTask
import PrioritizedTask
import ToDoListFileIO



class MainWindow(QtWidgets.QMainWindow, ui_test2.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # self.assign_widgets()
        # self.retranslateUi(self)
        # self.show()
        self.window_functions()


    def window_functions(self):
        self.action_Add_Tasks.triggered.connect(self.open_add_tasks_dialog)
        self.actionNew.triggered.connect(self.open_new_tasklist_dialog)

    def open_new_tasklist_dialog(self):
        input_window = ui_new_tasklist.Ui_new_tasklist()
        self.window = QtWidgets.QDialog()
        input_window.setupUi(self.window)
        input_window.pushButton_2.clicked.connect(lambda: ToDoListFileIO.TodoListFileIO().create_new_todo_list(input_window.lineEdit.text()))
        # change slot to a function, and add a close.window at the end of the function
        self.window.setModal(True)
        self.window.show()

    def open_add_tasks_dialog(self):
        add_tasks = ui_add_task_type_pick.Ui_add_task_type_pick()
        self.window = QtWidgets.QDialog()
        add_tasks.setupUi(self.window)
        add_tasks.pushButton.clicked.connect(lambda: self.open_add_task_type_dialog(add_tasks.comboBox.currentText()))

        self.window.setModal(True)
        self.window.show()

    def open_add_task_type_dialog(self, task_type):
        print(task_type)
        new_task = UIUtilities.TaskTypeKVP[task_type]
        print(new_task)
        self.window = QtWidgets.QDialog()
        new_task.setupUi(self.window)
        self.window.setModal(True)
        self.window.show()
        if task_type == "SuperBasicTask":
            new_task.pushButton_2.clicked.connect(lambda: self.add_super_basic_task(new_task))
        if task_type == "TrackedTask":
            new_task.pushButton_2.clicked.connect(lambda: self.add_tracked_task(new_task))
        # if task_type == "PrioritizedTask":
        #     new_task.pushButton_2.clicked.connect(lambda: self.add_prioritized_task(new_task))
        if task_type == "TimedTask":
            new_task.pushButton_2.clicked.connect(lambda: self.add_timed_task(new_task))

    def add_super_basic_task(self, task):
        test = SuperBasicTask.SuperBasicTask()
        test.set_task_name(task.lineEdit.text())
        print(test.get_task_name)
        test.set_date_of_next(task.dateTimeEdit.dateTime().toPython())
        test.set_frequency(task.comboBox_2.currentText().lower())
        print(test.get_frequency)
        # Work on this next time.

    def add_tracked_task(self, task):
        test = TrackedTask.TrackedTask()
        test.set_task_name(task.lineEdit.text())
        print(test.get_task_name)
        test.set_date_of_next(task.dateTimeEdit.dateTime().toPython())
        test.set_frequency(task.comboBox_2.currentText().lower())
        test.set_max_completions(task.spinBox.value())
        print(test)

    # def add_prioritized_task(self, task):
    #     test = PrioritizedTask.PrioritizedTasks()
    #     test.set_task_name(task.lineEdit.text())
    #     print(test.get_task_name)
    #     test.set_date_of_next(task.dateTimeEdit.dateTime().toPython())
    #     test.set_frequency(task.comboBox_2.currentText().lower())
    #     test.set_max_completions(task.spinBox.value())
    #
    #     print(test)

    def add_timed_task(self, task):
        test = TimedTask.TimedTask()
        test.set_task_name(task.lineEdit.text())
        print(test.get_task_name)
        test.set_date_of_next(task.dateTimeEdit.dateTime().toPython())
        test.set_frequency(task.comboBox_2.currentText().lower())
        test.set_max_completions(task.spinBox.value())
        print(test)

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
