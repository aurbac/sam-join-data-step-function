import json
import boto3
import os

def lambda_handler(event, context):

    print(event)
    STATE_MACHINE_ARN = os.environ['STATE_MACHINE_ARN']

    sfn_client = boto3.client('stepfunctions')
    
    response = sfn_client.start_execution(
        stateMachineArn=STATE_MACHINE_ARN,
        input="{\"source1\": \""+event['source1']+"\",\"source2\": \""+event['source2']+"\",\"jobid\": \""+event['jobid']+"\"}",
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
