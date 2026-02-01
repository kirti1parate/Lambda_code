def lambda_handler(event, context):
    # TODO implement
    response_data = {
    "message":"Hello! your GET request was received successfully" ,
    "Status":"Success"
    }

    return {
    "statusCode": 200,
    "headers":{
        "Content_type": "application/json"},
    "body": json.dumps(response_data)
}
