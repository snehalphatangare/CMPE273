def lambda_handler(event, context):
    import boto3

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table('Menu')

    menuId=event.get('menu_id')
    store_name=event.get('store_name')
    selection=event.get('selection')
    size=event.get('size')
    price=event.get('price')
    store_hours=event.get('store_hours')
    response = table.put_item(
       Item={
            'menuId': menuId,
            'store_name': store_name,
            'selection': selection,
            'size': size,
            'price': price,
            'store_hours': store_hours
        }
    )

    print("PutItem succeeded:")
    return "200 OK"
