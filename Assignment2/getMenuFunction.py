def lambda_handler(event, context):
    import boto3
    import json
    import decimal
    from botocore.exceptions import ClientError

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table('Menu')

    try:
        response = table.get_item(
            Key={
                'menuId': event['menuId']
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print("GetItem succeeded:")
        return item
