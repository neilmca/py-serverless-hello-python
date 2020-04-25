import json
import boto3
import os


def hello(event, context):
    
    client = boto3.client("lambda")
    flist = client.list_functions()
    
    
    body = {
        "message": os.environ['MY_ENV'],
        
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    print "this goes to the logs"

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
