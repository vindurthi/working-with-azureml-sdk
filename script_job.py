from azureml.core import Workspace, Experiment, ScriptRunConfig

#Access the workspace using config.json
ws = Workspace.from_config('./config')

new_experiment = Experiment(ws, name='Loan_script')

script_config = ScriptRunConfig(source_directory='.',
                                script='script_to_run.py')

new_run = new_experiment.submit(config=script_config)

new_run.wait_for_completion()