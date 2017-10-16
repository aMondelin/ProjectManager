import sys
import projectmanager
from PySide.QtGui import *


PROJECT_NAME = 'ProjectManager-Template'


class MainUi(QWidget):
    def __init__(self):
        super(MainUi, self).__init__()

        self.init_ui()
        self.create_asset_widget = None

    def init_ui(self):
        self.resize(500, 700)
        center_window(self)
        self.setWindowTitle('Project-Manager')
        self.setWindowIcon(QIcon('D:/ProjectManager-Template/super_favicon.jpg'))

        # Main Layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Asset Types
        group_asset_types = QGroupBox('Select Asset')
        group_asset_types.setMaximumHeight(80)
        layout_asset_types = QGridLayout(group_asset_types)

        self.radio_characters = QRadioButton('characters')
        self.radio_characters.toggle()

        self.radio_props = QRadioButton('props')
        self.radio_shots = QRadioButton('shot')
        self.spacer_task = QSpacerItem(20, 40)
        self.label_task = QLabel('Task:')
        self.combo_tasks = QComboBox()

        layout_asset_types.addWidget(self.radio_characters, 0, 0, 1, 2)
        layout_asset_types.addWidget(self.radio_props, 0, 2, 1, 2)
        layout_asset_types.addWidget(self.radio_shots, 0, 4, 1, 2)
        layout_asset_types.addItem(self.spacer_task, 1, 0)
        layout_asset_types.addWidget(self.label_task, 1, 3)
        layout_asset_types.addWidget(self.combo_tasks, 1, 4, 1, 2)

        # Asset Description
        group_asset_description = QWidget()
        layout_asset_description = QGridLayout(group_asset_description)

        self.label_asset_thumbnail = QLabel('VIGNETTE')
        self.label_asset_thumbnail.setMinimumWidth(130)
        self.label_asset_thumbnail.setMinimumHeight(80)
        self.label_asset_thumbnail.setMaximumWidth(130)
        self.label_asset_thumbnail.setMaximumHeight(80)
        self.thumbnail_asset = QPixmap('D:/ProjectManager-Template/assets/characters/jean/vignette.jpg')
        self.label_asset_thumbnail.setPixmap(self.thumbnail_asset)

        self.label_asset_description = QLabel('dzeyg ygfyzgfze zugfizuf fyzuh zodhvbezd fzeg zy  uezgduyedf z fhzebfiezf zefzbefiuzebf zeiugze zeuriuzbe bze iuu z ziuhuzhcu nz z hchoz ofzdfzp dzfoijfoierg ijhozuhfoizeiopfzefefe')
        self.label_asset_description.setWordWrap(1)
        self.label_asset_description.setContentsMargins(15, 0, 0, 0)

        layout_asset_description.addWidget(self.label_asset_thumbnail, 0, 0)
        layout_asset_description.addWidget(self.label_asset_description, 0, 1, 1, 2)

        # Asset Picker
        group_asset_picker = QGroupBox('Assets')
        layout_asset_picker = QVBoxLayout(group_asset_picker)

        self.list_view_assets = QListView()

        layout_asset_picker.addWidget(self.list_view_assets)

        # Asset Version
        group_asset_version = QGroupBox('Versions')
        layout_asset_version = QVBoxLayout(group_asset_version)

        self.list_view_versions = QListView()

        layout_asset_version.addWidget(self.list_view_versions)

        # Asset Tools
        group_asset_tools = QWidget()
        layout_asset_tools = QHBoxLayout(group_asset_tools)

        self.button_save = QPushButton('SAVE')
        self.button_save.setMinimumHeight(35)

        self.button_share = QPushButton('SHARE')
        self.button_share.setMinimumHeight(30)

        self.spacer_import = QSpacerItem(80, 20)

        self.button_import = QPushButton('Import')
        self.button_import.setMinimumHeight(20)

        self.spin_box_import = QSpinBox()
        self.spin_box_import.setMinimum(1)
        self.spin_box_import.setMaximum(20)
        self.spin_box_import.setMinimumHeight(20)
        self.spin_box_import.setValue(1)

        self.button_create_asset = QPushButton('Create Asset')
        self.button_create_asset.setMinimumHeight(20)

        self.button_create_task = QPushButton('v')
        self.button_create_task.setMaximumWidth(15)
        self.button_create_task.setMinimumHeight(20)

        layout_asset_tools.addWidget(self.button_save)
        layout_asset_tools.addWidget(self.button_share)
        layout_asset_tools.addItem(self.spacer_import)
        layout_asset_tools.addWidget(self.button_import)
        layout_asset_tools.addWidget(self.spin_box_import)
        layout_asset_tools.addWidget(self.button_create_asset)
        layout_asset_tools.addWidget(self.button_create_task)

        # Action - Create Task
        self.create_task = QAction(self)
        self.create_task.setText('Create Task')
        self.create_task.triggered.connect(self.create_task_window)

        # Menu - Roots
        self.menu_roots = QMenu(self)
        self.menu_roots.addAction(self.create_task)

        main_layout.addWidget(group_asset_types)
        main_layout.addWidget(group_asset_description)
        main_layout.addWidget(group_asset_picker)
        main_layout.addWidget(group_asset_version)
        main_layout.addWidget(group_asset_tools)

        # Events
        self.button_create_asset.clicked.connect(self.create_asset_window)
        self.button_create_task.clicked.connect(self.create_menu_window)

        self.radio_characters.clicked.connect(self.refresh_combo_box)
        self.radio_props.clicked.connect(self.refresh_combo_box)
        self.radio_shots.clicked.connect(self.refresh_combo_box)

        refresh_combo_box(self)

        self.show()

    def refresh_combo_box(self):
        refresh_combo_box(self)

    def create_menu_window(self):
        self.menu_roots.move(QCursor.pos())
        self.menu_roots.exec_()

    def create_asset_window(self):
        self.create_asset_widget = create_asset_ui()

    def create_task_window(self):
        self.create_task_widget = create_task_ui()


