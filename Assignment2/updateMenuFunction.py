def lambda_handler(event, context):
    import boto3
    from botocore.exceptions import ClientError
    
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    
    table = dynamodb.Table('Menu')
    
    try:
        menuId=event['menuId']
        
        response = table.update_item(
           Key={
                'menuId': menuId
            },UpdateExpression = 'set selection = :val1',
        ExpressionAttributeValues = {
            ':val1': event['selection']
        },
        ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("PutItem succeeded:")
        return "200 OK"
   