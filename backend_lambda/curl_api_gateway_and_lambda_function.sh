#!/bin/sh

# API gateway
curl -X POST https://0fg461p92j.execute-api.eu-west-3.amazonaws.com/DEV  -d '{"base": "3", "exponent":"4"}'

echo "\n\nNOW with FUNCTION URL\n"


# Lambda function
curl -X POST https://3uru7prmi2lwjamxpy2gi45cwi0phcgp.lambda-url.eu-west-3.on.aws\
     -H 'content-type: application/json'\
     -d '{"base": "3", "exponent":"4"}'