class CreateAssetUi(QWidget):
    def __init__(self):
        super(CreateAssetUi, self).__init__()

        self.init_ui()
        # self.new_asset_type = ""

    def init_ui(self):
        self.resize(275, 150)
        center_window(self)
        self.setWindowTitle('Create New Asset')

        self.radio_character = QRadioButton('CHARACTERS', self)
        self.radio_character.move(44, 15)
        self.radio_character.toggle()

        self.radio_props = QRadioButton('PROPS', self)
        self.radio_props.move(154, 15)

        self.label_asset_name = QLabel('ASSET NAME:', self)
        self.label_asset_name.move(21, 49)

        self.line_edit_asset_name = QLineEdit(self)
        self.line_edit_asset_name.move(94, 46)
        self.line_edit_asset_name.resize(150, 20)

        self.button_create_asset = QPushButton('GO', self)
        self.button_create_asset.resize(115, 50)
        self.button_create_asset.move(80, 85)

        self.button_create_asset.clicked.connect(self.create_asset_triggered)

        self.show()

    def create_asset_triggered(self):
        asset_types = [self.radio_character, self.radio_props]
        asset_type = ''

        for type in asset_types:
            if type.isChecked():
                asset_type = type.text()

        asset_name = self.line_edit_asset_name.text()

        if asset_name != '':
            projectmanager.create_asset(project_name = PROJECT_NAME,
                                        asset_type = asset_type,
                                        asset_name = asset_name)
        else:
            print 'Please write asset\'s name'


