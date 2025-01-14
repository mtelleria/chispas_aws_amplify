# import the JSON utility package
import json

# For timestamping
import time

# import the Python math library
import math

# import the AWS SDK (for Python the package name is boto3)
import boto3

# Initial actions
# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
dynamodb_table = dynamodb.Table('powerofmath')
# store the current time in a human readable format in a variable
now = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())


# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):

    invoker = context.invoked_function_arn

    # If called from the function_url the event contains a lot of metadata, input is in "body"
    # If called from the test or from API Gateway the event just contains the input
    if "body" in event:
        event_body_str = event["body"]
        event_body = json.loads(event_body_str)
    else:
        event_body = event
        
    # extract the two numbers from the Lambda service's event object
    base = int(event_body["base"])
    exponent = int(event_body["exponent"])
    math_result = math.pow(base, exponent)

    db_response = dynamodb_table.put_item( Item={
        'ID': str(math_result),
        'LatestGreetingTime':now
    })

    
    
    response = {
        "result": math_result,
        "invoker": invoker,
        "event": event
    }

    # return a properly formatted JSON object
    # IMPORTANT:  Body must be a string, not a dictionary. Otherwise proxy lambda will fail
    return {
        "isBase64Encoded": False,
        'statusCode': 200,
        "headers": {"Access-Control-Allow-Origin":"*"},
        "multiValueHeaders":{},
        'body': json.dumps(response) }



