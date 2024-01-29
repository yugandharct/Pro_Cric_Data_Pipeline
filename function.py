from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "prj-poc-001"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://bkt-dataflow-metadata00/udf.js",
        "JSONPath": "gs://bkt-dataflow-metadata00/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "cricket-data-410916:Cricket_dataset.ICC_ODI_Batsmen_Ranking",
        "inputFilePattern": "gs://cricket-bucket-00/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://bkt-dataflow-metadata00",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

