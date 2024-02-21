import json
import decimal
from boto3.dynamodb.conditions import Key
import boto3


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            # Convert decimal instances to strings to preserve precision.
            return str(o)
        return super(DecimalEncoder, self).default(o)


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event))
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("users")

    # Scan the table (Note: Use query for more efficient, key-based access)
    response = table.scan()

    items = response["Items"]
    return {"statusCode": 200, "body": json.dumps(items, cls=DecimalEncoder)}
