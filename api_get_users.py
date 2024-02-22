import json
import decimal
import boto3


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            # Convert decimal instances to strings to preserve precision.
            return str(o)
        return super(DecimalEncoder, self).default(o)


# "`lambda_handler`: Entry point for the lambda function"
#
# "The `event` object contains information from the invoker, which could be an"
# "AWS service or a custom application"
#
# "The `context` object provides methods and properties that provide information"
# "about the invocation, function, and execution environment.#
def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event))
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("users")

    # Scan the table (Note: Use query for more efficient, key-based access)
    response = table.scan()

    items = response["Items"]
    return {"statusCode": 200, "body": json.dumps(items, cls=DecimalEncoder)}


# Full Configuration
# https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/api_get_users?tab=configure
