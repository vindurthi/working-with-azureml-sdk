from azureml.core import Workspace, Datastore, Dataset

ws = Workspace.from_config(path='./config')

#Access the datastore
az_store = Datastore.get(ws, 'azureml_ds_practice_01')

#Create the path of the csv file
csv_path = [(az_store,'Loan Data/Loan Approval Prediction.csv')]

#Create the dataset
loan_dataset = Dataset.Tabular.from_delimited_files(path=csv_path)

#Register the dataset
loan_dataset = loan_dataset.register(workspace=ws,
                                    name='Loan Applications Using SDK',
                                    create_new_version=True)

csv_path = [(az_store,'Loan Data/data/defaults.csv')]
#Create the dataset
defaults_dataset = Dataset.Tabular.from_delimited_files(path=csv_path)

#Register the dataset
defaults_dataset = defaults_dataset.register(workspace=ws,
                                    name='Defaults',
                                    create_new_version=True)

