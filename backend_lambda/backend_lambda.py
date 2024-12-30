# import the JSON utility package
import json
# import the Python math library
import math

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):

# extract the two numbers from the Lambda service's event object
    base = int(event["base"])
    exponent = int(event["exponent"])
    event_str = json.dumps(event)
    
    math_result = math.pow(base, exponent)

    response = {
        "result": math_result,
        "event": event_str
    }

    # return a properly formatted JSON object
    return {
    'statusCode': 200,
    'body': response
    }
