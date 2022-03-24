from azureml.core import Workspace, Datastore, Dataset

#Access the workspace by name
ws = Workspace.from_config('./config')

#List all the workspaces within a subscription
ws_list = list(Workspace.list(subscription_id='4522505d-0690-4e44-84d2-d9b3a4b46f1a'))

for space in ws_list:
    print(space)

#Acess the default datastore
az_default_store = ws.get_default_datastore()

#list all the datastores
store_list = list(ws.datastores)

for store in store_list:
    print(store)

#Get the datasets from a workspace
az_dataset = Dataset.get_by_name(ws, 'Loan Applications Using SDK')

#list all datasets from a workspace
ds_list = list(ws.datasets.keys())

for items in ds_list:
    print(items)

