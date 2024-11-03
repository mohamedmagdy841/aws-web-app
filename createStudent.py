import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='YOUR_REGION')
table = dynamodb.Table('TABLE_NAME')

def lambda_handler(event, context):
    # Extract values from the event object we got from the Lambda service and store in variables
    student_id = event['studentid']
    name = event['name']
    student_class = event['class']
    age = event['age']
    
    # Write student data to the DynamoDB table and save the response in a variable
    response = table.put_item(
        Item={
            'studentid': student_id,
            'name': name,
            'class': student_class,
            'age': age
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Student data saved successfully!')
    }
