from azureml.core import Workspace, Datastore, Dataset

#Acess workspace, Datastore and Datasets

ws = Workspace.from_config('./config')
az_store = Datastore.get(ws, 'azureml_ds_practice_01')
az_dataset = Dataset.get_by_name(ws, 'Loan Applications USing SDK')
az_default_store = ws.get_default_datastore()

#Load the Azureml dataset into the pandas dataframe
df = az_dataset.to_pandas_dataframe()
print(df.head())

df_sub = df[['Married','Gender','Loan_Status']]

az_ds_from_df = Dataset.Tabular.register_pandas_dataframe(dataframe=df_sub,
                                                          target = az_store,
                                                          name = 'Loan dataset from dataframe')
adult_income = Dataset.get_by_name(ws, 'AdultIncome')

adult_income_df = adult_income.to_pandas_dataframe()

adult_income_df = adult_income_df.rename(columns={'Column1':'age',
                  'Column2':'workclass',
                  'Column3':'fnlwgt',
                  'Column4':'education',
                  'Column5':'education_num',
                  'Column6':'marital_status',
                  'Column7':'occupation',
                  'Column8':'relationship',
                  'Column9':'race',
                  'Column10':'sex',
                  'Column11':'capital_gain',
                  'Column12':'capital_loss',
                  'Column13':'hours_per_week',
                  'Column14':'native_country',
                  'Column15':'label'})

az_ds_clean_adult_income_df = Dataset.Tabular.register_pandas_dataframe(dataframe=adult_income_df,
                                                          target = az_store,
                                                          name = 'Clean Adult Income')