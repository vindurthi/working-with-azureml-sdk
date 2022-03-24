from azureml.core import Workspace, Datastore, Dataset, Experiment

#Acess workspace, Datastore and Datasets

ws = Workspace.from_config('./config')
az_store = Datastore.get(ws, 'azureml_ds_practice_01')
az_dataset = Dataset.get_by_name(ws, 'Loan Applications USing SDK')
az_default_store = ws.get_default_datastore()


#Create/Access an experiment object
experiment = Experiment(ws, name='Loan-sdk-exp01')

#Run an experiment 
new_run = experiment.start_logging()

#Do your stuff here
df = az_dataset.to_pandas_dataframe()

#count the observations
total_observations = len(df)

#Get the null/missing values
nulldf = df.isnull().sum()

#Log metrics and Complete an experiment run

#Log metrics
new_run.log('Total Observations', total_observations)

#Log the missing data values
for col in df.columns:
    new_run.log(col, nulldf[col])

new_run.complete()

for run in experiment.get_runs():
    print(run.id)
    if run.status=="Running":
        run.cancel()
for run in experiment.get_runs():
    print(run.id)
    print(run.status)