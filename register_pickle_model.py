from azureml.core import Workspace, Model

ws = Workspace.from_config('./config')

Model.register(workspace=ws,
               model_path = './outputs/models.pkl',
               model_name='AdultIncome_models_local',
               tags={'source':'SDK-Run', 'algorithm': 'RandomForest'},
               properties={'Accuracy':0.855},
               description='Combined Models from the Run.')

