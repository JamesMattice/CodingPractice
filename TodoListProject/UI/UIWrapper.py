import os
import sys
from PySide2 import QtCore, QtWidgets

sys.path.append(os.path.abspath('../UI/ui_rough_draft'))
from ui_rough_draft.ui import ui_test2
# from ui_rough_draft.converted_ui import ui_add_task_type_pick

sys.path.append(os.path.abspath('../basicCode'))
import TrackedTask


class MainWindow(QtWidgets.QMainWindow, ui_test2.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #self.assign_widgets()
        #self.retranslateUi(self)
        #self.show()
        # self.windowFunctions()
        # dialog = ui_add_task_type_pick.Ui_add_task_type_pick()

    # def windowFunctions(self):
    #     self.action_Add_Tasks.triggered.connect(ui_add_task_type_pick.Ui_add_task_type_pick().setupUi(add_task_type_pick))

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
