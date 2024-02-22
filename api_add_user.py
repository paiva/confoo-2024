import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("users")


def lambda_handler(event, context):

    print("Received event: " + json.dumps(event))

    try:
        # API Gateway with Lambda Proxy Integration passes the request payload as a JSON string in 'event['body']'
        body = event
    except (KeyError, TypeError, json.JSONDecodeError):
        return {"statusCode": 400, "body": "Invalid request"}

    # Extract and validate data
    user_id = body.get("user_id")
    firstname = body.get("firstname")
    lastname = body.get("lastname")
    affiliation = body.get("affiliation")
    email = body.get("email")

    if not all([user_id, firstname, lastname, email]):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Missing required fields"}),
        }

    try:
        response = table.put_item(
            Item={
                "user_id": int(user_id),
                "firstname": firstname,
                "lastname": lastname,
                "affiliation": affiliation,
                "email": email,
            }
        )
        print("Put Item Response:", response)
    except Exception as e:
        print("Error saving to DynamoDB:", str(e))
        return {"statusCode": 500, "body": json.dumps({"message": "Error saving user"})}

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "User saved successfully", "user_id": user_id}),
    }
