from azureml.core import Workspace, Model

ws = Workspace.from_config('./config')

new_run = ws.get_run('3538af0c-5902-45fe-8153-e672fe39cdc2')

new_run.register_model(model_path='outputs/models.pkl',
                       model_name='AdultIncome_models',
                       tags={'source':'SDK-Run', 'algorithm': 'RandomForest'},
                       properties={'Accuracy':new_run.get_metrics()['accuracy']},
                       description='Combined Models from the Run.')