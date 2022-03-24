from azureml.core import Workspace

ws = Workspace.create(name='aml_practice',
                      subscription_id='4522505d-0690-4e44-84d2-d9b3a4b46f1a',
                      resource_group='rg-dabods-sandbox-cus-ce27',
                      create_resource_group=False,
                      location='centralus')


ws.write_config(path='./config')

