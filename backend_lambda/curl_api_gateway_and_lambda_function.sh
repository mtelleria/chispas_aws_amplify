#!/bin/sh

# https://b1052wf6p3.execute-api.eu-west-3.amazonaws.com/DEV/books

set -x

API_GATEWAY_URL=https://lxf8gxyp35.execute-api.eu-west-3.amazonaws.com/dev/books

LAMBDA_URL=https://3uru7prmi2lwjamxpy2gi45cwi0phcgp.lambda-url.eu-west-3.on.aws
LAMBDA_URL2=https://uyxt474xa7hyqrx47si4pmf7pa0clckv.lambda-url.eu-west-3.on.aws/

# API gateway
curl --silent -X POST $API_GATEWAY_URL  -H 'content-type: application/json' -d '{"base": "3", "exponent":"4"}' | python3 -m json.tool

echo "\n\nNOW with FUNCTION URL\n"


# Lambda function
curl --silent -X POST $LAMBDA_URL\
     -H 'content-type: application/json'\
     -d '{"base": "3", "exponent":"4"}' | python3 -m json.tool


echo "\n\nNOW with FUNCTION URL 2\n"


# Lambda function
curl --silent -X POST $LAMBDA_URL2\
     -H 'content-type: application/json'\
     -d '{"base": "3", "exponent":"4"}' | python3 -m json.tool



