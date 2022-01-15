import os
import sys
from PyQt5 import QtCore, QtWidgets

sys.path.append(os.path.abspath('../UI/ui_rough_draft'))
from ui_rough_draft.converted_ui import ui_add_task_superbasictask,ui_add_task_trackedtask, ui_add_task_prioritizedtask, ui_add_task_timedtask


TaskTypeKVP = {"SuperBasicTask": ui_add_task_superbasictask.Ui_add_task_superbasictask(), "TrackedTask": ui_add_task_trackedtask.Ui_add_task_trackedtask(), "PrioritizedTask": ui_add_task_prioritizedtask.Ui_add_task_prioritizedtask(), "TimedTask": ui_add_task_timedtask.Ui_add_task_timedtask()}
