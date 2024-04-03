```python
import json
import boto3
from decimal import Decimal

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
question_table_name = 'question_bank'
highscore_table_name = 'awscphighscore'

# Lambda function entry point
def lambda_handler(event, context):
    try:
        # Define CORS headers
        cors_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH',
            'Access-Control-Allow-Headers': 'Content-Type'
        }

        # Handle requests based on resource paths
        if event['resource'] == '/questions':
            if event['httpMethod'] == 'GET':
                # Retrieve data from DynamoDB table
                table = dynamodb.Table(question_table_name)
                response = table.scan()
                items = response['Items']
                
                # Convert Decimal objects to strings
                items = convert_decimal_to_string(items)
                
                # Return response with CORS headers
                return {
                    'statusCode': 200,
                    'headers': cors_headers,
                    'body': json.dumps(items)
                }
            elif event['httpMethod'] == 'POST':
                # Create a new item in DynamoDB table
                table = dynamodb.Table(question_table_name)
                data = json.loads(event['body'], parse_float=Decimal)  # Parse floats as Decimal objects
                
                # Check if the request body contains the 'id' field
                if 'id' not in data:
                    # Retrieve the highest existing ID in the database
                    highest_id = get_highest_id(table)
                    if highest_id is None:
                        highest_id = 0
                    
                    # Increment the ID and assign it to the new item
                    data['id'] = highest_id + 1
                
                # Use promises to put item into table
                response = table.put_item(Item=data)
                
                # Return response with CORS headers
                return {
                    'statusCode': 201,
                    'headers': cors_headers,
                    'body': json.dumps("Item created successfully")
                }
            else:
                return {
                    'statusCode': 405,
                    'headers': cors_headers,
                    'body': json.dumps("Method not allowed")
                }
        
        elif event['resource'] == '/questions/{id}':
            if event['httpMethod'] == 'PATCH':
                # Update an existing item in DynamoDB table
                table = dynamodb.Table(question_table_name)
                data = json.loads(event['body'], parse_float=Decimal)  # Parse floats as Decimal objects
                item_id = event['pathParameters']['id']
                data['id'] = item_id
                
                # Use promises to put item into table
                response = table.put_item(Item=data)
                
                # Return response with CORS headers
                return {
                    'statusCode': 200,
                    'headers': cors_headers,
                    'body': json.dumps("Item updated successfully")
                }
            elif event['httpMethod'] == 'DELETE':
                # Delete an existing item from DynamoDB table
                table = dynamodb.Table(question_table_name)
                item_id = event['pathParameters']['id']
                
                try:
                    # Use the delete_item method to delete the item by its ID
                    response = table.delete_item(
                        Key={
                            'id': item_id
                        }
                    )
                    
                    # Return response with CORS headers
                    return {
                        'statusCode': 200,
                        'headers': cors_headers,
                        'body': json.dumps("Item deleted successfully")
                    }
                except Exception as e:
                    return {
                        'statusCode': 500,
                        'headers': cors_headers,
                        'body': json.dumps(str(e))
                    }
            else:
                return {
                    'statusCode': 405,
                    'headers': cors_headers,
                    'body': json.dumps("Method not allowed")
                }
        
        elif event['resource'] == '/questions/search':
            if event['httpMethod'] == 'GET':
                # Retrieve search query from query parameters
                search_query = event['queryStringParameters']['q']
                
                # Retrieve data from DynamoDB table based on search query
                table = dynamodb.Table(question_table_name)
                response = table.scan()
                items = response['Items']
                
                # Filter items based on search query
                formatted_response = []
                for item in items:
                    # Iterate through all attributes of the item
                    for attribute_name, attribute_value in item.items():
                        # Check if the attribute value contains the search query
                        if isinstance(attribute_value, str) and search_query.lower() in attribute_value.lower():
                            # Convert Decimal objects to strings
                            item = convert_decimal_to_string(item)
                            formatted_response.append(item)
                            break  # If any attribute contains the search query, add the item to the response and move to the next item
                
                # Return response with CORS headers
                return {
                    'statusCode': 200,
                    'headers': cors_headers,
                    'body': json.dumps(formatted_response)
                }
            else:
                return {
                    'statusCode': 405,
                    'headers': cors_headers,
                    'body': json.dumps("Method not allowed")
                }
        
        elif event['resource'] == '/status':
            if event['httpMethod'] == 'GET':
                # Perform a simple status check
                status_message = "Server is up"
                
                # Return response with CORS headers
                return {
                    'statusCode': 200,
                    'headers': cors_headers,
                    'body': json.dumps(status_message)
                }
            else:
                return {
                    'statusCode': 405,
                    'headers': cors_headers,
                    'body': json.dumps("Method not allowed")
                }
        
        elif event['resource'] == '/highscores':
            if event['httpMethod'] == 'GET':
                # Retrieve all high scores from the awscphighscore table
                table = dynamodb.Table(highscore_table_name)
                response = table.scan()
                items = response['Items']
                
                # Convert Decimal objects to strings
                items = convert_decimal_to_string(items)
                
                # Return response with CORS headers
                return {
                    'statusCode': 200,
                    'headers': cors_headers,
                    'body': json.dumps(items)
                }
            elif event['httpMethod'] == 'POST':
                # Create a new item in the awscphighscore table
                table = dynamodb.Table(highscore_table_name)
                data = json.loads(event['body'], parse_float=Decimal)  # Parse floats as Decimal objects
                
                # Use promises to put item into table
                response = table.put_item(Item=data)
                
                # Return response with CORS headers
                return {
                    'statusCode': 201,
                    'headers': cors_headers,
                    'body': json.dumps("Score added successfully")
                }
            else:
                return {
                    'statusCode': 405,
                    'headers': cors_headers,
                    'body': json.dumps("Method not allowed")
                }
        
        else:
            return {
                'statusCode': 404,
                'headers': cors_headers,
                'body': json.dumps("Resource not found")
            }
    
    except Exception as e:
        # Return response with CORS headers
        return {
            'statusCode': 500,
            'headers': cors_headers,
            'body': json.dumps(str(e))
        }

# Helper function to convert Decimal objects to strings
def convert_decimal_to_string(data

):
    if isinstance(data, list):
        return [convert_decimal_to_string(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_decimal_to_string(value) for key, value in data.items()}
    elif isinstance(data, Decimal):
        return str(data)
    else:
        return data

# Helper function to get the highest ID from the table
def get_highest_id(table):
    response = table.scan(Select='COUNT', ProjectionExpression='id')
    return response['Count']
```