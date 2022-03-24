from azureml.core import Workspace, Datastore

ws = Workspace.from_config(path='./config/')

az_store = Datastore.register_azure_blob_container(workspace=ws,
                                                   datastore_name='azureml_ds_practice_01',
                                                   account_name='amlpractice',
                                                   container_name='azuremlpracticeblob',
                                                   account_key='V/PzE2cmZvchmNp887w6R7LaQm1GVdh0ZtvXxVwgnyLFdjWorVeA9e3FDdQKi1wYEWMqJjMT0p/PERd8QWGl4g=='
                                                   )