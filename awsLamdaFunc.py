import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'question_bank'  

def lambda_handler(event, context):
    try:
        if event['resource'] == '/questions':
            if event['httpMethod'] == 'GET':
                # Retrieve data from DynamoDB table
                table = dynamodb.Table(table_name)
                response = table.scan()
                items = response['Items']
                
                # Format the response
                formatted_response = []
                for item in items:
                    formatted_item = {
                        'id': item['id'],
                        'question': item['question'],
                        'choices': item['choices'],
                        'correct_answer': item['correct_answer']
                    }
                    formatted_response.append(formatted_item)
                
                return {
                    'statusCode': 200,
                    'body': json.dumps(formatted_response)
                }
            elif event['httpMethod'] == 'POST':
                # Create a new item in DynamoDB table
                table = dynamodb.Table(table_name)
                data = json.loads(event['body'])
                table.put_item(Item=data)
                
                return {
                    'statusCode': 201,
                    'body': json.dumps("Item created successfully")
                }
            else:
                return {
                    'statusCode': 405,
                    'body': json.dumps("Method not allowed")
                }
        elif event['resource'] == '/questions/{id}':
            if event['httpMethod'] == 'GET':
                # Retrieve data for a specific item from DynamoDB table
                table = dynamodb.Table(table_name)
                item_id = event['pathParameters']['id']
                response = table.get_item(Key={'id': item_id})
                if 'Item' not in response:
                    return {
                        'statusCode': 404,
                        'body': json.dumps("Item not found")
                    }
                else:
                    return {
                        'statusCode': 200,
                        'body': json.dumps(response['Item'])
                    }
            elif event['httpMethod'] == 'PUT':
                # Update an existing item in DynamoDB table
                table = dynamodb.Table(table_name)
                data = json.loads(event['body'])
                item_id = event['pathParameters']['id']
                data['id'] = item_id
                table.put_item(Item=data)
                
                return {
                    'statusCode': 200,
                    'body': json.dumps("Item updated successfully")
                }
            elif event['httpMethod'] == 'DELETE':
                # Delete an existing item from DynamoDB table
                table = dynamodb.Table(table_name)
                item_id = event['pathParameters']['id']
                table.delete_item(Key={'id': item_id})
                
                return {
                    'statusCode': 200,
                    'body': json.dumps("Item deleted successfully")
                }
            else:
                return {
                    'statusCode': 405,
                    'body': json.dumps("Method not allowed")
                }
        elif event['resource'] == '/questions/search':
            if event['httpMethod'] == 'GET':
                # Retrieve search query from query parameters
                search_query = event['queryStringParameters']['q']
                
                # Retrieve data from DynamoDB table based on search query
                table = dynamodb.Table(table_name)
                response = table.scan()
                items = response['Items']
                
                # Filter items based on search query
                formatted_response = []
                for item in items:
                    # Iterate through all attributes of the item
                    for attribute_name, attribute_value in item.items():
                        # Check if the attribute value contains the search query
                        if isinstance(attribute_value, str) and search_query.lower() in attribute_value.lower():
                            formatted_item = {
                                'id': item['id'],
                                'question': item['question'],
                                'choices': item['choices'],
                                'correct_answer': item['correct_answer']
                            }
                            formatted_response.append(formatted_item)
                            break  # If any attribute contains the search query, add the item to the response and move to the next item
                
                return {
                    'statusCode': 200,
                    'body': json.dumps(formatted_response)
                }
            else:
                return {
                    'statusCode': 405,
                    'body': json.dumps("Method not allowed")
                }
        elif event['resource'] == '/status':
            if event['httpMethod'] == 'GET':
                # Perform a simple status check
                status_message = "Server is up"
                return {
                    'statusCode': 200,
                    'body': json.dumps(status_message)
                }
            else:
                return {
                    'statusCode': 405,
                    'body': json.dumps("Method not allowed")
                }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps("Resource not found")
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