class CreateTaskUi(QWidget):
    def __init__(self):
        super(CreateTaskUi, self).__init__()

        self.init_ui()
        # self.new_asset_type = ""

    def init_ui(self):
        self.resize(275, 175)
        center_window(self)
        self.setWindowTitle('Create New Task')

        # Global Layout
        layout_global = QVBoxLayout()
        self.setLayout(layout_global)

        # Select Asset
        group_asset = QGroupBox('Select Asset')
        layout_group_asset = QVBoxLayout()
        group_asset.setLayout(layout_group_asset)

        group_radios_asset = QWidget()
        layout_radios_asset = QHBoxLayout()
        group_radios_asset.setLayout(layout_radios_asset)

        self.radio_character = QRadioButton('CHARACTERS', self)
        self.radio_character.toggle()

        self.radio_props = QRadioButton('PROPS', self)

        layout_radios_asset.addWidget(self.radio_character)
        layout_radios_asset.addWidget(self.radio_props)

        layout_group_asset.addWidget(group_radios_asset)

        group_combo_asset_names = QWidget()
        layout_combo_asset_names = QVBoxLayout()
        group_combo_asset_names.setLayout(layout_combo_asset_names)

        self.combo_asset_names = QComboBox()
        self.refresh_combo_asset()

        layout_combo_asset_names.addWidget(self.combo_asset_names)

        layout_group_asset.addWidget(group_combo_asset_names)

        layout_global.addWidget(group_asset)

        # Create New Task
        group_task_name = QWidget()
        layout_group_task = QHBoxLayout()
        group_task_name.setLayout(layout_group_task)

        label_task_name = QLabel('Task Name:')

        self.line_edit_task_name = QLineEdit(self)
        self.line_edit_task_name.resize(150, 18)

        layout_group_task.addWidget(label_task_name)
        layout_group_task.addWidget(self.line_edit_task_name)

        group_create_task = QWidget()
        layout_group_create_task = QVBoxLayout()
        group_create_task.setLayout(layout_group_create_task)

        self.button_create_task = QPushButton('CREATE TASK', self)

        layout_group_create_task.addWidget(self.button_create_task)

        layout_global.addWidget(group_task_name)
        layout_global.addWidget(group_create_task)

        # Events
        self.radio_character.toggled.connect(self.combo_state_changed)
        self.radio_props.toggled.connect(self.combo_state_changed)
        self.button_create_task.clicked.connect(self.create_task_triggered)

        self.show()

    def checked_asset_type(self):
        asset_types = [self.radio_character, self.radio_props]
        asset_type = ''

        for type in asset_types:
            if type.isChecked():
                asset_type = type.text()

        return asset_type

    def refresh_combo_asset(self):
        asset_type = self.checked_asset_type()

        asset_list = projectmanager.all_assets(project_name = PROJECT_NAME, asset_type = asset_type)

        self.combo_asset_names.clear()
        self.combo_asset_names.addItem('Select Asset')

        for asset in asset_list:
            self.combo_asset_names.addItem(asset)

    def combo_state_changed(self):
        self.refresh_combo_asset()

    def create_task_triggered(self):
        asset_type = self.checked_asset_type()
        asset_name = self.combo_asset_names.currentText()
        task_name = self.line_edit_task_name.text()

        if (asset_name != '') and (asset_name != 'Select Asset'):
            projectmanager.create_tasks(project_name = PROJECT_NAME,
                                        asset_type = asset_type,
                                        asset_name = asset_name,
                                        task_name = task_name)
        else:
            print 'Please write asset\'s name'


def checked_asset_type(self):
    asset_types = [self.radio_characters , self.radio_props, self.radio_shots]
    asset_type = ''

    for type in asset_types:
        if type.isChecked():
            asset_type = type.text()

    return asset_type


def refresh_combo_box(self):
    asset_type = checked_asset_type(self)

    asset_task_list = ['lighting', 'modeling', 'rig']
    shot_task_list = ['animation', 'fx', 'render']

    self.combo_tasks.clear()
    # self.combo_tasks.addItem('Select Asset')

    if asset_type == 'characters' or asset_type == 'props':
        for asset in asset_task_list:
            self.combo_tasks.addItem(asset)

    elif asset_type == 'shot':
        for asset in shot_task_list:
            self.combo_tasks.addItem(asset)

    else:
        pass


def center_window(self):
    size_window = self.frameGeometry()
    user_window_center = QDesktopWidget().availableGeometry().center()
    size_window.moveCenter(user_window_center)
    self.move(size_window.topLeft())


def generate_ui():
    app = QApplication(sys.argv)
    main_ui = MainUi()
    sys.exit(app.exec_())


def create_asset_ui():
    #app = QApplication(sys.argv)
    create_asset_ui = CreateAssetUi()
    return create_asset_ui


def create_task_ui():
    #app = QApplication(sys.argv)
    create_task_ui = CreateTaskUi()
    return create_task_ui


if __name__ == '__main__':
    generate_ui()
    #create_asset_ui()