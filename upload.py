from azureml.core import Workspace, Datastore, Dataset

#Acess workspace, Datastore and Datasets

ws = Workspace.from_config('./config')
az_store = Datastore.get(ws, 'azureml_ds_practice_01')
az_dataset = Dataset.get_by_name(ws, 'Loan Applications USing SDK')
az_default_store = ws.get_default_datastore()

#Upload local files to storage account using datastore
files_list = ['../All+Data+Files/Employee Dataset - AC1.csv', '../All+Data+Files/Employee Dataset - AC2.csv','../All+Data+Files/defaults.csv']
az_store.upload_files(files=files_list,
                      target_path='Loan Data/',
                      relative_root='../All+Data+Files/',
                      overwrite=True)

az_store.upload(src_dir='../All+Data+Files',
                target_path='Loan Data/data',
                overwrite=True)

