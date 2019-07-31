from os import path

import Final_Project_Squad1

base_path = path.dirname(path.dirname(Final_Project_Squad1.__file__))
workspace_path = path.join(base_path, 'workspace')
data_path = path.join(workspace_path, 'data')
models_path = path.join(workspace_path, 'models')
