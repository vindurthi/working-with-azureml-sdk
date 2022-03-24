from azureml.core import Workspace, Datastore, Dataset, Experiment
from azureml.core import Run

#Acess workspace, Datastore and Datasets

ws = Workspace.from_config('./config')
az_store = Datastore.get(ws, 'azureml_ds_practice_01')
az_dataset = Dataset.get_by_name(ws, 'Loan Applications USing SDK')
az_default_store = ws.get_default_datastore()


#Get the context of the experiment run
new_run = Run.get_context()

#Do your stuff here
df = az_dataset.to_pandas_dataframe()

#count the observations
total_observations = len(df)

#Get the null/missing values
nulldf = df.isnull().sum()

#Create a new df and write to outputs
new_df = df[['Gender', 'Married', 'Education', 'Loan_Status']]
new_df.to_csv('./outputs/loan_trunc.csv', index=False)

#Log metrics and Complete an experiment run

#Log metrics
new_run.log('Total Observations', total_observations)

#Log the missing data values
for col in df.columns:
    new_run.log(col, nulldf[col])

new_run.complete()
