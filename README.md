# Azure ML SDK

This repo contains boiler plate code snippets to perform the following actions in Azure Machine Learning studio using  Azureml-SDK. 

1. Set up Azure ML workspace - workspace.py
2. Create and register datastore - datastore.py
3. Upload files to datastore - upload.py
4. Create and register dataset - dataset.py
5. Registering a new dataset from an existing registered dataset - dataprocessing.py
6. Access all assets within a subscription (like workspaces, datastores, datasets) - access.py
7. Create and run an experiment - experiment.py
8. Create and submit a job to run script to enable running experiment with an environment for replication across different machines - script_to_run.py, script_job.py
9. Train a ML model as a script - model_script.py
10. Run ML model script as an experiment with environment - model_job.py
11. Running ML experiment as a pipelie - dataprep_pipeline.py, training_pipeline.py, pipeline_job.py
12. Create and run model for webservice - webservice_model.py
13. Register a ML model using run_id - register_model.py
14. Register a ML model using local model pickle file - register_pickle_model.py
15. Create a webservice for serving the ML model - ./service_files/scoring_script.py, deploy_job.py
16. Consuming the model webservice from workspace - consume_webservice.py
17. Consuming the model webservice using REST api - api_test.py

### NOTE: Create an upstream All+Data+Files folder when setting up your own repo to run the files without issues. Or change the paths within the dataset.py
