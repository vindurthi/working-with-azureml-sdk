from azureml.core import Workspace

subscription_id = '4522505d-0690-4e44-84d2-d9b3a4b46f1a'
resource_group  = 'rg-dabods-sandbox-cus-ce27'
workspace_name  = 'aml_practice'

try:
    ws = Workspace(subscription_id = subscription_id, resource_group = resource_group, workspace_name = workspace_name)
    ws.write_config('./config')
    print('Library configuration succeeded')
except:
    print('Workspace not found')